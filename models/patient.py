from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self:_('New'))
    age = fields.Integer(string='Age' , tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='Male', tracking=True)
    note = fields.Text(string='Description')
    car = fields.Text(string='Car')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), 
                              ('done', 'Done'), ('cancel', 'Cancelled')], default="draft", string="Status",
                              tracking=True)    
    responsible_id = fields.Many2one('res.partner' , string="Responsible") 

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    @api.model 
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] =  'New Patient'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res
