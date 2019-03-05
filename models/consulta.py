from odoo import models, fields, api
from . import sapdata
from . import logger



class Consulta(models.Model):
    _name = 'tickets.consulta'
    _description = "Consulta"

    # log = Log()

    modelo = fields.Char(
        string="Modelo",
        required=True
    )

    almacen = fields.Integer(
        string='Almacén'
    )

    articulos = fields.One2many(
        comodel_name='tickets.articulos',
        inverse_name='consulta_id',
        string='Artículos'
    )

    consultar_articulos = fields.Boolean(
        string='Consultar Artículos'
    )

    @api.multi
    @api.onchange('consultar_articulos')
    def onchange_consultar_articulos(self):
        if self.modelo and self.almacen:
            articulos = sapdata.get_articulos(self.modelo, self.almacen)
            log = logger.Log()
            log.logger.info(articulos)
            valores = []
            for item in articulos:
                valores += [
                    (0, 0, {
                        'itemcode2': item['itemcode2'],
                        'onhand': item['onhand'],
                        'descripcion': item['descripcion'],
                        'color': item['color'],
                        'talla': item['talla'],
                        'precio': item['precio'],
                        'modelo': item['modelo']
                    })
                ]
            self.articulos = valores


class Data(models.TransientModel):
    _inherit = 'wizard.print.record.label'
