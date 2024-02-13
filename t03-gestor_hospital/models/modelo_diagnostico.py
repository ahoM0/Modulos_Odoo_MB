# -*- coding: utf-8 -*-

from odoo import models, fields


class Diagnostico(models.Model):
    _name = 'hospital.diagnosticos'
    _description = 'Listado de Diagnosticos realizados por los médicos'
    _rec_name="num_diagnostico"

    # 
    num_diagnostico = fields.Integer('Número del diagnostico.')

    # 
    atencion_medicos = fields.Many2one('hospital.medicos')
    pacientes_ids = fields.Many2one('hospital.pacientes')
 



  
    

