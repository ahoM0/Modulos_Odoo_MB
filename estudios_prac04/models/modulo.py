
from odoo import models, fields, api

class Modulo(models.Model):
    _name = 'estudios.modulo'
    _description = 'Modulos del Instituto'

    _rec_name="nombre"

    nombre = fields.Char(string="Nombre")
    
    cicloFormativo = fields.Many2one('estudios.cicloformativo', string="Ciclo")

    alumnosMatriculados = fields.Many2many('estudios.alumno', string="Alumnos")

    profesorImparte = fields.Many2one('estudios.profesor', string="Profesor")
