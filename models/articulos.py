from odoo import models, fields, api

class Consulta(models.Model):
    _name = 'tickets.articulos'
    _description = "Articulos"

    itemcode2 = fields.Char(
        string="Item",
        required=True
    )

    onhand = fields.Integer(
        string='OnHand'
    )

    impresion = fields.Integer(
        string='Impresión'
    )

    descripcion = fields.Char(
        string='Descripción'
    )

    color = fields.Char(
        string='Color'
    )

    talla = fields.Char(
        string='Talla'
    )

    precio = fields.Float(
        string='Precio Dolar'
    )

    modelo = fields.Char(
        string='Modelo'
    )

    consulta_id = fields.Many2one(
        comodel_name='tickets.consulta',
        string='Consuta',
        ondelete='cascade'
    )