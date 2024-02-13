# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Paciente(models.Model):
    _name = 'hospital.pacientes'
    _description = 'Paciente del Hospital'
    #
    _rec_name="nombre"
    
    # 
    nombre = fields.Char('Nombre del pacinte', required=True)
    apellidos = fields.Char('Apellidos del paciente')
    sintomas = fields.Text('Síntomas del paciente')

    # 
    diagnosticos_ids = fields.One2many('hospital.diagnosticos', 'pacientes_ids')




