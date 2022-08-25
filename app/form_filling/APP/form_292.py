import os.path
import tempfile
from collections import OrderedDict
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import PyPDF2
import fillpdf.fillpdfs
from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import IndirectObject
from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
import pdfrw
from .process_pdf import ProcessPdf


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


def updateCheckboxValues(page, fields):
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in fields:
            if writer_annot.get('/T') == field:
                writer_annot.update({
                    NameObject("/V"): NameObject(fields[field]),
                    NameObject("/AS"): NameObject(fields[field])
                })


class Form292:

    def __init__(self, form200a_name):
        folder_path = os.path.join(os.getcwd(), 'PDFs')
        file_path = os.path.join(folder_path, form200a_name)
        self.file_name = os.path.basename(file_path).split(".")[0]
        self.output_path = os.path.join(os.path.join(os.getcwd(), 'fiiled_form'), os.path.basename(file_path))

        self.file_path = file_path
        self.writer = PdfWriter()
        # self.reader = PdfReader(self.file_path)

    def read_write_first_page(self, data):
        pdf = pdfrw.PdfReader(self.file_path)
        # page_1 = self.reader.pages[0]
        # fields = self.reader.get_fields()
        # page_2 = self.reader.pages[1]
        for page in pdf.pages:
            annotations = page['/Annots']
            if annotations is None:
                continue

            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    if annotation['/T']:
                        key = annotation['/T'].to_unicode()
                        print(key)
        # self.writer.add_page(page_1)
        # Inspired by updatePageFormFieldValues but also handle checkboxes
        # page = self.writer.pages[0]

        # self.writer.add_page(page_2)
        # list_date = datetime.strptime(data.get('list_date'), "%d/%m/%Y")
        # list_d = day_format(list_date.date().day)
        # list_m = list_date.date().strftime("%B")
        # list_y = list_date.date().strftime("%y")
        # expire_date = datetime.strptime(data.g('list_expire'), "%d/%m/%Y")
        # expire_d = day_format(expire_date.date().day)
        # expire_m = expire_date.date().strftime("%B")
        # expire_y = expire_date.date().strftime("%y")
        #
        # possession_date = datetime.strptime(data.g('possession_date'), "%d/%m/%Y")
        # possession_d = day_format(possession_date.date().day)
        # possession_m = possession_date.date().strftime("%B")
        # possession_y = possession_date.date().strftime("%y")
        # broker_address = data['Broker Address']
        # if broker_address:
        #     address, city, state, zip = broker_address.split(',')
        #     address = address.strip()
        #     city = city.strip()
        #     state = state.strip()
        #     zip = zip.strip()
        # else:
        #     address = city = state = zip = None
        #
        fields_to_file = {
            'txtmlsnumber': data.get('mls_listing_number', ''),
            'txtp_TaxID': data.get('assessment_roll_number', ''),
            'txtParcel_id': data.get('pin_number', ''),
            'hidArea_code': data.get('area', ''),
            'hidCommunity_code': data.get('community', ''),
            'txtp_streetnum': data.get('street_number', ''),
            'txtp_UnitNumber': data.get('apt_unit', ''),
            'txtp_zipcode': data.get('zip_code', ''),
            'txtbldg_name': data.get('building_name', ''),
            'txtProp_mgmt': data.get('property_management', ''),
            'txtCondo_corp': data.get('condo_registry', ''),
            'txtCorp_num': data.get('condo_corp_number', ''),
            'txtStories': data.get('level', ''),
            'txtUnit_num': data.get('unit_number', ''),
            'txtCross_st': data.get('cross_street', ''),
            'txtMmap_page': data.get('map_number', ''),
            'txtMmap_col': data.get('map_col', ''),
            'map_row': data.get('txtMmap_row', ''),
            'txtp_listprice': data.get('list_price', ''),
            # 'txtp_listdate_mm':list_m,
            # 'txtp_listdate_dd':list_d,
            # 'txtp_listdate_yyyy':list_y,
            # 'txtp_expiredate_mm':expire_m,
            # 'txtp_expiredate_dd':expire_d,
            # 'txtp_expiredate_yyyy':expire_y,
            # 'txtp_possessiondate_mm':possession_m,
            # 'txtp_possessiondate_dd':possession_d,
            # 'txtp_possessiondate_yyyy':possession_y,
            'txtOcc': data.get('possession_remarks', ''),
            'txtp_bal1stMortgage': data.get('holdover_days', ''),
            'txtMaint': data.get('maintenance', ''),
            'txtseller': data.get('landlord_name', ''),
            'chkTypeown_CommElementCondo': '',
            'chkTypeown_CondoApt': '',
            'chkOpt_to_buy': 'On',

        }
        fillpdfs.write_fillable_pdf(self.file_path, output_pdf_path=self.output_path, data_dict=fields_to_file, flatten=True)

        #     "txtl_broker": data.get('Broker Name', ''),
        #     "txtl_brkaddr": address,
        #     "txtl_brkcity": city,
        #     "txtl_brkstate": state,
        #     "txtl_brkzipcode": zip,
        #     "txtl_brkphone": data.get('Broker Phone', ''),
        #     "txtseller1": data.get('Seller1 Name', ''),
        #     "hidAndBSAmp": data.get('hidAndBSAmp', ''),
        #     "txtseller2": data.get('Seller2 Name', ''),
        #     "txtp_listdate_d": list_d,
        #     "txtp_listdate_mmmm": list_m,
        #     "txtp_listdate_yy": list_y,
        #     "txtp_expiredate_d": expire_d,
        #     "txtp_expiredate_mmmm": expire_m,
        #     "txtp_expiredate_yy": expire_y,
        #     "txtp_listprice": data.get('Price', ''),
        #     "txtp_listpricewords": data.get('Price Word', ''),
        #     "txtCommissionPer": data.get('Commission %', ''),
        #     "txtCommissionAmt": '' if data.get('Commission %', '') else data.get('Commission Amount', ''),
        #     "txtCoopCommissionPer": data.get('Coop Commission %', ''),
        #     "txtCoopCommissionAmt": '' if data.get('Coop Commission %', '') else data.get(
        #         'Coop Commission Amount', ''),
        #     "txtHoldoverDays": data.get('holdoverday', ''),
        #
        # }
        # self.writer.update_page_form_field_values(page, fields=fields_to_file)
        # with open(self.output_path, 'wb') as output_stream:
        #     self.writer.write(output_stream)

    def read_write_3rd_page(self, data):
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
        output_fodler = os.path.join(os.getcwd(), "../../static/fiiled_form")
        file_path = os.path.join(output_fodler, f"{self.file_name}-{name}.pdf")
        with open(file_path, 'wb') as output_stream:
            self.writer.write(output_stream)
        print("Complete")

    def insert_signature(self):
        page = self.reader.pages[2]
        sig_fodler = os.path.join(os.getcwd(), "../SIGNATURES")
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

    def _getFields(self, obj, tree=None, retval=None, fileobj=None):
        fieldAttributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name',
                           '/TU': 'Alternate Field Name', '/TM': 'Mapping Name', '/Ff': 'Field Flags',
                           '/V': 'Value', '/DV': 'Default Value'}
        if retval is None:
            retval = OrderedDict()
            catalog = obj.trailer["/Root"]
            if "/AcroForm" in catalog:
                tree = catalog["/AcroForm"]
            else:
                return None
        if tree is None:
            return retval

        obj._checkKids(tree, retval, fileobj)
        for attr in fieldAttributes:
            if attr in tree:
                obj._buildField(tree, retval, fileobj, fieldAttributes)
                break

        if "/Fields" in tree:
            fields = tree["/Fields"]
            for f in fields:
                field = f.getObject()
                obj._buildField(field, retval, fileobj, fieldAttributes)

        return retval
