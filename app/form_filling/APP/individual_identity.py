import os.path
import tempfile
from datetime import datetime
from pathlib import Path

import PyPDF2
from PyPDF2 import PdfFileReader, PdfWriter, PdfReader, PdfFileWriter
from PyPDF2.generic import NameObject
from PyPDF2_Fields import PdfFieldType, \
    set_need_appearances, update_page_fields, RadioBtnGroup
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
    d = int(d)
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


def updateCheckboxValues(page, fields):
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in fields:
            if writer_annot.get('/T') == field:
                writer_annot.update({
                    NameObject("/V"): NameObject(fields[field]),
                    NameObject("/AS"): NameObject(fields[field])
                })


class IndividualIdentity:

    def __init__(self):
        input_folder = os.path.join(os.getcwd(), 'PDFs')
        ouput_folder = os.path.join(os.getcwd(), 'Filled_Form')
        self.input_file_path = os.path.join(input_folder,
                                            'residential_sale.pdf')
        self.output_file_path = os.path.join(ouput_folder,
                                             'indvidual_Identify_record.pdf')
        self.reader = PdfFileReader(Path(self.input_file_path).open(mode='rb'), strict=False)
        self.writer = PdfFileWriter()

    def write_to_file(self, data):
        # fields = fillpdf.fillpdfs.get_form_fields(self.input_file_path, page_number=7)
        fields = self.reader.get_fields()
        expiry_date = data.get('expiry_date', "2022/10/02")
        verify_date = data.get('verify_date', "2022/10/02")
        iden_date = data.get('iden_date', "2022/10/02")
        expiry_date = datetime.strptime(expiry_date, "%Y/%m/%d").strftime("%y-%b-%d").split("-")
        iden_date = datetime.strptime(iden_date, "%Y/%m/%d").strftime("%Y-%b-%d").split("-")
        content = {
            'txtp_streetnum': data.get('p_street_num', '4343'),
            'txtp_street': data.get('p_street'),
            'txtp_unitNumber': data.get('p_unit_num'),
            'txtp_city': data.get('p_city'),
            'txtProvince': data.get('p_sate'),
            'txtp_zipcode': data.get('p_zip'),
            'txtpropAddrLine2': data.get('p_address'),
            'txtAgent': data.get('agent'),
            'txtBroker': data.get('broker'),
            'txtverifieddate1_mmmm': day_format(verify_date[-1]),
            'txtverifieddate1_d': verify_date[1],
            'txtverifieddate1_yyyy': verify_date[0],
            'txtindividualName': data.get('i_name'),
            'txtindividualAddress1': data.get('i_address1'),
            'txtindividualAddress2': data.get('i_address2'),
            'txtindividualDOB': data.get('i_dob'),
            'txtnatureOfBusinessOccupation': data.get('i_occupation'),
            'txtidDocument': data.get('id_doc'),
            'txtdocIdentifierNumber': data.get('ident_num'),
            'txtissuingJurisdiction': data.get('jurisdiction'),
            'txtissuingCountry': data.get('country'),
            'txtdocumentExpiryDated1_mmmm': day_format(expiry_date[-1]),
            'txtdocumentExpiryDated1_d': expiry_date[1],
            'txtdocumentExpiryDated1_yyyy': expiry_date[0],
            'txtcreditBureau1': data.get('credit_bureau1'),
            'txtcreditBureau2': data.get('credit_bureau2'),
            'txtcreditBureauRefNum': data.get('bureau_ref_num'),
            'chkOpt_dualID1': data.get('dual_Id', None),
            'txtsourceName1': data.get('source1_name'),
            'txtBillNumber1': data.get('source1_number'),
            'chkOpt_dualID2': data.get('dual2_id'),
            'txtsourceName2': data.get('source2_name'),
            'txtBillNumber2': data.get('source2_number'),
            'chkOpt_dualID3': data.get('dual3_id'),
            'txtsourceName3': data.get('source3_name'),
            'txtacctType': data.get('acct_type'),
            'txtBillNumber3': data.get('bill_number'),
            'chkOpt_ascertainIdentity': data.get('accertain_ident'),
            'txtascertainIdentityExplain1': data.get('ident_explain1'),
            'txtascertainIdentityExplain2': data.get('ident_explain2'),
            'txtascertainIdentityDated1_mmmm': day_format(iden_date[-1]),
            'txtascertainIdentityDated1_d': iden_date[1],
            'txtascertainIdentityDated1_yyyy': iden_date[0],
            'chkOpt_reasonsMeasuresUnsccessful': data.get('measure_unsuccessful'),
            'txtreasonsMeasuresUnsuccessful1': data.get('measure_unsuccessful1'),
            'txtreasonsMeasuresUnsuccessful2': data.get('measure_unsuccessful2'),
            'chkOpt_transConductedBehalfClient': data.get('trans_conduct'),
            'txtthirdPartyReasonsMeasuresTaken': data.get('part_measure_taken'),
            'txtthirdPartyName': data.get('third_party_name'),
            'txtthirdPartyAddress1': data.get('third_party_addr_1'),
            'txtthirdPartyAddress2': data.get('third_party_addr_2'),
            'txtthirdPartyDOB': data.get('third_party_dob'),
            'txtthirdPartyBusinessOccupation1': data.get('third_party_biz_occu1'),
            'txtthirdPartyBusinessOccupation2': data.get('third_party_biz_occu2'),
            'txtthirdPartyIncorporationNumber1': data.get('third_party_biz_number1'),
            'txtthirdPartyIncorporationNumber2': data.get('third_party_biz_number2'),
            'txtthirdPartyRelationship1': data.get('third_party_biz_relationship1'),
            'txtthirdPartyRelationship2': data.get('third_party_biz_relationship2'),
            'DISCLAIMER': data.get('disclaimer'),
            'chkOpt_lowRisk': data.get('check_low_risk', ),
            'txtlowRiskExplain': data.get('low_risk_explain'),
            'chkOpt_medRisk': data.get('check_medium_risk'),
            'txtmedRiskExplain': data.get('medium_risk_explain'),
            'chkOpt_highRisk': data.get('check_high_risk'),
            'txthighRiskExplain': data.get('high_risk_explain'),
            'chkOpt_D1a': data.get('check_D1a', None),
            'chkOpt_D1b': data.get('check_D1b'),
            'chkOpt_D1c': data.get('check_D1c'),
            'chkOpt_D1d': data.get('check_D1d'),
            'chkOpt_D1e': data.get('check_D1e'),
            'txtD1explain1': data.get('D1e_explain'),
            'txtthirdPartyReasonsMeasuresTaken2': data.get('third_party_reason_meaure2'),
            'txtD2explain1': data.get('D2e_explain1'),
            'txtD2explain2': data.get('D2e_explain2'),
        }
        # fillpdf.fillpdfs.write_fillable_pdf(self.input_file_path, self.output_file_path,content)
        radio_list = [

        ]
        for k, v in content.items():
            if k.startswith('chk') and v is not None:
                radio_list.append(RadioBtnGroup(k, '1'))
        self.writer.add_page(self.reader.getPage(3))
        self.writer.add_page(self.reader.getPage(4))
        self.writer.add_page(self.reader.getPage(5))
        self.writer.add_page(self.reader.getPage(6))
        # set_need_appearances(self.writer, bool_val=True)

        update_page_fields(self.writer.getPage(0), content, *radio_list)
        update_page_fields(self.writer.getPage(1), content, *radio_list)
        update_page_fields(self.writer.getPage(2), content, *radio_list)
        update_page_fields(self.writer.getPage(3), content, *radio_list)

        # self.writer.updatePageFormFieldValues(self.writer.getPage(0), content)
        # self.writer.updatePageFormFieldValues(self.writer.getPage(1), content)
        # self.writer.updatePageFormFieldValues(self.writer.getPage(2), content)
        # self.writer.updatePageFormFieldValues(self.writer.getPage(3), content)

        with open(self.output_file_path, 'wb') as output_stream:
            self.writer.write(output_stream)

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
