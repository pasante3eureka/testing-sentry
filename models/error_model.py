from odoo import models, fields

class ErrorModel(models.Model):
    _name = 'error.model'
    _description = 'Modelo con error en vista'

    name = fields.Char(string='Nombre', required=True)
    value = fields.Integer(string='Valor')