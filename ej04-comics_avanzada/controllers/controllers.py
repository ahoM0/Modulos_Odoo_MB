# -*- coding: utf-8 -*-
# from odoo import http


# class Ej04-comicsAvanzada(http.Controller):
#     @http.route('/ej04-comics_avanzada/ej04-comics_avanzada', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ej04-comics_avanzada/ej04-comics_avanzada/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ej04-comics_avanzada.listing', {
#             'root': '/ej04-comics_avanzada/ej04-comics_avanzada',
#             'objects': http.request.env['ej04-comics_avanzada.ej04-comics_avanzada'].search([]),
#         })

#     @http.route('/ej04-comics_avanzada/ej04-comics_avanzada/objects/<model("ej04-comics_avanzada.ej04-comics_avanzada"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ej04-comics_avanzada.object', {
#             'object': obj
#         })

