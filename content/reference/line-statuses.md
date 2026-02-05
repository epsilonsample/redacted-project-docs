# Ticket Line Statuses

Reference guide for all possible ticket line statuses in the eBilling Workbench.

## Status Definitions

| Status | Description |
|--------|-------------|
| **Open** | Line is active and editable |
| **Ready to Review** | Line is complete and awaiting review |
| **Approved** | Line has been reviewed and approved |
| **Locked** | Line is locked and cannot be edited |
| **Invoiced** | Line has been invoiced to the customer |

## Status Transitions

Ticket lines progress through these stages:

1. **Open** → Ready to Review (all information entered)
2. **Ready to Review** → Approved (reviewed and confirmed)
3. **Approved** → Locked (locked for invoicing)
4. **Locked** → Invoiced (invoice generated)

## Related Documentation

- [eBilling Workbench View](../views/ebilling-workbench.md)
- [How to Find Tickets](../how-to/find-tickets.md)
- [How to Create Service Receipt](../how-to/create-sr-ticket.md)
