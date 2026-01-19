---
name: React FAA Best Practices
description: Coding standards and best practices for FAA repair station React applications
tags:
  - react
  - faa
  - best-practices
  - aviation
patterns:
  - "**/*repair-station*.tsx"
  - "**/*faa*.tsx"
---

# React FAA Best Practices

## Component Structure
- Use TypeScript for type safety with FAA data structures
- Separate business logic from UI components
- Implement proper error boundaries for compliance operations

## Data Management
- Never hardcode FAA certificate numbers or sensitive data
- Use environment variables for API endpoints
- Implement proper state management for audit trails

## Compliance
- Validate all FAA data before submission
- Log all state changes for audit purposes
- Implement role-based access control for compliance functions
- Document compliance decisions in code comments

## Testing
- Write unit tests for all validation functions
- Test edge cases in FAA data formats
- Include integration tests for compliance workflows

## Security
- Sanitize user inputs before FAA data processing
- Use HTTPS for all FAA-related communications
- Implement proper authentication and authorization
