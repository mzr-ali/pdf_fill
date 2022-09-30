import os.path
import tempfile
from datetime import datetime
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


class Form244Form:

    def __init__(self):
        self.input_file_path = os.path.join('static/PDFs', 'residential_sale.pdf')
        self.output_file_path = os.path.join('media', 'form_244.pdf')
        self.reader = PdfFileReader(Path(self.input_file_path).open(mode='rb'), strict=False)
        self.writer = PdfWriter()

    def write_to_file(self, data):
        # fields = fillpdf.fillpdfs.get_form_fields(self.input_file_path, page_number=13)
        # fields = self.reader.get_fields()
        # print(fields)
        self.writer.add_page(self.reader.getPage(12))
        present_date = data.get('present_date', "2022-10-02")
        present_date = datetime.strptime(present_date, "%Y-%m-%d").strftime("%y-%b-%d").split("-")
        content = {
            'txtp_streetnum': data.get('street_num', ''),
            'txtp_street': data.get('street'),
            'txtp_UnitNumber':  data.get('unit_num'),
            'txtp_city':  data.get('city'),
            'txtp_state':  data.get('state'),
            'txtp_zipcode': data.get('zip_code'),
            'txtseller1':  data.get('seller_1'),
            'hidsand':  data.get('hidsand'),
            'txtseller2': data.get('seller_2'),
            'txtl_broker':  data.get('broker'),
            'txtmlsnumber':  data.get('msl_number'),
            'txtl_brokerid':  data.get('broker_id'),
            'txtinterboardmls':  data.get('interboaard_mls'),
            'txtboard':  data.get('board'),
            'txtp_listdate':  data.get('list_date'),
            'txttimelimit_time': data.get('time_limit'),
            'chkOpt_SofferTime':  data.get('offer_time'),
            'txtNoPresentation_d':present_date[-1],
            'txtNoPresentation_m': present_date[1],
            'txtNoPresentation_y': present_date[0],
            'txtotherdirection': data.get('other_dir'),
            'txtotherdirection1': data.get('other_dir1'),
            'txtotherdirection2': data.get('other_dir2'),
            'txtotherdirection3': data.get('other_dir3'),
            'txtsellersig1': data.get('seller1_sig'),
            'txtsellersig2': data.get('seller2_sig'),
            'txtl_brkagentsig': data.get('borkger_sig'),
            'DISCLAIMER': data.get('disclaimer',"")
        }

        self.writer.updatePageFormFieldValues(self.writer.getPage(0), content)

        set_need_appearances(self.writer, bool_val=True)
        with open(self.output_file_path, 'wb') as output_stream:
            self.writer.write(output_stream)
        # get_write_page(self.output_file_path, 12)

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
