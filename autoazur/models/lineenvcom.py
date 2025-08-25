# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Lineenvcom(models.Model):
    _name = 'x_lineenvcom'
    _description = 'x_lineenvcom'
    
    x_name = fields.Char(string="Descripción",store=True,default="lineenvcom")
    x_studio_orden_de_venta = fields.Many2one('sale.order',string="Orden de Venta",store=True)
    x_studio_producto = fields.Many2one('product.product',string="Producto",store=True)
    x_studio_cantidad = fields.Float(string="Cantidad",store=True)
    x_studio_precio_unitario = fields.Float(string="Precio Unitario",store=True)
    x_studio_subtotal = fields.Float(string="Subtotal",store=True,compute='_compute_subtotal')
    x_studio_company_id = fields.Many2one('res.company',string="Empresa",store=True)

    @api.depends('x_studio_cantidad','x_studio_precio_unitario','x_studio_producto')
    def _compute_subtotal(self):
        for record in self:
            if record.x_studio_cantidad:
                record.x_studio_subtotal = record.x_studio_cantidad * record.x_studio_precio_unitario