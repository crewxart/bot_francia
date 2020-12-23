# -*- coding: utf-8 -*-

from odoo import models, fields, api
class detalle(models.Model):
    _name='detalle'
    factura_id = fields.Many2one('factura', string="Factura")
    productos_id = fields.Many2one('producto', string="Productos")
    cantidad= fields.Float()
