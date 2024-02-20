# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'estudios.alumno'
    _description = 'Alumnos Matriculados del Instituto.'
    
    _rec_name="nombre"

    dni = fields.Char(string="DNI")
    nombre = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")

    modulosMatriculado= fields.Many2many('estudios.modulo', string="Modulos")


