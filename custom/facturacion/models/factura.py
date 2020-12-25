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


    ########## GENERAL
    ## Obtener costo neto de producto seleccionado.
    @api.onchange('productos_id')
    def _onchange(self):
        self.precioNeto= self.productos_id.costoNeto
    

    precioNeto=fields.Float()
    ###################


    ##Calcular subtotal al modificar cantidad o descuento
    cantidad= fields.Float()
    descuento = fields.Float(string="Descuento %")

    iva=fields.Float(string="IVA")


    @api.onchange('cantidad','descuento')
    def _compute_subtotal(self):
        if (self.descuento>0):
            self.iva= (self.cantidad*self.precioNeto)*0.19
            self.subtotal = ((self.cantidad*self.precioNeto)-(self.cantidad * self.precioNeto)*self.descuento/100)+self.iva
        else:
            self.iva= (self.cantidad*self.precioNeto)*0.19
            self.subtotal = (self.cantidad * self.precioNeto)+self.iva

    subtotal=fields.Float()
    ## Impuesto
