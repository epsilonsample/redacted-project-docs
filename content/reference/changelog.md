# Changelog

All notable changes to Asset Management are documented here.

## Version C_2025.05.001 (May 2025)

### Improvements

- Updated spec sheets fetch functionality.
- Enhanced print preview on Windows
- Updated runtime-build to latest version.
- Updated all CloudCode tasks to v1.13.0.

### Bug Fixes

- Fixed spec sheet differences between BitLocker and Asset Management.
- Fixed error: "Cannot read properties of null (reading 'well_name')".
- Fixed fetch_spec_sheets_subtask log discrepancy.
- Fixed Historical PDF functionality
- Fixed route error process change per serial.
- Fixed webhook_assestchange error
- Fixed well data in DB not displaying on UI.

### New Features

- Added **Tariff Surcharge** support:
    - SR Billing PDF updates.
    - Delivery Ticket view & PDF integration.
    - SR Details view display.
    - Toggle/Checkbox for enabling
- Added consignment constraints
- Created delete_ebilling_ticket_updates cloud code function
- Added "Delete _ebilling_ticket_updates" button to ADMIN Integration view.

### Data Management

- Archive functionality for Can Master Ticket Group.
- Archiving existing Can Master Ticket records for inactive customers.
- Updated run_archive_wellselection_list

### Technical Updates

| Ticket | Description |
|--------|-------------|
| JCB-911 | INC0134186 Update Spec Sheets Fetch |
| JCB-1012 | Print Preview on Windows |
| JCB-1044 | INC0148810 Spec sheet differences |
| JCB-1061 | Create CC run_delete_ebilling_ticket_updates |
| JCB-1094 | Update Runtime-build to latest |
| JCB-1095 | Update ALL CloudCode tasks to v1.13.0 |
| JCB-1096 | INC0168596 Archive Can Master Ticket Group |
| JCB-1107 | BUG: Error Cannot read properties of null |
| JCB-1108 | fetch_spec_sheets_subtask discrepancy |
| JCB-1109 | Add Consignment Constraints |
| JCB-1112 | Create Delivery Ticket - Well data logic |
| JCB-1115 | Archive Can Master Ticket for inactive customers |
| JCB-1116 | Limit of 12 |
| JCB-1118 | Historical PDF not working |
| JCB-1121 | ADMIN Integration updates |
| JCB-1124 | route error process change per serial |
| JCB-1125 | webhook_assestchange error |
| JCB-1126 | Well data DB/UI sync |
| JCB-1128 | TARIFF SURCHARGE - SR Billing PDF |
| JCB-1133 | TARIFF SURCHARGE - Delivery Ticket |
| JCB-1134 | TARIFF SURCHARGE - SR Details |
| JCB-1135 | Print Preview for Historical PDF |
| JCB-1145 | TARIFF SURCHARGE - Toggle |
| JCB-1146 | TARIFF SURCHARGE - PDF tweaks |
| JCB-1149 | TARIFF SURCHARGE - Save fix |
