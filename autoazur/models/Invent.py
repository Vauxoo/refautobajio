# -*- coding: utf-8 -*-
from cgitb import strong

from odoo import models, fields, api

class Logsyncinvent(models.Model):
    _name = 'x_logsyncinvent'
    _description='x_logsyncinvent'

    x_studio_sequence = fields.Integer(string="Secuencia",store=True)
    x_name = fields.Char(string="Descripción", store=True)
    x_studio_log = fields.Html(string="Log",store=True)
    x_studio_company_id = fields.Many2one('res.company',string="Empresa",store=True)


class Invubisync(models.Model):
    _name = 'x_invubisync'
    _description = 'x_invubisync'

    x_name = fields.Char(string="Descripción", store=True)
    x_studio_sincronizar_por = fields.Selection([
        ('Almacen', 'Almacen'),
        ('Ubicacion', 'Ubicacion')],
        string="Sincronizar por", default=False, store=True,
    )
    x_studio_almacenes = fields.Many2many('stock.warehouse', string='Almacenes', store=True)
    x_studio_ubicaciones = fields.Many2many('stock.location', string='Ubicaciones', store=True)
    x_studio_almacen = fields.Many2one('stock.warehouse',string="Almacén",store=True)
    x_studio_inventarios = fields.One2many('x_lininvsync','x_studio_inventario_por_ubicacin',string="Inventarios")
    x_studio_company_id = fields.Many2one('res.company',string="Empresa",store=True)
    x_studio_cantidad_minima =  fields.Integer(string='Cantidad Minima')
    x_studio_azaccountid = fields.Char(string='Azaccountid',store=True,compute='_compute_azaccount')
    x_studio_azwarehouseid = fields.Integer(string='Azwarehouseid',related='id')

    @api.depends('x_studio_sincronizar_por')
    def _compute_azaccount(self):
        for record in self:
            cuentaaz = self.env['x_configuraciones_auto'].search([], limit=1)
            if cuentaaz:
                record['x_studio_azaccountid'] = cuentaaz.x_studio_zaccountid
            else:
                record['x_studio_azaccountid'] = False


class lininvsync(models.Model):
    _name = 'x_lininvsync'
    _description = 'x_lininvsync'

    x_name = fields.Char(string="Descripción", store=True)
    x_studio_inventario_por_ubicacin = fields.Many2one('x_invubisync',string="Inventario por ubicación",store=True)
    x_studio_producto = fields.Many2one('product.product',string="Producto",store=True)
    x_studio_sku = fields.Char(related='x_studio_producto.default_code',string="SKU")
    x_studio_cdb = fields.Char(related='x_studio_producto.x_studio_cdb',string="CDB")
    x_studio_cdb2 = fields.Char(related='x_studio_producto.x_studio_cdb2',string="CDB2")
    x_studio_cdigo_de_barras = fields.Char(related='x_studio_producto.barcode',string="Código de barras")
    x_studio_stock = fields.Float(string='Stock',store=True)
    x_studio_company_id = fields.Many2one('res.company',string="Empresa",store=True)
    

