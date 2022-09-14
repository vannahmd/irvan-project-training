# -*- coding: utf-8 -*-
# from odoo import http


# class Tesproject(http.Controller):
#     @http.route('/tesproject/tesproject', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tesproject/tesproject/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tesproject.listing', {
#             'root': '/tesproject/tesproject',
#             'objects': http.request.env['tesproject.tesproject'].search([]),
#         })

#     @http.route('/tesproject/tesproject/objects/<model("tesproject.tesproject"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tesproject.object', {
#             'object': obj
#         })
