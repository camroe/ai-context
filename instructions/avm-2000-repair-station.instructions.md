# AVM-2000 Repair Station Management

## Overview

AVM-2000 is a comprehensive Windows-based repair station management software developed by TangoWare (CTI). It's designed to manage all aspects of aviation repair station operations, including work orders, inventory, invoicing, compliance documentation, and financial management.

**Reference**: See `references/avm-2000/avmguide.md` for complete documentation.

## Core Modules & Functions

### Work Orders
- **Purpose**: Central hub for tracking aircraft repair and maintenance work
- **Key Features**:
  - Create and manage repair tasks with labor, parts, and equipment tracking
  - Support for custom job/work types
  - Task status configuration and tracking
  - Labor budgeting and cost estimation
  - TBO (Time Between Overhaul) tracking integration
  - Work order conversion to invoices
  - Equipment and parts requisition management
  - Exchange/repair item tracking with cores

### Documentation & Compliance
- **337 Forms**: FAA Form 337 (Major Repair and Alteration)
  - Conformity pages (6 & 7)
  - Work accomplished documentation
  - Printing with electronic signatures (optional)

- **8130-3 Forms**: Airworthiness Certification
  - Configuration and setup
  - Batch creation and management
  - Printing capabilities

- **Weight & Balance Documentation**:
  - Fixed wing weight & balance
  - Rotary wing (helicopter) weight & balance
  - Component tracking and calculations

- **Material Certification Forms (MCF)**:
  - Up to 22 items per form
  - Copy functionality from invoices

### Inventory Management
- **Parts Management**:
  - Serialized and batch tracking
  - SKU management with multiple condition fields
  - PartsBase condition tracking
  - AEA exchange pricing
  - Inventory history and cost updates
  - Import/update from spreadsheet (XLS)

- **Equipment Specs**:
  - Installed equipment master database
  - Equipment integration with work orders and quotes

- **Test Equipment**:
  - Calibration tracking
  - Check in/out logging
  - Repair history

### Financial Management
- **Accounts Receivable (A/R)**:
  - Customer invoicing with tax support (up to 4 tax rates)
  - Customer statements (batch and individual)
  - Customer payments and deposits
  - Credit memos and adjustments
  - Terms configuration (customizable)

- **Accounts Payable (A/P)**:
  - Vendor management and contact tracking
  - PO's (Purchase Orders) and expenses
  - Vendor payments and check management
  - Vendor adjustments
  - Vendor history tracking

- **General Ledger (GL)**:
  - GL account management with cost centers
  - GL adjustments with configuration
  - COGS (Cost of Goods Sold) account support
  - Monthly and annual reporting

- **Financial Reports**:
  - P&L (Income Statement)
  - Annual totals
  - Monthly totals with browse functionality
  - Special financials reports

### Customer & Vendor Management
- **Customers**:
  - Contact information with search functionality
  - AR Terms (customizable payment terms)
  - Hide from picklists for inactive customers
  - Comments and history tracking
  - Integration with invoices and work orders

- **Vendors**:
  - Multi-contact support
  - Order information and history
  - Hide from picklists for inactive vendors
  - Approved vendor list reporting

### Additional Features
- **Quotes & Estimates**:
  - Quote templates for recurring work
  - Pricing updates (all items, template items, or non-template items)
  - Labor, parts, equipment, and trades breakdown
  - Customer estimate details with sign-off capability
  - Margin calculations

- **Aircraft Management**:
  - Aircraft database with integration to other modules
  - Inspection tracking
  - Aircraft types (manufacturers)

- **Recurring Invoices**:
  - Template-based recurring billing
  - Automatic invoice creation from recurring templates
  - Modification before posting

- **TBO (Time Between Overhaul) Tracking** (Optional Module):
  - Component master management
  - Flight record tracking
  - Forecast reporting
  - Detail inspections and extensions

- **ATC (Attendance Time Clock)** (Optional Module):
  - Employee time tracking
  - WO labor entry integration
  - Billed vs. actual hours tracking

- **QuickBooks® Integration** (Optional Module):
  - Customer, vendor, and invoice synchronization
  - Chart of accounts mapping
  - GL account transfer options
  - Custom memo field configuration
  - Support for QB 2008-2011

### Utility & Administrative Features
- **Security** (Optional Module):
  - User login and password management
  - Access levels configuration
  - Menu permission groups
  - Control permission groups
  - Employee sensitive data access control
  - Electronic signature support (optional)

- **Backup & Recovery**:
  - Internal backups
  - External backups
  - Reindex/pack table utilities
  - Data restoration procedures

- **Reporting**:
  - Query-based reporting across modules
  - Custom report creation
  - Print-to-file capability (optional)
  - Export to XLS format

- **Electronic Document Storage (EDS)** (Optional Module):
  - Document attachment and storage
  - Backup procedures

- **Print-to-File** (Optional Module):
  - File-based printing
  - Email attachment support (up to 3 additional files)

## Key Workflows

### Work Order to Invoice Conversion
1. Create work order with tasks, labor, parts, and equipment
2. Complete work with electronic signatures (optional)
3. Convert work order to invoice
4. Apply customer AR terms
5. Post invoice for financial recording

### Compliance Documentation
1. Create 337 or 8130-3 form
2. Attach work details from work order
3. Apply electronic signature (optional)
4. Print for compliance filing

### Purchase Order to Vendor Payment
1. Create PO with requisitions from work order
2. Receive items into inventory
3. Create vendor adjustment if needed
4. Pay vendor via check or payment method
5. Reconcile in general ledger

## Important Configuration Areas
- **Customer AR Terms**: Configure payment terms for invoicing
- **Invoice Tax Configuration**: Set up 1-4 tax rates with GL account mapping
- **Cost Centers**: Assign to departments for GL tracking
- **Security Permissions**: Control user access to forms, reports, and sensitive data
- **Serialized Inventory**: Choose pricing strategy (standard or per-serial)
- **Work Order Statuses**: Define completion status options
- **Job/Work Types**: Customize work categories

## Version Information
Current guide covers version 6.50+ (as of August 2011). Notable features in recent releases:
- Multi-user licensing protection
- Electronic signatures capability
- QuickBooks® integration
- TBO component tracking
- Enhanced weight & balance documentation
- Improved UI with larger screens (1024x768 minimum resolution required)

## Integration Considerations
When building FAA Repair Station tracking software to replace or complement AVM-2000:
- Understand the relationship between work orders, invoices, and compliance documents
- Consider data migration strategies for existing repair station data
- Map AVM-2000 GL accounts and cost centers to new system
- Plan for electronic signature requirements
- Plan for multi-user/multi-location support
- Ensure FAA Form 337 and 8130-3 compliance in data model
- Consider TBO tracking requirements
- Plan for inventory serialization and batch tracking

## References
- See `references/avm-2000/avmguide.md` for complete AVM-2000 user guide
- See `references/avm-2000/starter.pdf` for quick start guide