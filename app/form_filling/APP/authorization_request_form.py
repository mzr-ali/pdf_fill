import os.path
import tempfile
import time
from pathlib import Path

import PyPDF2
import fillpdf
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from PyPDF2_Fields import PdfFieldType, update_page_fields, make_writer_from_reader, set_need_appearances
from fillpdf import fillpdfs
from reportlab.pdfgen import canvas


def _get_tmp_filename(suffix=".pdf"):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        return fh.name


def field_type_to_str(field_type):
    if field_type == PdfFieldType.NONE:
        return "none"

    elif field_type == PdfFieldType.OTHER:
        return "other"

    elif field_type == PdfFieldType.ACTION_BTN:
        return "action btn"

    elif field_type == PdfFieldType.CHECKBOX:
        return "checkbox"

    elif field_type == PdfFieldType.RADIO_BTN_GROUP:
        return "radio btn group"

    elif field_type == PdfFieldType.TEXT_FIELD:
        return "text"


def day_format(d):
    if d == 1:
        return f'{d}st'
    if d == 2:
        return f'{d}nd'
    if d == 3:
        return f'{d}rd'
    if d < 10:
        return f'{d}th'
    else:
        return f'{d}th'


def on_off(val):
    val = val if val else "0"
    if int(val) == 1:
        return 'On'
    return "Off"


def get_write_page(file_path, page_number):
    reader = PdfReader(file_path)
    writer = PdfWriter()
    writer.add_page(reader.pages[page_number])
    set_need_appearances_writer(writer)

    with open(file_path, 'wb') as output_stream:
        writer.write(output_stream)


def set_need_appearances_writer(writer):
    # See 12.7.2 and 7.7.2 for more information:
    # http://www.adobe.com/content/dam/acom/en/devnet/acrobat/
    #     pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree and add "/NeedAppearances attribute
        if "/AcroForm" not in catalog:
            writer._root_object.update(
                {
                    NameObject("/AcroForm"): IndirectObject(
                        len(writer._objects), 0, writer
                    )
                }
            )

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print("set_need_appearances_writer() catch : ", repr(e))
        return writer


class AuthorizationRequestForm:

    def __init__(self):
        self.input_file_path = os.path.join('static/PDFs', 'residential_sale.pdf')
        self.output_file_path = os.path.join('media', 'authorization_request_form.pdf')


    def write_to_file(self, data):
        # fields = fillpdf.fillpdfs.get_form_fields(self.input_file_path)
        # fields = self.reader.get_fields()
        # print(fields)
        # self.writer.add_page(self.reader.getPage(13))
        content = {
            'Property Address & Postal Code': data.get('property_address', 'address'),
            'Name(s)': data.get('name'),
            'Until date': data.get('offer_until', '24/10'),
            'Initial': '',
            'Initial 2': ''}
        fillpdfs.write_fillable_pdf(self.input_file_path, output_pdf_path=self.output_file_path, data_dict=content,
                                    flatten=True)

        # update_page_fields(self.writer.get_page(13), content)
        # set_need_appearances(self.writer, bool_val=True)
        # with open(self.output_file_path, 'wb') as output_stream:
        #     self.writer.write(output_stream)
        # time.sleep(2)
        # get_write_page(self.output_file_path, 13)

        return self.output_file_path

    def insert_signature(self):
        page = self.reader.pages[2]
        sig_fodler = os.path.join(os.getcwd(), "SIGNATURES")
        sig_file = os.path.join(sig_fodler, f"signature.png")
        sig_tmp_filename = _get_tmp_filename()
        c = canvas.Canvas(sig_tmp_filename, pagesize=page.cropBox)
        c.drawImage(sig_file, 300, 130, 150, 70, mask='auto')

        c.showPage()
        c.save()
        sig_tmp_fh = open(sig_tmp_filename, 'rb')
        sig_tmp_pdf = PyPDF2.PdfFileReader(sig_tmp_fh)
        sig_page = sig_tmp_pdf.getPage(0)
        sig_page.mediaBox = page.mediaBox
        page.mergePage(sig_page)
        return page

        # sig_fodler = os.path.join(os.getcwd(), "SIGNATURES")
        # sig_file = os.path.join(sig_fodler, f"signature.png")
        # output_fodler = os.path.join(os.getcwd(), "Filled_Form")
        # file_path = os.path.join(output_fodler, f"{os.path.basename(input_file).split('.')[0]}-sig.pdf")
        # sign_pdf(input_file,3,300,130,150,70, file_path, sig_file)
