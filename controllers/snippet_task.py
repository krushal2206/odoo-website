from odoo import http
from odoo.http import request, Controller, route
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import Response
import json
from odoo.exceptions import UserError, ValidationError


class SnippetTask(http.Controller):

    @http.route('/schools/', auth="public", type="json", methods=['POST'])
    def all_schools(self):
        schools = http.request.env['school.info'].search_read(
            [], ['school_name', 'country_id', 'state_id', 'image'])
        return schools


class SignupLoginPage(http.Controller):
    @http.route('/sign-up', type='http', auth='public', website=True)
    def sign_up(self, **kw):
        return request.render('website_task.signup_template')


class CustomWebpage(http.Controller):
    @http.route('/custom_page', type='http', auth="public", website=True)
    def create_form_data(self, **kw):
        if (request.env.user.id == 4):
            return request.render('website_task.signup_template')
        else:
            request.env['website.task'].sudo().create(kw)
            return request.render('website_task.custom_template')
