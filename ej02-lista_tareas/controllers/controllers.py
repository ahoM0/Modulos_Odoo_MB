# -*- coding: utf-8 -*-
# from odoo import http


# class Ej02-listaTareas(http.Controller):
#     @http.route('/ej02-lista_tareas/ej02-lista_tareas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ej02-lista_tareas/ej02-lista_tareas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ej02-lista_tareas.listing', {
#             'root': '/ej02-lista_tareas/ej02-lista_tareas',
#             'objects': http.request.env['ej02-lista_tareas.ej02-lista_tareas'].search([]),
#         })

#     @http.route('/ej02-lista_tareas/ej02-lista_tareas/objects/<model("ej02-lista_tareas.ej02-lista_tareas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ej02-lista_tareas.object', {
#             'object': obj
#         })

