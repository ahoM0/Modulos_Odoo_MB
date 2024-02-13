# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medico(models.Model):
    _name = 'hospital.medicos'
    _description = 'Medico del hospital'
    _rec_name="nombre"
    
    # Campos del modelo
    num_colegiado = fields.Integer('Número del colegiado', required=True)
    nombre = fields.Char('Nombre del médico', required=True)
    apellidos = fields.Char('Apellidos del médico') 

    # Definimos la relacion de one2many hacia el campo atencion_medicos del modelo diagnosticos.
    atenciones_id = fields.One2many('hospital.diagnosticos', 'atencion_medicos')


    


