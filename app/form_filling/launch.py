from APP.app_instructions import AppInstructions

app = AppInstructions('Appt_Instructions_editable.pdf')
form_fields = app.read_write_first_page({})
# pro = ProcessPdf("","")
# gs = GoogleSheetItemExporter('1fwM2E-OSGnvsHpoIFIO_01CSyAiJEc7EDSmDClH4QGw') # Google sheet Key
#
#
# def start_process():
#     form200_sheet_data = gs.get_record('Applicable Instructions')
#     for data in form200_sheet_data:
#         app.read_write_first_page(data)
# pdf_writer = ('(Toronto) 200a - Listing Agreement Authority to Offer for Sale.pdf')  # Form200a PDF file name
# result_file_suffix=data.get('Seller1 Name') # suffix to result file after processing
# pdf_writer.read_write_first_page(data)
# pdf_writer.read_write_3rd_page(data)
# pdf_writer.save_file(result_file_suffix)


# if __name__ == '__main__':
#     start_process()
