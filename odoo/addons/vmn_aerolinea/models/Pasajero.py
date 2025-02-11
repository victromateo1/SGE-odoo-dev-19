# -*- coding: utf-8 -*-

from odoo import models, fields

class Maleta(models.Model):
    _name = 'vmn_aerolinea.pasajero'
    _description = 'Pasajero'
    
    name = fields.Char('Pasajero', required=True)
    destino = fields.Char('Destino')
    numAsiento = fields.Char('Numero de asiento')