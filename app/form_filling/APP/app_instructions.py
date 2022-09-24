import os.path
import tempfile

from fillpdf import fillpdfs


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
    if val:
        return 'On'
    return "Off"


def is_alaram_val(val):
    if val.lower() == 'yes':
        return 'YES_2'
    else:
        return 'NO_2'


def premetive_offers_val(val):
    if val.lower() == 'yes':
        return 'YES_3'
    else:
        return 'NO_3'


def minimum_irrevocable_val(val):
    if val.lower() == 'yes':
        return 'YES_4'
    else:
        return 'NO_4'


class AppInstructions:

    def __init__(self):
        self.file_path = os.path.join('static/PDFs', 'Appt_Instructions_editable.pdf')
        self.output_path = os.path.join('media', 'appt_instruction.pdf')

    def read_write_first_page(self, data):
        fields = fillpdfs.get_form_fields(self.file_path)
        print(self.output_path)
        fields_to_file = {'Property': data.get('property_name', ''),
                          'New  Appt': on_off(data.get('property_new_appointment',  False)),
                          'Denied': on_off(data.get('property_denied', '')),
                          'Cancelled': on_off(data.get('property_cancelled',  False)),
                          'Agent': data.get('agent_name', ''),
                          'Confirmed': on_off(data.get('property_confirmed', False)),
                          'Time Change': on_off(data.get('property_time_change',  False)),
                          'Reminders': on_off(data.get('property_reminder', False)),
                          'Appointment Duration': data.get('appointment_duration', ''),
                          # ['1 hour', '1/2 Hour', '15 minutes']
                          'Min Notice Required': data.get('min_notice', '2'),
                          'Allow Double Bookings': data.get('double_booking', 'NO').upper(),  # ['YES', 'NO']
                          'LBX / Other Code': data.get('lbx_code', ''),
                          'instructions': data.get('lbx_located', ''),
                          'Is there an Alarm': is_alaram_val(data.get("is_alarm", 'NO_2')),  # ['YES_2', 'NO_2']
                          'Alarm Code': data.get('alaram_code', ''),
                          'Turn Off Lights': on_off(data.get('turn_off_lights',  False)),
                          'Remove Shoes': on_off(data.get('remove_shoes',  False)),
                          'Leave Card': on_off(data.get('leave_card',  False)),
                          'Lock Doors': on_off(data.get('lock_doors',  False)),
                          'Call if late': on_off(data.get('call_if_late',  False)),
                          'Knock First': on_off(data.get('knock_first',  False)),
                          'Bring RECO Lic': on_off(data.get('bring_reco_lic',  False)),
                          'Name': data.get('contact_name_1', ''),
                          'Area Code': data.get('contact_1_areacode', ''),
                          'Phone': data.get('contact_1_phone1', ''),
                          'Email': data.get('contact_1_email', ''),
                          'Email_2': on_off(data.get('contact_1_notify_email',  False)),
                          'Text Msg': on_off(data.get('contact_1_notify_text',  False)),
                          'Must Call': on_off(data.get('contact_1_notify_call',  False)),
                          'Can Confirm': on_off(data.get('contact_1_canconfirm',  False)),
                          'Can Deny': on_off(data.get('contact_1_candenied',  False)),
                          'New  Appt_2': on_off(data.get('contact_1_appt',  False)),
                          'Denied_2': on_off(data.get('contact_1_denied',  False)),
                          'Cancelled_2': on_off(data.get('contact_1_cancelled',  False)),
                          'Confirmed_2': on_off(data.get('contact_1_confirmed',  False)),
                          'Time Change_2': on_off(data.get('contact_1_timechange',  False)),
                          'Reminders_2': on_off(data.get('contact_1_reminder',  False)),
                          'Name_2': data.get('contact_2_name', ''),
                          'Phone_2': data.get('contact_2_areacode', ''),
                          'undefined_4': data.get('contact_2_phone1', ''),
                          'undefined_5': data.get('contact_2_phone2', ''),
                          'Email_3': data.get('contact_2_email', ''),
                          'Email_4': on_off(data.get('contact_2_notify_email',  False)),
                          'Text Msg_2': on_off(data.get('contact_2_notify_text',  False)),
                          'Must Call_2': on_off(data.get('contact_2_notify_call',  False)),
                          'Can Confirm_2': on_off(data.get('contact_2_canconfirm',  False)),
                          'Can Deny_2': on_off(data.get('contact_2_candenied',  False)),
                          'New  Appt_3': on_off(data.get('contact_2_appt',  False)),
                          'Denied_3': on_off(data.get('contact_2_denied',  False)),
                          'Cancelled_3': on_off(data.get('contact_2_cancelled',  False)),
                          'Confirmed_3': on_off(data.get('contact_2_confirmed',  False)),
                          'Time Change_3': on_off(data.get('contact_2_timechange',  False)),
                          'Reminders_3': on_off(data.get('contact_2_reminder',  False)),
                          'Admin / Front-desk instructions': data.get('admin_instruction', ''),
                          # ['Email / Text listing contact(s) & wait for confirmation', 'Leave voicemail & immediatley confirm', 'Property is vacant, always confirm', 'Auto message listing contacts and confirm', 'Call listing agent for confirmation instructions', 'Do not contact listing agent. They will confirm direct.', 'Page listing agent for confirmation instructions', 'Call listing contac(s) & wait for conf']
                          'Restricted Times / Days / Special instructions': data.get('restrict_time', ''),
                          'Other info for showing agent': data.get('showing_agent_info', ''),
                          'Access instructions': data.get('access_instruction', 'door code'),
                          # ['door code', 'go direct', 'key', 'sentrilock', 'lock box']
                          'Phone_1': data.get('contact_1_phone2', ''),
                          'MLS #': data.get('mls_number', ''),
                          'Property_2': data.get('property_name_2', ''),
                          'Agent_2': data.get('agent_name_2', ''),
                          'At Location': data.get('at_location', ''),
                          'Date': data.get('date', ''),
                          'Time': data.get('time', ''),
                          'Are you accepting preemptive offers': premetive_offers_val(data.get('premetive_offers', '')),
                          # ['YES_3', 'NO_3']
                          'To Email': data.get('to_email', ''),
                          'Are you requesting a minimum irrevocable': minimum_irrevocable_val(
                              data.get('minimum_irrevocable', '')),
                          # ['YES_4', 'NO_4']
                          'To Fax': data.get('to_fax', ''),
                          'If yes how long': data.get('how_long', ''),
                          'Is there any additional information you would like to include in the automated notification that goes to the showing agents when an offer is registered': data.get(
                              'additional_information', ''),
                          'In person': on_off(data.get('in_person',  False)),
                          'By Email': on_off(data.get('by_email',  False)),
                          'Fax': on_off(data.get('by_fax',  False)),
                          'Other': on_off(data.get('other_method',  False)),
                          'Text8': data.get('other_method_text', ''),
                          'Other offer details': data.get('other_offer_details', 'Offers accepted anytime'),
                          'Offers': data.get('Offers', ''),  # ['Offers accepted anytime', 'Holding offer date']
                          'Automated Offer Notifications': data.get('notification',
                                                                    'All agents')}  # ['All agents', 'Agents with registered offers', 'Do Not Send']

        fillpdfs.write_fillable_pdf(self.file_path, output_pdf_path=self.output_path, data_dict=fields_to_file,
                                    flatten=True)
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
