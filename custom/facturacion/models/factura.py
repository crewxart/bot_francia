# -*- coding: utf-8 -*-

from odoo import models, fields, api
class factura(models.Model):
    _name='factura'
    EmpresaMandante=fields.Char(string="Empresa")
    name=fields.Char()
    DireccionFactura=fields.Char()
    DireccionEntrega=fields.Char()
    Rut=fields.Integer() ##Validar datos.
    Comuna=fields.Char()
    Planilla=fields.Char()
    Local=fields.Char()
    nFactura=fields.Integer()
    LugarEmision=fields.Char()


    factura_ids= fields.One2many('detalle', 'factura_id', string="Productos")

    
      

class detalle(models.Model):
    _name='detalle'
    factura_id = fields.Many2one('factura', string="Factura")


    productos_id = fields.Many2one('producto', string="productos")
    cantidad= fields.Float()  