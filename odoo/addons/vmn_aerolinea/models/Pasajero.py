# -*- coding: utf-8 -*-

from odoo import models, fields

class Pasajero(models.Model):
    _name = 'vmn_aerolinea.pasajero'
    _description = 'Pasajero'
    
    name = fields.Char('Pasajero', required=True)
    destino = fields.Char('Destino')
    numAsiento = fields.Char('Numero de asiento')
    
    avion_id = fields.Many2one('vmn_aerolinea.avion', string='Avion')
    maleta_ids = fields.One2many('vmn_aerolinea.maleta', 'pasajero_id', string='Maletas')
    azafata_ids = fields.Many2many('vmn_aerolinea.azafata', relation='vmn_aerolinea_azafata_pasajero_rel', string='Azafato/as')