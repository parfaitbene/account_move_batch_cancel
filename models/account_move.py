# -*- coding: utf-8 -*-
from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_batch_draft(self):
        if not self:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Attention',
                    'message': 'Aucun enregistrement sélectionné',
                    'sticky': False,
                },
            }

        drafted = 0
        for move in self:
            if move.state == 'posted':
                move.button_draft()
                drafted += 1

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Succès',
                'message': f'{drafted} enregistrement(s) modifié(s)',
                'sticky': False,
            },
        }

    def action_batch_cancel(self):
        if not self:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Attention',
                    'message': 'Aucun enregistrement sélectionné',
                    'sticky': False,
                },
            }

        cancelled = 0
        for move in self:
            if move.state in ('draft', 'posted'):
                try:
                    move.button_draft()
                except Exception:
                    pass
                move.button_cancel()
                cancelled += 1

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Succès',
                'message': f'{cancelled} enregistrement(s) annulé(s)',
                'sticky': False,
            },
        }