from odoo import models, fields

class department(models.Model):
    _name="hms.department"
    Name = fields.Char(required=True)
    Capacity = fields.Integer(required=True)
    isOpened = fields.Boolean(default=False)
    patient_id = fields.One2many(comodel_name='hms.patient', inverse_name='dep_id')