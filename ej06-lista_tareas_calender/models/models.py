# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ej06-lista_tareas_calender(models.Model):
#     _name = 'ej06-lista_tareas_calender.ej06-lista_tareas_calender'
#     _description = 'ej06-lista_tareas_calender.ej06-lista_tareas_calender'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

