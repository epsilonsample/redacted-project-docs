# Bit Statuses

Reference guide for all possible bit statuses in Asset Management.

## Status Definitions

| Status | Description |
|--------|-------------|
| **Available** | Bit is in inventory and ready for use |
| **In Use** | Bit is currently deployed at a job site |
| **Locked** | Bit is locked and cannot be transferred |
| **In Transit** | Bit is being transferred between locations |
| **Consigned** | Bit is placed with a customer under consignment |
| **DBR** | Damaged Beyond Repair — bit is retired |
| **LIH** | Lost In Hole — bit was lost downhole |
| **Returned** | Bit has been returned to warehouse |

## Status Transitions

Bits move through statuses as they are used:

1. **Available** → In Use (delivered to customer).
2. **In Use** → Returned (picked up from customer).
3. **In Use** → DBR (damaged beyond repair).
4. **In Use** → LIH (lost in hole).
5. **Available** → Locked (locked by Inventory Manager).
6. **Locked** → Available (unlocked).
7. **Available** → In Transit (transferred to another user).

## Related Documentation

- [Find Bits View](../views/find-bits.md)
- [Inventory Management View](../views/inventory-management.md)
- [How to Lock a Bit](../how-to/lock-bit.md)
