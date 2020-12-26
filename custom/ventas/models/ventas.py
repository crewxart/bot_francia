# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ventas(models.Model):
    _name='ventas'
    fechaInicio= fields.Date(string="Fecha de venta")
    totalparcial=fields.Float(string="Total parcial")
    totalsimpuestos=fields.Float(string="Total sin impuestos")
    impuesto=fields.Float(string="Impuestos")
    ganancia=fields.Float(string="Ganancia")