# Permissions Matrix

This reference documents the specific permissions each role has within the Service Receipt (SR) Summary Line Action Menu.

## Field Sales Permissions

| Action | Billed | Reviewed/Approved | Approved & Locked | Invoiced |
|--------|:------:|:-----------------:|:-----------------:|:--------:|
| Well Information | Editable | View Only | View Only | View Only |
| Print/Share SR Billing PDF | ✅ | ✅ | ✅ | ✅ |
| Print/Share SR Run PDF | ✅ | ✅ | ✅ | ✅ |
| Add Stamped PDF/Photo | Edit | View* | View* | View* |
| Add Competitor's Bit Run Data | Edit | View* | View* | View* |
| Service Receipt Lines | ✅ | ✅ | ✅ | ✅ |
| Edit Nav Service Receipt Date | ✅ | — | — | — |

*"View" only appears when PDF/Photo has been uploaded; otherwise not visible

## Billing Permissions

| Action | Billed | Reviewed/Approved | Approved & Locked | Invoiced |
|--------|:------:|:-----------------:|:-----------------:|:--------:|
| Well Information | Editable | Editable | View Only | View Only |
| Print/Share SR Billing PDF | ✅ | ✅ | ✅ | ✅ |
| Print/Share SR Run PDF | ✅ | ✅ | ✅ | ✅ |
| Add Stamped PDF/Photo | Edit | Edit | View* | View* |
| Add Competitor's Bit Run Data | Edit | Edit | View* | View* |
| Update National Account Rep | ✅ | ✅ | — | — |
| Service Receipt Lines | ✅ | ✅ | ✅ | ✅ |

*"View" only appears when PDF/Photo has been uploaded; otherwise not visible

## Account Rep & Finance Permissions

!!! note "View-Only Roles"
    Account Rep and Finance roles have view-only access across all statuses.

| Action | Billed | Reviewed/Approved | Approved & Locked | Invoiced |
|--------|:------:|:-----------------:|:-----------------:|:--------:|
| Well Information | View Only | View Only | View Only | View Only |
| Print/Share SR Billing PDF | ✅ | ✅ | ✅ | ✅ |
| Print/Share SR Run PDF | ✅ | ✅ | ✅ | ✅ |
| View Stamped PDF/Photo | —* | —* | —* | —* |
| View Competitor's Bit Run Data | —* | —* | —* | —* |
| Service Receipt Lines | ✅ | ✅ | ✅ | ✅ |

*Not visible unless content has been uploaded

## Understanding Status Progression

```
Billed → Reviewed/Approved → Approved & Locked → Invoiced
```

| Status | Description |
|--------|-------------|
| **Billed** | Initial billing entry; most fields editable |
| **Reviewed/Approved** | Under review; limited editing available |
| **Approved & Locked** | Approved and locked; view-only for most actions |
| **Invoiced** | Final state; all fields view-only |

## Key Takeaways

1. **Field Sales** loses editing capabilities after the Billed status.
2. **Billing** maintains edit access through Reviewed/Approved status.
3. **Account Rep & Finance** have view-only access at all statuses.
4. **PDF/Photo viewing** is only available when content exists.
5. All roles can always view Service Receipt Lines and print PDFs.

## Related Documentation

- [eBilling Workbench View](../views/ebilling-workbench.md)
- [User Roles Overview](../roles/index.md)
- [Admin Permissions Management](permissions.md)
