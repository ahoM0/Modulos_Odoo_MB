# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medico(models.Model):
    _name = 'hospital.medicos'
    _description = 'Medico del hospital'
    _rec_name="nombre"
    
    # 
    num_colegiado = fields.Integer('Número del colegiado', required=True)
    nombre = fields.Char('Nombre del médico', required=True)
    apellidos = fields.Char('Apellidos del médico') 

    # 
    atenciones_id = fields.One2many('hospital.diagnosticos', 'atencion_medicos')


    


