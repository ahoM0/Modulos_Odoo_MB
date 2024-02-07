# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente del Hospital'

    nombre = fields.Char('Nombre del pacinte', required=True)
    apellidos = fields.Char('Apellidos del paciente')
    sintomas = fields.Text('Síntomas del paciente')

    #  Variable atendido por medicos 
    # un paciente puede ser atendido por varios medicos

    

