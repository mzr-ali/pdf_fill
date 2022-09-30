import os.path
import tempfile
from pathlib import Path

import PyPDF2
from PyPDF2 import PdfFileReader, PdfWriter, PdfReader
from PyPDF2_Fields import make_writer_from_reader, update_page_fields, RadioBtnGroup, PdfFieldType, \
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


class CheckListForm:

    def __init__(self):
        self.input_file_path = os.path.join('static/PDFs', 'residential_sale.pdf')
        self.output_file_path = os.path.join('media', 'check_list.pdf')
        self.reader = PdfFileReader(Path(self.input_file_path).open(mode='rb'), strict=False)
        self.writer = PdfWriter()

    def write_to_file(self, data):
        self.writer.add_page(self.reader.getPage(0))

        mls_check_list = {
            'Property Address': data.get('property_address', ''),
            'undefined': data.get('mls_num', ''),
            'undefined_2': data.get('ar_mls_num', ''),
            # has listing already been loaded?
            'Check Box1': 0 if data.get('already_loaded_no', False) else None,
            'Check Box2': 0 if data.get('already_loaded_yes', False) else None,

            # will need  another board
            'Check Box4': 0 if data.get('board_yes', False) else None,
            'Check Box3': 0 if data.get('board_no', False) else None,
            'Check Box5': 0 if data.get('already_loaded', False) else None,

            'Check Box6': 0 if data.get('s_data_sheet', False) else None,
            'Check Box7': 0 if data.get('s_listing_agreement', False) else None,
            'Check Box8': 0 if data.get('s_working_with_realtor', False) else None,
            'Check Box9': 0 if data.get('mortgage_verification', False) else None,
            'Check Box10': 0 if data.get('fintrac', False) else None,
            'Check Box11': 0 if data.get('property_facts', False) else None,
            'Check Box12': 0 if data.get('s_appt_instruc', False) else None,
            'Check Box13': 0 if data.get('s_process_to_seller', False) else None,
            'Check Box14': 0 if data.get('s_mls_depart', False) else None,
            'Check Box15': 0 if data.get('s_power_of_attorney', False) else None,
            'Check Box16': 0 if data.get('s_property_officer', False) else None,
            'Check Box17': 0 if data.get('s_property_tenant_ack', False) else None,
            'Check Box18': 0 if data.get('s_speak_design', False) else None,
            'Check Box19': 0 if data.get('s_privacy_act', False) else None,
            'Check Box20': 0 if data.get('s_auth_forms', False) else None,
            'Check Box21': 0 if data.get('except_listing_agreement', False) else None,
            'Check Box22': 0 if data.get('proceedure_agreement', False) else None,
            'Check Box23': 0 if data.get('l_data_sheet', False) else None,
            'Check Box24': 0 if data.get('l_listing_agreement', False) else None,
            'Check Box25': 0 if data.get('l_working_with_realtor', False) else None,
            'Check Box26': 0 if data.get('l_appt_instruc', False) else None,
            'Check Box27': 0 if data.get('l_process_to_seller', False) else None,
            'Check Box28': 0 if data.get('l_mls_depart', False) else None,
            'Check Box29': 0 if data.get('l_power_of_attorney', False) else None,
            'Check Box30': 0 if data.get('l_property_officer', False) else None,
            'Check Box31': 0 if data.get('l_property_tenant_ack', False) else None,
            'Check Box32': 0 if data.get('l_speak_design', False) else None,
            'Check Box33': 0 if data.get('l_privacy_act', False) else None,
            'Check Box34': 0 if data.get('l_auth_forms', False) else None,

        }

        radio_list = [

        ]
        for k, v in mls_check_list.items():
            if k.startswith('Check') and v is not None:
                radio_list.append(RadioBtnGroup(k, '/Yes'))

        # for index, page in enumerate(reader_pages):
        # self.writer.update_page_form_field_values(self.writer.getPage(0), content)
        update_page_fields(self.writer.getPage(0), mls_check_list, *radio_list)

        set_need_appearances(self.writer, bool_val=False)
        with open(self.output_file_path, 'wb') as output_stream:
            self.writer.write(output_stream)
        # get_write_page(self.output_file_path, 0)

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
