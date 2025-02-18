# -*- coding: utf-8 -*-

from odoo import models, fields

class Maleta(models.Model):
    _name = 'vmn_aerolinea.maleta'
    _description = 'Maleta'
    
    name = fields.Char('Maleta', required=True)
    peso = fields.Integer('Peso')
    destino = fields.Char('Destino')
    cabina = fields.Boolean('Maleta de cabina')
    
    pasajero_id = fields.Many2one('vmn_aerolinea.pasajero', string='Pasajero')
    avion_id = fields.Many2one('vmn_aerolinea.avion', string='Avion')