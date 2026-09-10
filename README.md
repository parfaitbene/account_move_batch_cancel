# Account Move Batch Cancel

Batch draft and cancel journal entries (`account.move`) directly from the
list view, instead of opening each record one by one.

## Features

- **Revenir à l'état brouillon** — reset selected posted or cancelled
  entries back to draft in one action.
- **Annuler les écritures** — cancel selected draft or posted entries in
  one action.
- Notification summarizing how many records were processed.

## Usage

1. Go to **Accounting > Journal Entries**.
2. Select one or more entries in the list view.
3. Open the **Actions** menu (gear icon) and pick either:
   - *Revenir à l'état brouillon*
   - *Annuler les écritures*

## Access rights

Actions are available to users in the **Accounting / Invoicing: Manager**
group (`account.group_account_manager`).

## Compatibility

Odoo 18.0 — Community & Enterprise.

## Author

[Parfait BENE](https://parfaitbene.com/) — contact@parfaitbene.com

## License

LGPL-3
