# -*- coding: utf-8 -*-
# from odoo import http


# class EstudiosPrac04(http.Controller):
#     @http.route('/estudios_prac04/estudios_prac04', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estudios_prac04/estudios_prac04/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estudios_prac04.listing', {
#             'root': '/estudios_prac04/estudios_prac04',
#             'objects': http.request.env['estudios_prac04.estudios_prac04'].search([]),
#         })

#     @http.route('/estudios_prac04/estudios_prac04/objects/<model("estudios_prac04.estudios_prac04"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estudios_prac04.object', {
#             'object': obj
#         })

