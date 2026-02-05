# User Roles

Asset Management uses role-based access to provide each user with the views and capabilities relevant to their job function.

## Role Overview

| Role | Home View | View Only? | Description |
|------|-----------|------------|-------------|
| [Inventory Manager](inventory-manager.md) | Inventory Management | No | Manages bit inventory, transfers, and stock |
| [Field Sales](field-sales.md) | My Bits | No | Handles field operations, deliveries, and billing |
| [Billing](billing.md) | eBilling Workbench | No | Processes service receipts and invoicing |
| [Rep Manager](rep-manager.md) | Add/Edit Customer Rep | No | Manages customer representative records |
| [Viewer](viewer.md) | Find Bits (Lite) | Yes | Read-only access to bit information |
| [Account Rep](account-rep.md) | eBilling Workbench | Yes | Views billing information for assigned accounts |
| [Finance](finance.md) | eBilling Workbench | Yes | Reviews financial data and reports |

## Role Access Matrix

The table below shows which views each role can access:

| View | Inv. Mgr | Field Sales | Billing | Rep Mgr | Viewer | Acct Rep | Finance |
|------|:--------:|:-----------:|:-------:|:-------:|:------:|:--------:|:-------:|
| Inventory Management | ✅ | — | — | — | — | — | — |
| My Bits | — | ✅ | — | — | — | — | — |
| Find Bits | ✅ | ✅ | ✅ | — | ✅* | ✅ | ✅ |
| Transactions | ✅ | — | — | — | — | — | — |
| Nav History | ✅ | — | — | — | ✅ | — | ✅ |
| eTransfer Tickets | ✅ | ✅ | — | — | — | — | — |
| eBilling Workbench | — | ✅ | ✅ | — | — | ✅ | ✅ |
| Add/Edit Customer Rep | — | — | ✅ | ✅ | — | — | — |

\* Viewer role has access to a "lite" version of Find Bits.

## Common Features

All roles have access to these features:

--8<-- "content/features/_common-features-list.md"

## Changing Your Role

If you have access to multiple roles, you can switch between them in your Profile settings.

[Learn how to change roles :material-arrow-right:](../features/profile.md#changing-roles){ .md-button }
