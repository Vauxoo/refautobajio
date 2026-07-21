# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Picking(models.Model):
    _inherit = 'stock.picking'

    x_studio_orden_de_venta = fields.Many2one('sale.order',string="Orden de Venta",store=True,compute="_compute_orden_venta")
    x_studio_actualizar = fields.Boolean(string="Actualizar", store=True)
    x_studio_tipo_de_venta = fields.Selection(related="x_studio_orden_de_venta.x_studio_tipo_de_venta",string="Tipo de Venta",store=True)

    @api.depends('origin','x_studio_actualizar','state','group_id')
    def _compute_orden_venta(self):
        for record in self:
            if record.state == 'cancel':
                record.x_studio_orden_de_venta = False
            else:
                #raise UserError("Aqui")
                registro_encontrado = self.env['sale.order'].search([('name', '=', record.group_id.name)],limit=1)
                if registro_encontrado:
                    record.x_studio_orden_de_venta = registro_encontrado.id