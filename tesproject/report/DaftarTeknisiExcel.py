from odoo import models, fields, api


class PartnerXlsx(models.AbstractModel):
    _name = 'report.tesproject.report_teknisi_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()


    def generate_xlsx_report(self, workbook, data, barang):
        sheet = workbook.add_worksheet('Daftar Teknisi')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'ID Teknisi', bold)
        sheet.write(1, 1, 'Nama', bold)
        sheet.write(1, 2, 'Alamat', bold)
        sheet.write(1, 3, 'Tanggal Lahir', bold)
        row = 2
        col = 0
        for obj in barang:
            col = 0
            sheet.write(row, col, str(obj.id_teknisi))
            sheet.write(row, col+1, obj.name)
            sheet.write(row, col+2, obj.alamat)
            sheet.write(row, col+3, str(obj.tgl_lahir))
            row += 1
                