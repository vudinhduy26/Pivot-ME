# -*- coding: utf-8 -*-
# from odoo import http


# class ReportSales(http.Controller):
#     @http.route('/report_sales/report_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_sales/report_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_sales.listing', {
#             'root': '/report_sales/report_sales',
#             'objects': http.request.env['report_sales.report_sales'].search([]),
#         })

#     @http.route('/report_sales/report_sales/objects/<model("report_sales.report_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_sales.object', {
#             'object': obj
#         })
