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


def on_off(val):
    val = val if val else "0"
    if int(val) == 1:
        return 'On'
    return "Off"


class AppInstructions:

    def __init__(self):
        self.file_path = os.path.join('static/PDFs', 'Appt_Instructions_editable.pdf')
        self.output_path = os.path.join('media', 'appt_instruction.pdf')

    def read_write_first_page(self, data):
        fields = fillpdfs.get_form_fields(self.file_path)
        print(self.output_path)
        fields_to_file = {'Property': data.get('property_name', ''),
                          'New  Appt': on_off(data.get('new_appt', '')),
                          'Denied': on_off(data.get('denied', '')),
                          'Cancelled': on_off(data.get('cancelled', '')),
                          'Agent': data.get('agent_name', ''),
                          'Confirmed': on_off(data.get('confirmed', '')),
                          'Time Change': on_off(data.get('time_change', '')),
                          'Reminders': on_off(data.get('reminder', '')),
                          'Appointment Duration':data.get('appointment_duration', ''),#['1 hour', '1/2 Hour', '15 minutes']
                          'Min Notice Required': data.get('min_notice', '2'),
                          'Allow Double Bookings': data.get('double_booking'.upper(), 'YES'),#['YES', 'NO']
                          'LBX / Other Code': data.get('lbx_instruct', ''),
                          'instructions': data.get('instructions', ''),
                          'Is there an Alarm': data.get("is_alaram", 'YES_2'),# ['YES_2', 'NO_2']
                          'Alarm Code': data.get('alaram_code', ''),
                          'Turn Off Lights': on_off(data.get('turn_off_lights', '')),
                          'Remove Shoes': on_off(data.get('remove_shoes', '')),
                          'Leave Card': on_off(data.get('leave_card', '')),
                          'Lock Doors': on_off(data.get('lock_doors', '')),
                          'Call if late': on_off(data.get('call_if_late', '')),
                          'Knock First': on_off(data.get('knock_first', '')),
                          'Bring RECO Lic': on_off(data.get('bring_reco_lic', '')),
                          'Name': data.get('contact_name_1', ''),
                          'Area Code': data.get('contact_1_areacode', ''),
                          'Phone': data.get('contact_1_phone1', ''),
                          'Email': data.get('contact_1_email', ''),
                          'Email_2': on_off(data.get('contact_1_notify_email', '')),
                          'Text Msg': on_off(data.get('contact_1_notify_text', '')),
                          'Must Call': on_off(data.get('contact_1_notify_call', '')),
                          'Can Confirm': on_off(data.get('contact_1_canconfirm', '')),
                          'Can Deny': on_off(data.get('contact_1_candenied', '')),
                          'New  Appt_2': on_off(data.get('contact_1_appt', '')),
                          'Denied_2': on_off(data.get('contact_1_denied', '')),
                          'Cancelled_2': on_off(data.get('contact_1_cancelled', '')),
                          'Confirmed_2': on_off(data.get('contact_1_confirmed', '')),
                          'Time Change_2': on_off(data.get('contact_1_timechange', '')),
                          'Reminders_2': on_off(data.get('contact_1_reminder', '')),
                          'Name_2': data.get('contact_2_name', ''),
                          'Phone_2': data.get('contact_2_areacode', ''),
                          'undefined_4': data.get('contact_2_phone1', ''),
                          'undefined_5': data.get('contact_2_phone2', ''),
                          'Email_3': data.get('contact_2_email', ''),
                          'Email_4': on_off(data.get('contact_2_notify_email', '')),
                          'Text Msg_2': on_off(data.get('contact_2_notify_text', '')),
                          'Must Call_2': on_off(data.get('contact_2_notify_call', '')),
                          'Can Confirm_2': on_off(data.get('contact_2_canconfirm', '')),
                          'Can Deny_2': on_off(data.get('contact_2_candenied', '')),
                          'New  Appt_3': on_off(data.get('contact_2_appt', '')),
                          'Denied_3': on_off(data.get('contact_2_denied', '')),
                          'Cancelled_3': on_off(data.get('contact_2_cancelled', '')),
                          'Confirmed_3': on_off(data.get('contact_2_confirmed', '')),
                          'Time Change_3': on_off(data.get('contact_2_timechange', '')),
                          'Reminders_3': on_off(data.get('contact_2_reminder', '')),
                          'Admin / Front-desk instructions': data.get('admin_instruction', ''),
                          'Restricted Times / Days / Special instructions': data.get('Restricted Times', ''),
                          'Other info for showing agent': data.get('Other info for showing agent', ''),
                          'Access instructions': data.get('access_instruction', 'door code'), #['door code', 'go direct', 'key', 'sentrilock', 'lock box']
                          'Phone_1': data.get('contact_1_phone2', ''),
                          'MLS #': data.get('mls_number', ''),
                          'Property_2': data.get('Property_2', ''),
                          'Agent_2': data.get('Agent_2', ''),
                          'At Location': data.get('At Location', ''),
                          'Date': data.get('Date', ''),
                          'Time': data.get('Time', ''),
                          'Are you accepting preemptive offers': data.get('preemtive offers', 'YES_3'), # ['YES_3', 'NO_3']
                          'To Email': data.get('To Email', ''),
                          'Are you requesting a minimum irrevocable': data.get('minimum irrevocable', 'YES_4'),#['YES_4', 'NO_4']
                          'To Fax': data.get('To Fax', ''),
                          'If yes how long': data.get('how long', ''),
                          'Is there any additional information you would like to include in the automated notification that goes to the showing agents when an offer is registered': data.get(
                              'additional information', ''),
                          'In person': data.get('In person', ''),
                          'By Email': data.get('By Email', ''),
                          'Fax': data.get('Fax', ''),
                          'Other': data.get('Other', ''),
                          'Text8': data.get('Text8', ''),
                          'Other offer details': data.get('Other offers', ''),
                          'Offers': data.get('Offers', ''),
                          'Automated Offer Notifications': data.get('notification', '')} #['All agents', 'Agents with registered offers', 'Do Not Send']

        fillpdfs.write_fillable_pdf(self.file_path, output_pdf_path=self.output_path, data_dict=fields_to_file, flatten=True)
        return self.output_path

    # def insert_signature(self):
    #     page = self.reader.pages[2]
    #     sig_fodler = os.path.join(os.getcwd(), "SIGNATURES")
    #     sig_file = os.path.join(sig_fodler, f"signature.png")
    #     sig_tmp_filename = _get_tmp_filename()
    #     c = canvas.Canvas(sig_tmp_filename, pagesize=page.cropBox)
    #     c.drawImage(sig_file, 300, 130, 150, 70, mask='auto')
    #
    #     c.showPage()
    #     c.save()
    #     sig_tmp_fh = open(sig_tmp_filename, 'rb')
    #     sig_tmp_pdf = PyPDF2.PdfFileReader(sig_tmp_fh)
    #     sig_page = sig_tmp_pdf.getPage(0)
    #     sig_page.mediaBox = page.mediaBox
    #     page.mergePage(sig_page)
    #     return page

        # sig_fodler = os.path.join(os.getcwd(), "SIGNATURES")
        # sig_file = os.path.join(sig_fodler, f"signature.png")
        # output_fodler = os.path.join(os.getcwd(), "fiiled_form")
        # file_path = os.path.join(output_fodler, f"{os.path.basename(input_file).split('.')[0]}-sig.pdf")
        # sign_pdf(input_file,3,300,130,150,70, file_path, sig_file)
