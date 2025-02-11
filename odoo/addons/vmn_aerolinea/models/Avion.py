# -*- coding: utf-8 -*-

from odoo import models, fields

class Avion(models.Model):
    _name = 'vmn_aerolinea.avion'
    _description = 'Avión'
    
    name = fields.Char('Avión', required=True)
    description = fields.Char('Descripción')
    litrosCombustible = fields.Float('Litros de combustible')
    destino = fields.Char('Destino')