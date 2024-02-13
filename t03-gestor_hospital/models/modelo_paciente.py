# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Paciente(models.Model):
    _name = 'hospital.pacientes'
    _description = 'Paciente del Hospital'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo nombre
    _rec_name="nombre"
    
    # Campos del modelo
    nombre = fields.Char('Nombre del pacinte', required=True)
    apellidos = fields.Char('Apellidos del paciente')
    sintomas = fields.Text('Síntomas del paciente')

    # Definimos la relacion de one2many hacia el campo pacientes_ids del modelo diagnosticos.
    diagnosticos_ids = fields.One2many('hospital.diagnosticos', 'pacientes_ids')




