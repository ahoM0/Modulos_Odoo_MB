# -*- coding: utf-8 -*-
# from odoo import http


# class Ej06-listaTareasCalender(http.Controller):
#     @http.route('/ej06-lista_tareas_calender/ej06-lista_tareas_calender', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ej06-lista_tareas_calender/ej06-lista_tareas_calender/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ej06-lista_tareas_calender.listing', {
#             'root': '/ej06-lista_tareas_calender/ej06-lista_tareas_calender',
#             'objects': http.request.env['ej06-lista_tareas_calender.ej06-lista_tareas_calender'].search([]),
#         })

#     @http.route('/ej06-lista_tareas_calender/ej06-lista_tareas_calender/objects/<model("ej06-lista_tareas_calender.ej06-lista_tareas_calender"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ej06-lista_tareas_calender.object', {
#             'object': obj
#         })

