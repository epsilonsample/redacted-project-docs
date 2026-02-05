# Searching and Filtering Data

Asset Management provides powerful search and filtering capabilities across all views. This guide covers the common patterns used throughout the application.

## Global Search

Most views include a **global search box** above the data table. This searches across all visible columns.

![Global Search Placeholder](../assets/images/placeholder-global-search.svg)

**To use global search:**

1. Click in the search box above the table.
2. Type your search term.
3. Results filter automatically as you type.

!!! tip "Search Tips"
    - Search works across all columns (Serial Number, Item No, Status, etc.).
    - Search is case-insensitive
    - Partial matches are supported.

## Column Sorting

### Desktop & iPad

1. Hover over a column header
2. Click to the **left** of the funnel icon.
3. Sort arrows appear
4. Click the **up arrow** to sort ascending.
5. Click the **down arrow** to sort descending.
6. Click again to remove sorting.

![Column Sorting Placeholder](../assets/images/placeholder-column-sort.svg)

### Mobile

1. Tap the **Sort Order** button.
2. Select your sort preferences.
3. Choose **Sort** for one-time sorting.
4. Choose **Sort and Save Sort Order** to remember your preference.

## Column Filtering

### Desktop & iPad

1. Click the **funnel icon** in a column header.
2. A filter popup appears with available values.
3. Check the boxes for values you want to see.
4. The table updates to show only matching rows.

![Column Filter Placeholder](../assets/images/placeholder-column-filter.svg)

!!! note "Mobile Limitation"
    Column-specific filters are not available on mobile. Use the view's main filters (like EBILLING or SALES PERSON filters) instead.

## Clearing Filters and Sort Orders

### Clear Filter-Sort Button

Most views include a **Clear filter-sort** button that resets:

- ✅ Column sorting
- ✅ Column filters
- ✅ Global search text
- ❌ Main view filters (like eBilling or date filters).

!!! warning "What Doesn't Clear"
    The Clear filter-sort button affects only the **table display**. It does not clear:
    
    - eBilling filter selections
    - Sales Person filter selections.
    - Date range filters
    - Main search criteria (like in Find Bits).

### Clearing Main Filters

To clear main view filters:

- In **eBilling Workbench**: Click **Clear filter**
- In **Find Bits**: Manually reset your filter selections.
- In **Transactions**: Clear date filters manually.

## Common Filter Patterns

### Date Range Filtering

Many views support filtering by date range:

1. Set the **Start Date**.
2. Set the **End Date**.
3. Click **Apply Filters** or **Search**.

### Toggle Switches

Some views include toggle switches for quick filtering:

| Toggle | Function |
|--------|----------|
| **See Locked Serials** | Show/hide locked bits |
| **Pending / Sent/Received** | Switch between transfer states |
| **Pending / In Progress/Filled** | Switch between order states |

## View-Specific Filtering

### Find Bits

Uses a filter panel with multiple criteria. See [Find Bits View](../views/find-bits.md) for details.

### eBilling Workbench

Uses dropdown filters for quick access. See [eBilling Workbench View](../views/ebilling-workbench.md) for details.

### Nav History Transactions

Uses a combination of dropdown filters and date ranges. Default look-back is 7 days.

## Exporting Data

Some views support exporting filtered data:

1. Apply your desired filters.
2. Click **Export to CSV**.
3. A CSV file downloads with the filtered data.

!!! info "Available In"
    Export functionality is available in:
    
    - Transactions view
    - (Check individual view documentation for availability).

## Best Practices

1. **Start broad, then narrow** — Begin with fewer filters and add more to refine results.
2. **Use primary filters first** — In Find Bits, always set Bit Status and Company first.
3. **Save common filters** — In eBilling Workbench, save frequently used filter combinations.
4. **Clear filters when stuck** — If you're not seeing expected results, try clearing all filters.
