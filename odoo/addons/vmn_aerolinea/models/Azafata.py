# -*- coding: utf-8 -*-

from odoo import models, fields

class Azafata(models.Model):
    _name = 'vmn_aerolinea.azafata'
    _description = 'Azafata'
    
    name = fields.Char('Azafata', required=True)
    puesto = fields.Selection([
        ('0', 'Bebida'),
        ('1', 'Comida'),
        ('2', 'Seguridad'),
        ('3', 'Información')
    ], string='Puesto', default='0')
    
    avion_id = fields.Many2one('vmn_aerolinea.avion', string='Avion')
    pasajero_ids = fields.Many2many('vmn_aerolinea.pasajero', string='Pasajero/as', relation='vmn_aerolinea_azafata_pasajero_rel')