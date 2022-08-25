import os.path
import tempfile

import PyPDF2
from fillpdf import fillpdfs
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


class ResidentialLease:

    def __init__(self, input_file):
        folder_path = os.path.join(os.getcwd(), 'PDFs')
        file_path = os.path.join(folder_path, input_file)
        self.file_path = file_path

    def read_write_first_page(self, data):
        fields = fillpdfs.get_form_fields(self.file_path)
        print(fields)

        fields_to_file = {
            'Property Address': None,
            'undefined': None,
            'undefined_2': '',
            'Check Box1': None,
            'Check Box2': None,
            'Check Box4': None,
            'Check Box3': None,
            'Check Box6': None,
            'Check Box7': None,
            'Check Box8': None,
            'Check Box9': None,
            'Check Box10': None,
            'Check Box11': None,
            'Check Box12': None,
            'Check Box13': None,
            'Check Box14': None,
            'Check Box15': None,
            'Check Box16': None,
            'Check Box17': None,
            'Check Box18': None,
            'Check Box19': None,
            'Check Box20': None,
            'Check Box21': None,
            'Check Box22': None,
            'Check Box5': None,
            'Check Box23': None,
            'Check Box24': None,
            'Check Box25': None,
            'Check Box26': None,
            'Check Box27': None,
            'Check Box28': None,
            'Check Box29': None,
            'Check Box30': None,
            'Check Box31': None,
            'Check Box32': None,
            'Check Box33': None,
            'Check Box34': None,
            'Property': '',
            'New  Appt': 'On',
            'Denied': 'On',
            'Cancelled': 'On',
            'Agent': '',
            'Confirmed': 'On',
            'Time Change': 'On',
            'Reminders': 'On',
            'Min Notice Required': '',
            'Allow Double Bookings': 'NO',
            'LBX / Other Code': '',
            'instructions': '',
            'Is there an Alarm': None,
            'Alarm Code': '',
            'Turn Off Lights': 'On',
            'Remove Shoes': 'On',
            'Leave Card': 'On',
            'Lock Doors': 'On',
            'Call if late': 'On',
            'Knock First': 'On',
            'Bring RECO Lic': '',
            'Name': '',
            'Area Code': '',
            'Phone': '',
            'Email': '',
            'Email_2': '',
            'Text Msg': '',
            'Must Call': '',
            'Can Confirm': 'On',
            'Can Deny': '',
            'New  Appt_2': 'On',
            'Denied_2': 'On',
            'Cancelled_2': 'On',
            'Confirmed_2': 'On',
            'Time Change_2': 'On',
            'Reminders_2': 'On',
            'Name_2': '',
            'Phone_2': '',
            'undefined_4': '',
            'undefined_5': '',
            'Email_3': '',
            'Email_4': '',
            'Text Msg_2': '',
            'Must Call_2': '',
            'Can Confirm_2': 'On',
            'Can Deny_2': '',
            'New  Appt_3': 'On',
            'Denied_3': 'On',
            'Cancelled_3': 'On',
            'Confirmed_3': 'On',
            'Time Change_3': 'On',
            'Reminders_3': 'On',
            'Admin / Front-desk instructions': None,
            'Restricted Times / Days / Special instructions': '',
            'Other info for showing agent': '',
            'Appointment Duration': '1/2 Hour',
            'Access instructions': None,
            'Phone_1': '',
            'MLS #': '',
            'Property_2': '',
            'Agent_2': '',
            'At Location': '',
            'Date': None,
            'Time': '',
            'Are you accepting preemptive offers': None,
            'To Email': '',
            'Are you requesting a minimum irrevocable': None,
            'To Fax': '',
            'If yes how long': '',
            'Is there any additional information you would like to include in the automated notification that goes to the showing agents when an offer is registered': '',
            'In person': '',
            'By Email': '',
            'Fax': '',
            'Other': '',
            'Text8': '',
            'Other offer details': '',
            'Offers': None,
            'Automated Offer Notifications': 'All agents',
            'txtp_streetnum': '',
            'txtp_street': '',
            'txtp_UnitNumber': '',
            'txtp_city': '',
            'txtp_state': '',
            'txtp_zipcode': '',
            'txtseller1': '',
            'hidsand': '',
            'txtseller2': '',
            'txtl_broker': '',
            'txtmlsnumber': '',
            'txtl_brokerid': '',
            'txtinterboardmls': '',
            'txtboard': '',
            'txtp_listdate': '',
            'txttimelimit_time': '',
            'chkOpt_SofferTime': '',
            'txtNoPresentation_d': '',
            'txtNoPresentation_m': '',
            'txtNoPresentation_y': '',
            'txtotherdirection': '',
            'txtotherdirection1': '',
            'txtotherdirection2': '',
            'txtotherdirection3': '',
            'txtsellersig1': '',
            'txtsellersig2': '',
            'txtl_brkagentsig': '',
            'DISCLAIMER': '',
            'txtbuyer1': '',
            'hidband': '',
            'txtbuyer2': '',
            'txtp_unitNumber': '',
            'txtFpurpose': '',
            'txtEntryAccess': '',
            'txtFpurpose2': '',
            'txtEntryAccess2': '',
            'txtFpurpose3': '',
            'txtEntryAccess3': '',
            'txtAProp': '',
            'txtadditnlterms': '',
            'txtbuyersig1': '',
            'txtbuyersig2': '',
            'Witness': '',
            'Witness 2': '',
            'Witness 3': '',
            'Buyer': '',
            'Witness 4': '',
            'Buyer 2': '',
            'Date 4': '',
            'Property Address & Postal Code': '',
            'Name\\(s\\)': '',
            'Until date': '',
            'Initial': '',
            'Initial 2': '',
            'Sales Rep / Broker': ''
        }

        fillpdfs.write_fillable_pdf(self.file_path, output_pdf_path='test.pdf', data_dict=fields_to_file)

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
        # output_fodler = os.path.join(os.getcwd(), "fiiled_form")
        # file_path = os.path.join(output_fodler, f"{os.path.basename(input_file).split('.')[0]}-sig.pdf")
        # sign_pdf(input_file,3,300,130,150,70, file_path, sig_file)
