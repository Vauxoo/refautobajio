# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_studio_tipo_de_venta = fields.Selection([
        ('Full','Full'),
        ('Drop','Drop'),
        ('Flex','Flex'),
        ('Por definir','Por definir')],
        string="Tipo de venta", default=False, store=True,
    )

    x_studio_url_gua = fields.Char(string="URL Guía",store=True)
    x_studio_mktcode = fields.Char(string="Código de Marketplace",store=True)
    x_studio_status = fields.Char(string="Estado",store=True)
    x_studio_no_guia = fields.Char(string="No Guía",store=True)
    x_studio_fecha_mkt = fields.Date(string="Fecha mkt", store=True)
    x_studio_lineenvcom = fields.One2many('x_lineenvcom','x_studio_orden_de_venta',string="lineenvcom")
    x_studio_analisis_de_margen = fields.Html(string="Análisis de margen", store=True)
    x_studio_reclamos_meli = fields.Many2one('x_reclamos_meli',string="Reclamo Meli",compute="_compute_meli")
    # 1. Campo para el nombre del archivo (CharField)
    x_studio_xml_filename = fields.Char(string='Nombre del Archivo')
    x_studio_xml = fields.Binary(string="XML", filename='x_studio_xml_filename', store=True)
    x_studio_fecha_entrega = fields.Date(string="Fecha de entrega", store=True)
    x_studio_ubicacion_mkt = fields.Char(string="Ubicación Mkt", store=True)
    x_studio_folio_az = fields.Char(string="Folio AZ", store=True)




    @api.depends('name')
    def _compute_meli(self):
        for record in self:
            cuentaaz = self.env['x_reclamos_meli'].search([('x_name','=', record.name)], limit=1)
            if cuentaaz:
                record['x_studio_reclamos_meli'] = cuentaaz.id
            else:
                record['x_studio_reclamos_meli'] = False


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_studio_tipo_de_venta_lineas = fields.Selection(related='order_id.x_studio_tipo_de_venta', string="Tipo de venta Líneas",store=True)
    x_studio_orderid = fields.Char(string="OrderID",store=True)
    x_studio_split_order = fields.Boolean(string="Split Order", store=True)

class Pricelist(models.Model):
    _inherit = 'product.pricelist'

    x_studio_az_sync = fields.Boolean(string='AZ Sync', store=True, default=False)
    x_studio_canales = fields.Many2many('crm.team', string='Canales', store=True)