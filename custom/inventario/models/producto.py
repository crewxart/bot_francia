# -*- coding: utf-8 -*-

from odoo import models, fields, api

class categoria(models.Model):
    _name = 'categoria'
    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Char(string="Descripcion")

    categoria_ids = fields.One2many(
        'producto',
        'categoria_id',
        string="Productos asociados"
    )

class producto(models.Model):
    _name = 'producto'
    name = fields.Char()
    descripcion = fields.Char()
    costoNeto = fields.Float()
    precioVenta = fields.Float()
    productos_ids = fields.One2many('detalle', 'productos_id')
    stock=fields.Float(readonly=True)
    precioVenta=fields.Float()
    productov_id=fields.One2many('ventasdetalle','productov_ids')
    _sql_constraints = [('name', 'unique(name)', 'Este producto ya existe')
                    ]
    
    
    categoria_id = fields.Many2one(
        'categoria',
        string="Categoría"
    )