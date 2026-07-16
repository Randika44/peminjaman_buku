from odoo import models, fields, api


class Buku(models.Model):
     _name = 'perpustakaan.buku'
     _description = 'Data Buku Perpustakaan'

     judul = fields.Char()
     ISBN = fields.Char()
     stok = fields.Integer()

class Peminjaman(models.Model) :
    _name = 'perpustakaan.peminjaman'
    _description = 'Data Peminjaman Buku'

    buku_id = fields.Many2one ('perpustakaan.buku', string="Buku")
    peminjam = fields.Char()
    tanggal_pinjam = fields.Datetime()
    status = fields.Selection([
        ('dipinjam', 'Dipinjam'),
        ('dikembalikan', 'Dikembalikan'),
    ], default= 'dipinjam')