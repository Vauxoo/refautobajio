# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_studio_cdb = fields.Char(string="CDB",store=True)
    x_studio_cdb2 = fields.Char(string="CDB2",store=True)
    x_studio_azaccountid = fields.Char(string='Azaccountid',store=False,compute='_compute_azaccountid')
    x_studio_default_code = fields.Char(string='default_code',store=True,compute='_compute_defaultcode')
    x_studio_stock = fields.Float(string='Stock',store=True)
    x_studio_double_validation = fields.Boolean(string='double_validation',store=True)

    @api.depends('name')
    def _compute_azaccountid(self):
        for record in self:
            cuentaaz = self.env['x_configuraciones_auto'].search([], limit=1)
            if cuentaaz:
                record['x_studio_azaccountid'] = cuentaaz.x_studio_zaccountid
            else:
                record['x_studio_azaccountid'] = False

    @api.depends('name','default_code','x_studio_double_validation')
    def _compute_defaultcode(self):
        for record in self:
            if record.default_code and record.name:
                record['x_studio_default_code'] = record.default_code

    def productos_sincronizar_productos(self):
        """
        Mtodo para sincronizar productos con Autoazur
        """
        # Verifica que la acción exista
        action = self.env.ref('autoazur.productos_sincronizar_productos', raise_if_not_found=False)
        if action:
            # Ejecuta la acción para los registros seleccionados
            return action.with_context(active_ids=self.ids, active_model=self._name).run()
        else:
            # Si no existe la acción, muestra un mensaje
            return {
                'type': 'ir.actions.act_window',
                'name': 'Sincronizar',
                'view_mode': 'form',
                'res_model': 'product.template',
                'res_id': self.id,
                'target': 'current',
            }
    

    