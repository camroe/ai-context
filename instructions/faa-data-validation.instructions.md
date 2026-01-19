---
name: FAA Data Validation Standards
description: Data validation standards for FAA repair station tracking systems
tags:
  - faa
  - validation
  - data-integrity
patterns:
  - "**/*validation*.ts"
  - "**/*validator*.ts"
---

# FAA Data Validation Standards

## Input Validation
- Validate certificate format: 3 characters + 6 digits (e.g., ABC123456)
- Verify repair station class is one of: A, B, C, D, E, F, G, H
- Validate all dates are in ISO 8601 format

## Business Rules
- Repair station class determines authorized capabilities
- Maintenance records must have corresponding technician records
- Audit trail timestamps must be in chronological order
- All compliance statuses must have supporting documentation

## Error Messages
- Provide specific, actionable error messages
- Include reference to applicable FAA regulations
- Suggest corrective actions for validation failures

## Logging
- Log all validation failures with full context
- Maintain audit trail of compliance checks
- Track validation performance metrics
