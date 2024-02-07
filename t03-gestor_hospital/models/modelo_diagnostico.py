# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Listado de Diagnosticos realizados por los médicos'

    name_medico = fields.Char('Nombre del médico')
    name_paciente = fields.Char('Nombre del paciente')

    

