import os.path
import tempfile
from pathlib import Path

import PyPDF2
import fillpdf.fillpdfs
from PyPDF2 import PdfFileReader, PdfWriter, PdfReader
from PyPDF2_Fields import make_writer_from_reader, PdfFieldType, \
    set_need_appearances
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
    set_need_appearances(writer, bool_val=True)

    with open(file_path, 'wb') as output_stream:
        writer.write(output_stream)


class ExceptionListAgreement:

    def __init__(self):
        input_folder = os.path.join(os.getcwd(), 'PDFs')
        ouput_folder = os.path.join(os.getcwd(), 'Filled_Form')
        self.input_file_path = os.path.join(input_folder,
                                            'residential_sale.pdf')
        self.output_file_path = os.path.join(ouput_folder,
                                             'exception_list_agreement.pdf')
        self.reader = PdfFileReader(Path(self.input_file_path).open(mode='rb'), strict=False)
        self.writer = make_writer_from_reader(self.reader, editable=False)

    def write_to_file(self, data):
        # fields = fillpdf.fillpdfs.get_form_fields(self.input_file_path, page_number=15)
        # fields = self.reader.get_fields()
        # print(fields)
        content = {'Commission %': data.get('commission', '2')}

        self.writer.updatePageFormFieldValues(self.writer.getPage(14), content)

        set_need_appearances(self.writer, bool_val=True)
        with open(self.output_file_path, 'wb') as output_stream:
            self.writer.write(output_stream)
        get_write_page(self.output_file_path, 14)

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
