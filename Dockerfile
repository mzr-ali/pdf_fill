FROM python:3.10-alpine3.16
LABEL maintainer="Mazhar Ali"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000
ARG DEV=false
ARG PYMUPDF_VERSION=1.20.1
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache \
        build-base \
        gcc \
        jbig2dec \
        jpeg-dev \
        harfbuzz-dev \
        libc-dev \
        mupdf-dev \
        musl-dev \
        openjpeg-dev \
        swig \
    && ln -s /usr/lib/libjbig2dec.so.0 /usr/lib/libjbig2dec.so && \
    apk add --update --no-cache --virtual .tmp-build-dev \
      build-base postgresql-dev &&  \
    wget https://github.com/pymupdf/PyMuPDF/archive/refs/tags/${PYMUPDF_VERSION}.tar.gz \
    && tar -xzf ${PYMUPDF_VERSION}.tar.gz \
    && rm ${PYMUPDF_VERSION}.tar.gz \
    && cd PyMuPDF-${PYMUPDF_VERSION} \
    && python setup.py build && python setup.py install&&\
    /py/bin/pip pypdf2 fillpdf && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
      then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    apk del .tmp-build-dev && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user \

RUN

ENV PATH="/py/bin:$PATH"
USER django-user