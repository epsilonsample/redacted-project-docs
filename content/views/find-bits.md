# Find Bits View

The Find Bits view provides advanced search capabilities for locating specific bits across the system.

!!! info "Role Availability"
    This view is available to: Inventory Manager, Field Sales, Billing, Viewer (lite), Account Rep, Finance

## Overview

![Find Bits View Placeholder](../assets/images/placeholder-find-bits.svg)

Use Find Bits when you need to:

- Locate a specific bit by serial number.
- Search inventory across multiple locations.
- Filter by product specifications.
- Find bits with specific statuses.

## Search Filters

### Primary Filters

| Filter | Description | Priority |
|--------|-------------|----------|
| **Serial or Item Number** | Direct lookup by serial/item number | High |
| **Bit Status** | Filter by current status (most important filter) | Critical |
| **Company** | Filter by company (most important filter) | Critical |

### Product Filters

| Filter | Description |
|--------|-------------|
| Product Group | Category of the bit |
| Bit Size | Physical dimensions |
| Bit Type | Classification type |

### Location Filters

| Filter | Description |
|--------|-------------|
| Bit District | Geographic district |
| Bit Location | Specific location |
| Stockpoint | Inventory stockpoint |

### Technical Filters

| Filter | Description |
|--------|-------------|
| APP ID | Application identifier |
| Gauge Length | Gauge measurement |
| Feature | Product features |
| Technology | Technology classification |

## Using Find Bits

### Basic Search

1. Navigate to **Find Bits** from the left menu (or click **Find Bits** button if available).
2. Set your filters (at minimum, set **Bit Status** and **Company**).
3. Click **Search**
4. Results display in the table below.

### Viewing Results

The results table supports:

- **Global search** — Search any field in the results.
- **Column sorting** — Click column headers to sort.
- **Column filtering** — Click the funnel icon to filter by specific values.
- **Clear filter-sort** — Reset all table filters and sorting.

!!! note "Filter Scope"
    The **Clear filter-sort** button only clears table filters, not the main search filters above.

### Viewing Bit Details

Click any row to open the **Bit Details** page for that bit.

## Locked Serials

Toggle **See Locked Serials** to include or exclude locked bits from your search results.

![Locked Serials Toggle](../assets/images/placeholder-locked-toggle.svg)

## Quick Actions

From the Find Bits results, you can:

--8<-- "content/views/_find-bits-actions.md"

## Navigation

| Button | Action |
|--------|--------|
| **Home** | Return to your role's home page |
| **Search** | Execute search with current filters |
| **Clear filter-sort** | Reset table display options |

## Related Documentation

- [Understanding Bit Statuses](../reference/bit-statuses.md)
- [Searching and Filtering Data](../features/search-filter.md)
- [Bit Details Page](../views/bit-details.md)
