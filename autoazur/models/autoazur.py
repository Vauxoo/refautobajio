# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConfiguracionesAuto(models.Model):
    _name = 'x_configuraciones_auto'
    _description = 'x_configuraciones_auto'
    x_name = fields.Char(string="Descripción", store=True)
    x_studio_sales_team = fields.Many2many('crm.team', string='Sales Team', store=True)

    x_studio_company_id = fields.Many2one('res.company', string="Empresa", store=True)  # Coment
    x_studio_zaccountid = fields.Char(string='ID Cuenta de Autoazur', store=True)


class LogsAutoazur(models.Model):
    _name = 'x_logs_autoazur'
    _description = 'x_logs_autoazur'

    x_studio_sequence = fields.Integer(string="Secuencia", store=True)
    x_name = fields.Char(string="Descripción", store=True)
    x_studio_log = fields.Html(string="Log", store=True)
    x_studio_actualizar = fields.Boolean(string="Actualizar", store=True)
    x_studio_cdigo = fields.Char(string="Código", store=True)
    x_studio_status = fields.Char(string="Status", store=True)
    x_studio_codigo_log = fields.Char(string="Código Log", store=True)
    x_studio_canal = fields.Many2one('crm.team', string="Canal", store=True, compute='_compute_canal')
    x_studio_company_id = fields.Many2one('res.company', string="Empresa", store=True)

    @api.depends('x_studio_cdigo', 'x_studio_actualizar')
    def _compute_canal(self):
        for record in self:
            if record.x_studio_cdigo:
                canal = self.env['crm.team'].search([('x_studio_cdigo', '=', record.x_studio_cdigo)])
                if canal:
                    record['x_studio_canal'] = canal[0].id


class Historico(models.Model):
    _name = 'x_historico'
    _description = 'x_historico'

    name = fields.Char(string="Descripción", store=True)
    x_studio_ubicacin = fields.Many2one('x_invubisync', string="Ubicación", store=True)
    x_studio_reporte = fields.Html(string="Reporte", store=True, default="Histórico")
    company_id = fields.Many2one('res.company', string="Empresa", store=True)


class BuscadorSync(models.Model):
    _name = 'x_buscador_sync'
    _description = 'x_buscador_sync'

    x_name = fields.Char(string="Descripción", store=True)
    x_studio_keyword = fields.Char(string='Keyword', store=True)
    x_studio_reporte = fields.Html(string="Reporte", store=True, default="Buscador Sync")
    company_id = fields.Many2one('res.company', string="Empresa", store=True)


class RepUtilidad(models.Model):
    _name = 'x_rep_utilidad'
    _description = 'x_rep_utilidad'

    x_name = fields.Char(string="Descripción", store=True)
    x_studio_fecha_inicio = fields.Date(string="Fecha Inicio", store=True)
    x_studio_fecha_final = fields.Date(string="Fecha Final", store=True)
    x_studio_canales = fields.Many2many('crm.team', string='Canales', store=True)
    x_studio_mostrar_detalle = fields.Boolean(string="Mostrar Detalle", store=True, default=False)
    x_studio_reporte = fields.Html(string="Reporte", store=True, default="Reporte de Utilidad")
    company_id = fields.Many2one('res.company', string="Empresa", store=True)


class AZPrices(models.Model):
    _name = 'x_az_prices'
    _description = 'x_az_prices'

    x_name = fields.Char(related='x_studio_producto.default_code', string="Descripción", store=True)
    x_studio_producto = fields.Many2one('product.product', string='Producto', store=True)
    x_studio_cdb = fields.Char(related='x_studio_producto.x_studio_cdb', string="CDB")
    x_studio_cdb2 = fields.Char(related='x_studio_producto.x_studio_cdb2', string="CDB2")
    x_studio_barcode = fields.Char(related='x_studio_producto.barcode', string='Código de barras')
    x_studio_precio = fields.Float(string='Precio', store=True)
    x_studio_canal = fields.Many2one('crm.team', string='Canal', store=True)
    x_studio_id_az = fields.Char(related='x_studio_canal.x_studio_id_az', string='ID AZ')
    x_studio_pricelist = fields.Many2one('product.pricelist', string='Pricelist', store=True)
    x_studio_az_sync = fields.Boolean(related='x_studio_pricelist.x_studio_az_sync', string='AZ Sync', store=True,
                                      default=False)
    x_studio_id_cliente_az = fields.Char(string='ID Cliente AZ', store=True, compute='_compute_codigo')
    company_id = fields.Many2one('res.company', string="Empresa", store=True)

    @api.depends('x_studio_producto')
    def _compute_codigo(self):
        for record in self:
            cuentaaz = self.env['x_configuraciones_auto'].search([], limit=1)
            if cuentaaz:
                record.x_studio_id_cliente_az = cuentaaz.x_studio_zaccountid
            else:
                record.x_studio_id_cliente_az = False
