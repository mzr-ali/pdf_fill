import os.path
import tempfile

import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas


def _get_tmp_filename(suffix=".pdf"):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        return fh.name


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


class FormEightOneZero:

    def __init__(self):
        self.input_file_path = os.path.join('static/PDFs', 'residential_sale.pdf')
        self.output_file_path = os.path.join('media', 'form_810.pdf')

        self.reader = PdfReader(self.input_file_path)
        self.writer = PdfWriter()

    def write_to_file(self, data):
        page_1 = self.reader.pages[0]
        fields = self.reader.get_fields()
        self.writer.add_page(page_1)
        fields_to_file = {
            'txtacknowledged': data.get('ack'),
            'txtBroker1': data.get('s_brok_name', 'seller'),
            'txtBroker2': data.get('b_brok_name', 'buy'),
            'txtSigner1': 'signature one',
            'txtSigner2': 'signature two',
            'txtSigner3': 'signature three',
            'txtSigner4': 'signature four'
        }

        self.writer.update_page_form_field_values(self.writer.pages[0], fields=fields_to_file)
        with open(self.output_file_path, 'wb') as output_stream:
            self.writer.write(output_stream)
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
