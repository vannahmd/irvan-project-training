from odoo import models, fields, api


class PartnerXlsx(models.AbstractModel):
    _name = 'report.tesproject.report_barang_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()


    def generate_xlsx_report(self, workbook, data, barang):
        sheet = workbook.add_worksheet('Daftar Barang')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Barang', bold)
        sheet.write(1, 1, 'Harga Modal', bold)
        sheet.write(1, 2, 'Harga Jual', bold)
        sheet.write(1, 3, 'Stok', bold)
        sheet.write(1, 4, 'Kelompok Barang', bold)
        row = 2
        col = 0
        for obj in barang:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, str(obj.harga_beli))
            sheet.write(row, col+2, str(obj.harga_jual))
            sheet.write(row, col+3, str(obj.stok))

            for a in obj.kelompokbarang_id:
                sheet.write(row, col+4, a.name)
                for b in obj.supplier_id:
                    sheet.write(row, col+5, b.name)
                    col += 1
                row += 1
                