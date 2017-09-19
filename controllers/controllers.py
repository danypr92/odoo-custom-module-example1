# -*- coding: utf-8 -*-
from odoo import http

# class Odoo-custom-module-example1(http.Controller):
#     @http.route('/odoo-custom-module-example1/odoo-custom-module-example1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-custom-module-example1/odoo-custom-module-example1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-custom-module-example1.listing', {
#             'root': '/odoo-custom-module-example1/odoo-custom-module-example1',
#             'objects': http.request.env['odoo-custom-module-example1.odoo-custom-module-example1'].search([]),
#         })

#     @http.route('/odoo-custom-module-example1/odoo-custom-module-example1/objects/<model("odoo-custom-module-example1.odoo-custom-module-example1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-custom-module-example1.object', {
#             'object': obj
#         })