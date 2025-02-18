# -*- coding: utf-8 -*-

from odoo import models, fields

class Avion(models.Model):
    _name = 'vmn_aerolinea.avion'
    _description = 'Avión'
    
    name = fields.Char('Avión', required=True)
    description = fields.Char('Descripción')
    litrosCombustible = fields.Float('Litros de combustible')
    destino = fields.Char('Destino')
    imagen = fields.Image(string='Imagen')
    
    pasajero_ids = fields.One2many('vmn_aerolinea.pasajero', 'avion_id', string='Pasajeros')
    azafata_ids = fields.One2many('vmn_aerolinea.azafata', 'avion_id', string='Azafatas')
    maleta_ids = fields.One2many('vmn_aerolinea.maleta', 'avion_id', string='Maletas')