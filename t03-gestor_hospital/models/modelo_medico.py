# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Medico del hospital'

    name = fields.Char('Nombre del médico', required=True)
    apellidos = fields.Char('Apellidos del médico') 
    num_colegiado = fields.Integer('Número del colegiado', required=True)

    #  Variable atendio a pacientes 
    # un medico puede atender varios pacientes

    


