
from odoo import models, fields, api, _


class ExampleModel(models.Model):
    _name = 'example_module.example_model'
    _description = 'It is an example model for creating example data'
    _order = 'create_date'


    example_boolean = fields.Boolean('Example Boolean', default=False)
    name = fields.Char('Example Char')
    example_date = fields.Date('Example Date')
    example_float = fields.Float('Example Float', default=0.0)
    example_html = fields.Html('Example Html')
