# -*- coding: utf-8 -*-

from odoo import models, fields

class Avion(models.Model):
    _name = 'vmn_aerolinea.azafata'
    _description = 'Azafata'
    
    name = fields.Char('Azafata', required=True)
    puesto = fields.Selection([
        ('0', 'Bebida'),
        ('1', 'Cocina'),
        ('2', 'Seguridad'),
    ], string='Puesto', default='0')