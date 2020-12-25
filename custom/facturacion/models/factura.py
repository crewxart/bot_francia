# -*- coding: utf-8 -*-

from odoo import models, fields, api
class factura(models.Model):
    _name='factura'
    EmpresaMandante=fields.Char(string="Empresa")
    name=fields.Char(string="Nombre")
    DireccionFactura=fields.Char(string="Dirección factura")
    DireccionEntrega=fields.Char(string="Dirección entrega")
    Rut=fields.Integer(string="Rut") ##Validar datos.
    Comuna=fields.Char(string="Comuna")
    Planilla=fields.Char(string="Planilla")
    Local=fields.Char(string="Local")
    nFactura=fields.Integer(string="Número de factura")
    LugarEmision=fields.Char(string="Lugar de emisión")
    fecha=fields.Date(string="Fecha emisión ")
    estado=fields.Selection([('Pagada','Pagada'),('Pendiente','Pendiente'),('Devolución','Devolución')])

    factura_ids= fields.One2many('detalle', 'factura_id', string="Detalle")
    
      

class detalle(models.Model):
    _name='detalle'
    factura_id = fields.Many2one('factura', string="Factura")
    productos_id = fields.Many2one('producto', string="Producto")


    ########## GENERAL
    ## Obtener costo neto de producto seleccionado.
    @api.onchange('productos_id')
    def _onchange(self):
        self.precioNeto= self.productos_id.costoNeto
    
    precioNeto=fields.Float(string="Precio bruto")
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
