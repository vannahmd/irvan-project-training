from odoo import models, fields, api
from datetime import timedelta

class PartnerXlsx(models.AbstractModel):
    _name = 'report.tesproject.report_pengajuan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()


    def generate_xlsx_report(self, workbook, data, pengajuan):
        sheet = workbook.add_worksheet('Daftar Teknisi')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Tanggal Pengajuan', bold)
        sheet.write(1, 1, 'Kode Pengajuan', bold)
        sheet.write(1, 2, 'Nama Pelanggan', bold)
        sheet.write(1, 3, 'No Telepon', bold)
        sheet.write(1, 4, 'Nama Barang', bold)
        sheet.write(1, 5, 'Keluhan', bold)
        row = 2
        col = 0
        for obj in pengajuan:
            col = 0
            sheet.write(row, col, (obj.tgl_pengser + timedelta(hours=7)).strftime("%d/%m/%Y, %H:%M:%S"))
            sheet.write(row, col+1, str(obj.kode_pengser))
            sheet.write(row, col+2, obj.name)
            sheet.write(row, col+3, str(obj.no_telp))
            sheet.write(row, col+4, obj.barang)
            sheet.write(row, col+5, obj.keluhan)
            row += 1
                