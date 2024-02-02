# -*- coding: utf-8 -*-
# from odoo import http


# class Ej01-holaMundo(http.Controller):
#     @http.route('/ej01-hola_mundo/ej01-hola_mundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ej01-hola_mundo/ej01-hola_mundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ej01-hola_mundo.listing', {
#             'root': '/ej01-hola_mundo/ej01-hola_mundo',
#             'objects': http.request.env['ej01-hola_mundo.ej01-hola_mundo'].search([]),
#         })

#     @http.route('/ej01-hola_mundo/ej01-hola_mundo/objects/<model("ej01-hola_mundo.ej01-hola_mundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ej01-hola_mundo.object', {
#             'object': obj
#         })

