from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import date
import re
class patient(models.Model):
    _name="hms.patient"
    First_name = fields.Char(required=True)
    Last_name = fields.Char(required=True)
    Birth_date = fields.Date()
    History = fields.Html()
    CR_Ratio = fields.Float()
    Blood_Type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    PCR = fields.Selection([('pos', 'Positive'),('neg', 'Negative')], string='PCR Test Result')
    Image = fields.Binary()
    Address = fields.Text()
    Age = fields.Integer(compute='compute_age', store=True)
    dep_id = fields.Many2one(comodel_name='hms.department')
    dep_capacity = fields.Integer(related='dep_id.Capacity')
    doctor_ids = fields.Many2many(comodel_name='hms.doctor')

    # lab 3
    log = fields.One2many('hms.log','patient_id','Log')
    # state = fields.Selection([
    #         ('u', 'Undetermined'),
    #         ('g', 'Good'),
    #         ('f', 'Fair'),
    #         ('s', 'Serious'),
    #     ], default='u')
    # def next_state(self):
    #     if self.state == 'u':
    #         self.state = 'g'
    #         self.changeState('Good')
    #     elif self.state == 'g':
    #         self.state = 'f'
    #         self.changeState('Fair')
    #     elif self.state == 'f':
    #         self.state = 's'
    #         self.changeState('Serious')
    #     elif self.state == 's':
    #         self.state = 'u'
    #         self.changeState('Undetermined')
            
    # def changeState(self,state):
    #     self.env['hms.log'].create({
    #         'details': "Patient State Changed To " + state,
    #         'patient_id': self.id
    #     })

    email = fields.Char(required=True, unique=True)
    @api.onchange('email')
    def _check_email(self):
        for record in self:
            if record.email and not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                raise models.ValidationError('Invalid email address: %s' % record.email)
    @api.depends('Birth_date')
    def compute_age(self):
        for record in self:
            if record.Birth_date:
                today = date.today()
                record.Age = today.year - record.Birth_date.year - ((today.month, today.day) < (record.Birth_date.month, record.Birth_date.day))
            else:
                record.Age = 0
    