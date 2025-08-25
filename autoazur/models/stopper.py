# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StopperAz(models.Model):
    _name = 'x_stopper_az'
    _description = 'x_stopper_az'

    x_studio_sequence = fields.Integer(string="Secuencia",store=True)
    x_name = fields.Char(string='Descripción', store=True)
    x_studio_segundos = fields.Float(string='Segundos para actualizar',store=True)
    company_id = fields.Many2one('res.company',string="Company ID",store=True, default=lambda self: self.env.company)
    x_studio_sincronizacion_de_inventario = fields.Many2one('x_invubisync', string='Sincronizacion de Inventario', store=True)
    x_studio_sincronizar_por = fields.Selection(related='x_studio_sincronizacion_de_inventario.x_studio_sincronizar_por',string="Sincronizar por")
    x_studio_almacenes = fields.Many2many(related='x_studio_sincronizacion_de_inventario.x_studio_almacenes', string="Almacenes")
    x_studio_ubicaciones = fields.Many2many(related='x_studio_sincronizacion_de_inventario.x_studio_ubicaciones', string="Ubicaciones")
    x_studio_almacen = fields.Many2one('stock.warehouse', string='Almacén',compute='_compute_almacen',store=True)
    x_studio_azaccountid = fields.Char(string='Azaccountid',compute='_compute_azaccountid')
    x_studio_linstopper = fields.One2many('x_linstopper','x_studio_stopper_az',string='linstopper')
    x_studio_cantidad_minima = fields.Integer(related='x_studio_sincronizacion_de_inventario.x_studio_cantidad_minima',string='Cantidad Minima')

    @api.depends('company_id')
    def _compute_azaccountid(self):
        for record in self:
            cuentaaz = self.env['x_configuraciones_auto'].search([], limit=1) 
            if cuentaaz:
                record.x_studio_azaccountid = cuentaaz.x_studio_zaccountid
            else:
                record.x_studio_azaccountid = False


    @api.depends('company_id')
    def _compute_almacen(self):
        for record in self:
            cuentaaz = self.env['x_invubisync'].search([], limit=1) 
            if cuentaaz:
                record.x_studio_almacen = cuentaaz.x_studio_almacen
            else:
                record.x_studio_almacen = False


class LinStopper(models.Model):
    _name = 'x_linstopper'
    _description = 'x_linstopper'

    x_studio_sequence = fields.Integer(string="Secuencia",store=True)
    x_name = fields.Char(related='x_studio_producto.default_code',string='Descripción', store=True)
    company_id = fields.Many2one('res.company',string="Company ID",store=True, default=lambda self: self.env.company)
    x_studio_stopper_az = fields.Many2one('x_stopper_az',string="Stopper AZ",store=True)
    x_studio_producto = fields.Many2one('product.product',string='Producto',store=True)
    x_studio_default_code = fields.Char(related='x_studio_producto.default_code',string='Default Code')
    x_studio_cdb = fields.Char(related='x_studio_producto.x_studio_cdb',string="CDB")
    x_studio_cdb2 = fields.Char(related='x_studio_producto.x_studio_cdb2',string="CDB2")
    x_studio_barcode = fields.Char(related='x_studio_producto.barcode',string='Código de barras')
    x_studio_stock = fields.Float(string='Stock',store=True)
    x_studio_azaccountid = fields.Char(related='x_studio_stopper_az.x_studio_azaccountid',string='Azaccountid')


class HistoricoStopper(models.Model):
    _name = 'x_historico_stopper'
    _description = 'x_historico_stopper'

    name = fields.Char(string="Descripción",store=True)
    x_studio_stopper = fields.Many2one('x_stopper_az',string="Stopper",store=True)
    x_studio_reporte = fields.Html(string="Reporte",store=True,default="Histórico")
    company_id = fields.Many2one('res.company', string="Empresa",store=True)



