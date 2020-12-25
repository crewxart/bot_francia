# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ventas(models.Model):
    _name='ventas'
    Vendedor_id = fields.Many2one('vendedor', string="Vendedor")
    fechaInicio= fields.Date()
    fechaTermino=fields.Date()
