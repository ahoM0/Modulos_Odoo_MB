
from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'estudios.profesor'
    _description = 'Profesores del instituto.'

    _rec_name="nombre"

    dni = fields.Char(string="DNI")
    nombre = fields.Char(string="Nombre")
    apellidos  = fields.Char(string="Apellidos")

    modulosImparte = fields.One2many('estudios.modulo',inverse_name='profesorImparte', string="Modulos")