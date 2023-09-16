from odoo import http
from odoo.http import request, Controller, route
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import Response
import json


class SnippetTask(http.Controller):

    @http.route('/schools/', auth="public", type="json", methods=['POST'])
    def all_schools(self):
        schools = http.request.env['school.info'].search_read(
            [], ['school_name', 'country_id', 'state_id', 'image'])
        return schools


class CustomWebpage(http.Controller):
    @http.route('/custom_page', type='http', auth="public", website=True)
    def create_form_data(self, **kw):
        # Render your custom template
        request.env['website.task'].sudo().create(kw)
        return request.render('website_task.custom_template')
