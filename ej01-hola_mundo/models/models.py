# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ej01-hola_mundo(models.Model):
#     _name = 'ej01-hola_mundo.ej01-hola_mundo'
#     _description = 'ej01-hola_mundo.ej01-hola_mundo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

