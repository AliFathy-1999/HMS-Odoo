from odoo import models, fields

class doctor(models.Model):
    _name="hms.doctor"
    First_name = fields.Char(required=True)
    Last_name = fields.Char(required=True)
    Image = fields.Binary(required=True)
    patient_ids = fields.Many2many(comodel_name='hms.patient')