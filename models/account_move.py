# -*- coding: utf-8 -*-
from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_batch_draft(self):
        for move in self:
            if move.state == 'posted':
                move.button_draft()

    def action_batch_cancel(self):
        for move in self:
            if move.state in ('draft', 'posted'):
                try:
                    move.button_draft()
                except Exception:
                    pass
                move.button_cancel()