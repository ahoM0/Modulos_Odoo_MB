# -*- coding: utf-8 -*-
# from odoo import http


# class T03-gestorHospital(http.Controller):
#     @http.route('/t03-gestor_hospital/t03-gestor_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/t03-gestor_hospital/t03-gestor_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('t03-gestor_hospital.listing', {
#             'root': '/t03-gestor_hospital/t03-gestor_hospital',
#             'objects': http.request.env['t03-gestor_hospital.t03-gestor_hospital'].search([]),
#         })

#     @http.route('/t03-gestor_hospital/t03-gestor_hospital/objects/<model("t03-gestor_hospital.t03-gestor_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('t03-gestor_hospital.object', {
#             'object': obj
#         })

