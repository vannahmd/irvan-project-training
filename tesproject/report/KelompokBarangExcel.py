from odoo import models, fields, api


class PartnerXlsx(models.AbstractModel):
    _name = 'report.tesproject.report_kelompokbarang_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()


    def generate_xlsx_report(self, workbook, data, kelompokbarang):
        sheet = workbook.add_worksheet('Kelompok Barang')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Kelompok Barang', bold)
        sheet.write(1, 1, 'Kode Kelompok', bold)
        sheet.write(1, 2, 'Kode Rak', bold)
        sheet.write(1, 3, 'Daftar Barang', bold)
        row = 2
        col = 0
        for obj in kelompokbarang:
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, str(obj.kode_kelompok))
            sheet.write(row, col+2, str(obj.kode_rak))
            sheet.write(row, col+3, obj.daftar)
            row += 1

                