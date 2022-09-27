import os.path
import tempfile
from datetime import datetime

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


class Form200A:

    def __init__(self, form200a_name):
        folder_path = os.path.join(os.getcwd(), 'PDFs')
        file_path = os.path.join(folder_path, form200a_name)
        self.file_name = os.path.basename(file_path).split(".")[0]
        self.file_path = file_path
        self.writer = PdfWriter()
        self.reader = PdfReader(self.file_path)

    def read_write_first_page(self, data):
        page_1 = self.reader.pages[0]
        fields = self.reader.get_fields()
        page_2 = self.reader.pages[1]
        self.writer.add_page(page_1)
        self.writer.add_page(page_2)
        list_date = datetime.strptime(data['List Date'], "%d/%m/%Y")
        list_d = day_format(list_date.date().day)
        list_m = list_date.date().strftime("%B")
        list_y = list_date.date().strftime("%y")
        expire_date = datetime.strptime(data['Expire Date'], "%d/%m/%Y")
        expire_d = day_format(expire_date.date().day)
        expire_m = expire_date.date().strftime("%B")
        expire_y = expire_date.date().strftime("%y")
        broker_address = data['Broker Address']
        if broker_address:
            address, city, state, zip = broker_address.split(',')
            address = address.strip()
            city = city.strip()
            state = state.strip()
            zip = zip.strip()
        else:
            address = city = state = zip = None

        fields_to_file = {
            "txtl_broker": data.get('Broker Name', ''),
            "txtl_brkaddr": address,
            "txtl_brkcity": city,
            "txtl_brkstate": state,
            "txtl_brkzipcode": zip,
            "txtl_brkphone": data.get('Broker Phone', ''),
            "txtseller1": data.get('Seller1 Name', ''),
            "hidAndBSAmp": data.get('hidAndBSAmp', ''),
            "txtseller2": data.get('Seller2 Name', ''),
            "txtp_listdate_d": list_d,
            "txtp_listdate_mmmm": list_m,
            "txtp_listdate_yy": list_y,
            "txtp_expiredate_d": expire_d,
            "txtp_expiredate_mmmm": expire_m,
            "txtp_expiredate_yy": expire_y,
            "txtp_listprice": data.get('Price', ''),
            "txtp_listpricewords": data.get('Price Word', ''),
            "txtCommissionPer": data.get('Commission %', ''),
            "txtCommissionAmt": '' if data.get('Commission %', '') else data.get('Commission Amount', ''),
            "txtCoopCommissionPer": data.get('Coop Commission %', ''),
            "txtCoopCommissionAmt": '' if data.get('Coop Commission %', '') else data.get(
                'Coop Commission Amount', ''),
            "txtHoldoverDays": data.get('holdoverday', ''),

        }

        self.writer.update_page_form_field_values(self.writer.pages[0], fields=fields_to_file)

    def read_write_3rd_page(self, data):
        print(data)
        page_3 = self.insert_signature()
        fields = self.reader.get_fields()
        self.writer.add_page(page_3)
        ack_date = data.get('Acknowledge Date', '')
        proper_address = data.get('Property Address', '')
        if proper_address:
            address, state, zip = proper_address.split(',')
            address = address.strip()
            state = state.strip()
            zip = zip.strip()
        else:
            address = state = zip = None
        if ack_date:
            ack_date_formatted = datetime.strptime(ack_date, "%d/%m/%Y")
            ack_date_d = day_format(ack_date_formatted.date().day)
            ack_date_m = ack_date_formatted.date().strftime("%B")
            ack_y = ack_date_formatted.date().strftime("%y")
        else:
            ack_date_d = ''
            ack_date_m = ''
            ack_y = ''

        fields_to_file = {
            "DISCLAIMER": data.get('Disclaimer', ''),
            "SupplementalInfo": data.get('Suppliment Info', 'NONE'),
            "txtsellersig1": data.get('sig_seller_1', ''),
            "txtS_phone1": data.get('Seller1 Phone', ''),
            "txtsellersig2": data.get('sig_seller_2', ''),
            "txtS2_phone1": data.get('Seller2 Phone', ''),
            "txtSpouseSig": data.get('sig_spouse', ''),
            "txtSpousePhone": data.get('Spouse Phone', ''),
            "txtl_brkagent": data.get('Broker Details', ''),
            "txtAcknowledgementDate_d": ack_date_d,
            "txtAcknowledgementDate_m": ack_date_m,
            "txtAcknowledgementDate_yy": ack_y,
            "txtp_street": address,
            "txtp_streetnum": data.get('p_street_number', ''),
            "txtp_unitNumber": data.get('p_unit_number', ''),
            "txtp_city": data.get('p_city', ''),
            "txtp_state": state,
            "txtp_zipcode": zip,

        }
        self.writer.update_page_form_field_values(self.writer.pages[2], fields=fields_to_file)

    def save_file(self, name):
        output_fodler = os.path.join(os.getcwd(), "Filled_Form")
        file_path = os.path.join(output_fodler, f"{self.file_name}-{name}.pdf")
        with open(file_path, 'wb') as output_stream:
            self.writer.write(output_stream)
        print("Complete")

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
