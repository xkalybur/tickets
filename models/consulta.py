from odoo import models, fields, api
from . import sapdata
from . import logger



class Consulta(models.Model):
    _name = 'tickets.consulta'
    _description = "Consulta"

    log = logger.Log()

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

    printer_id = fields.Many2one(
        comodel_name='printing.printer', string='Printer', required=True,
        help='Printer used to print the labels.')

    label_id = fields.Many2one(
        comodel_name='printing.label.zpl2', string='Label', required=True,
        # domain=lambda self: [
        #     ('model_id.model', '=', self.env.context.get('active_model'))],
        help='Label to print.')

    @api.multi
    @api.onchange('consultar_articulos')
    def onchange_consultar_articulos(self):
        if self.modelo and self.almacen:
            articulos = sapdata.get_articulos(self.modelo, self.almacen)
            self.log.logger.info(articulos)
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

    @api.multi
    def imprimir_ticket(self):
        self.env['printing.label.zpl2'].browse(self.label_id.id).print_label(
            self.env['printing.printer'].browse(self.printer_id.id),
            self.env['tickets.consulta'].browse(self.id)
        )
        self.log.logger.info(self.env['printing.label.zpl2'].browse(self.label_id))
        self.log.logger.info(self.env['printing.printer'].browse(self.printer_id))
        self.log.logger.info(self.env['tickets.consulta'].browse(self.id))
        return


class Data(models.TransientModel):
    _inherit = 'wizard.print.record.label'
