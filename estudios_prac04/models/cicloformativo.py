from odoo import models, fields, api

class CicloFormativo(models.Model):
    _name = 'estudios.cicloformativo'
    _description = 'Ciclos formatios del instituto.'

    _rec_name="nombre"

    nombre = fields.Char(string="Nombre")
    
    modulosAsociados = fields.One2many('estudios.modulo', inverse_name='cicloFormativo', string="Modulos")

