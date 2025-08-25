# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConfiguracionesAuto(models.Model):
    _name = 'x_configuraciones_auto'
    _description='x_configuraciones_auto'
    x_name = fields.Char(string="Descripción", store=True)
    x_studio_sales_team = fields.Many2many('crm.team',string='Sales Team',store=True)
    x_studio_almacn_drop = fields.Many2one('stock.warehouse',string="Almacén Drop", store=True)
    x_studio_id_drop = fields.Integer(related='x_studio_almacn_drop.id', string="ID DROP",store=True)
    x_studio_almacn_full = fields.Many2one('stock.warehouse',string="Almacén Full", store=True)
    x_studio_id_full = fields.Integer(related='x_studio_almacn_full.id', string="ID FULL",store=True)
    x_studio_company_id = fields.Many2one('res.company',string="Empresa",store=True) #Coment
    x_studio_zaccountid = fields.Char(string='ID Cuenta de Autoazur', store=True)

class LogsAutoazur(models.Model):
    _name = 'x_logs_autoazur'
    _description = 'x_logs_autoazur'

    x_studio_sequence = fields.Integer(string="Secuencia",store=True)
    x_name = fields.Char(string="Descripción", store=True)
    x_studio_log = fields.Html(string="Log",store=True)
    x_studio_actualizar = fields.Boolean(string="Actualizar", store=True)
    x_studio_cdigo = fields.Char(string="Código",store=True,compute='_compute_codigo')
    x_studio_canal = fields.Many2one('crm.team',string="Canal",store=True,compute='_compute_canal')
    x_studio_company_id = fields.Many2one('res.company',string="Empresa",store=True)



    @api.depends('x_name','x_studio_log','x_studio_actualizar')
    def _compute_codigo(self):
        for record in self:
            if record.x_name:
                record.x_studio_cdigo = record.x_name.split()[0]


    @api.depends('x_studio_cdigo','x_studio_actualizar')
    def _compute_canal(self):
        for record in self:
            if record.x_studio_cdigo:
                canal = self.env['crm.team'].search([('x_studio_cdigo', '=', record.x_studio_cdigo)])
                if canal:
                    record['x_studio_canal'] = canal[0].id

    

class Historico(models.Model):
    _name = 'x_historico'
    _description = 'x_historico'

    name = fields.Char(string="Descripción",store=True)
    x_studio_ubicacin = fields.Many2one('x_invubisync',string="Ubicación",store=True)
    x_studio_reporte = fields.Html(string="Reporte",store=True,default="Histórico")
    company_id = fields.Many2one('res.company', string="Empresa",store=True)

class BuscadorSync(models.Model):
    _name = 'x_buscador_sync'
    _description = 'x_buscador_sync'

    x_name = fields.Char(string="Descripción",store=True)
    x_studio_keyword = fields.Char(string='Keyword', store=True)
    x_studio_reporte = fields.Html(string="Reporte",store=True,default="Buscador Sync")
    company_id = fields.Many2one('res.company', string="Empresa",store=True)

