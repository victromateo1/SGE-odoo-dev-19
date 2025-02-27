# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Avion(models.Model):
    _name = 'vmn_aerolinea.avion'
    _description = 'Avión'
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    
    name = fields.Char('Avión', required=True)
    description = fields.Char('Descripción')
    litrosCombustible = fields.Float('Litros de combustible')
    destino = fields.Char('Destino')
    imagen = fields.Image(string='Imagen')
    
    pasajero_ids = fields.One2many('vmn_aerolinea.pasajero', 'avion_id', string='Pasajeros')
    azafata_ids = fields.One2many('vmn_aerolinea.azafata', 'avion_id', string='Azafatas')
    maleta_ids = fields.One2many('vmn_aerolinea.maleta', 'avion_id', string='Maletas')

    pasajeros_count = fields.Integer(
        string='Número de Pasajeros', 
        compute='_compute_pasajeros_count', 
        store=True
    )

    @api.depends('pasajero_ids')
    def _compute_pasajeros_count(self):
        for record in self:
            record.pasajeros_count = len(record.pasajero_ids)
