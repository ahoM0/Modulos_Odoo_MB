# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class t03-gestor_hospital(models.Model):
#     _name = 't03-gestor_hospital.t03-gestor_hospital'
#     _description = 't03-gestor_hospital.t03-gestor_hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

