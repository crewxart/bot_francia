# -*- coding: utf-8 -*-
from odoo import models, fields, api

class vendedor(models.Model):
    _name='vendedor'
    name=fields.Char(string="Nombre", required=True)
    apellidos=fields.Char(string="Apellidos", required=True)
    fechaIngreso=fields.Date(string="Fecha de ingreso", required=True)
    #vendedor_ids= fields.One2many('ventas','vendedor_id', string="Ventas del vendedor")