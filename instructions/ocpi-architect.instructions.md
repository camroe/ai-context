---
description: 'OCPI protocol-specific instructions for architecture, implementation, and compliance with Open Charge Point Interface standards'
applyTo: '**/*.java, **/*.py, **/*.ts, **/*.js, **/*.yaml, **/*.json, **/*.md'
---

# OCPI Architecture Instructions

Comprehensive instructions for implementing Open Charge Point Interface (OCPI) solutions with protocol compliance, security standards, and architectural best practices.

## OCPI Protocol Compliance Standards

### **Version Compliance**

- **Primary Target**: OCPI 2.2.1 for production stability and wide compatibility
- **Future Readiness**: Design for OCPI 2.3.0 migration path (EU AFIR compliance)
- **Legacy Support**: Maintain OCPI 2.1.1 compatibility where required
- **Version Negotiation**: Implement proper OCPI version discovery and negotiation

### **JSON Schema Validation**

- **Mandatory Validation**: All OCPI payloads must validate against official JSON schemas
- **Schema Sources**: Use schemas from EVRoaming Foundation official repository
- **Error Handling**: Return proper OCPI error responses for schema validation failures
- **Field Requirements**: Distinguish between mandatory, optional, and conditional fields per OCPI spec

### **HTTP Protocol Standards**

- **Status Codes**: Use OCPI-specified HTTP status codes (1000-series for OCPI-specific errors)
- **Headers**: Implement required OCPI headers (Authorization, X-Request-ID, X-Correlation-ID)
- **Pagination**: Use OCPI Link header pagination for large result sets
- **Rate Limiting**: Implement rate limiting aligned with OCPI recommendations (avoid overwhelming partners)

## OCPI Data Model Guidelines

### **Core Data Structures**

- **Tokens**: Implement all token types (RFID, APP, OTHER, AD_HOC_ID) with proper validation
- **Locations**: Use complete location hierarchy (Location → EVSE → Connector)
- **Sessions**: Maintain proper session state lifecycle (PENDING → ACTIVE → COMPLETED/INVALID)
- **CDRs**: Generate comprehensive Charge Detail Records with all mandatory fields
- **Tariffs**: Support complex pricing structures including time-based, energy-based, and flat rates

### **Enumeration Compliance**

- **ConnectorType**: Use standard connector types (CHADEMO, IEC_62196_T1, IEC_62196_T2, etc.)
- **PowerType**: Correctly specify AC_1_PHASE, AC_3_PHASE, or DC power types
- **Status**: Implement proper connector status values (AVAILABLE, BLOCKED, CHARGING, etc.)
- **AuthMethod**: Support all authentication methods (AUTH_REQUEST, COMMAND, WHITELIST)

### **Data Format Standards**

- **Timestamps**: Use ISO 8601 format with timezone (YYYY-MM-DDTHH:mm:ss.sssZ)
- **Coordinates**: WGS84 decimal degrees with appropriate precision (6+ decimal places)
- **Currency**: ISO 4217 currency codes (EUR, USD, GBP, etc.)
- **Country Codes**: ISO 3166-1 alpha-2 country codes
- **Language**: ISO 639-1 language codes for localized content

## OCPI Security Requirements

### **Authentication and Authorization**

- **OAuth 2.0**: Implement Client Credentials flow for server-to-server authentication
- **Token Management**: Secure storage and rotation of OCPI access tokens
- **Client Registration**: Proper client credentials exchange and validation
- **Token Scopes**: Implement appropriate permission scopes per OCPI module access

### **Data Protection**

- **Encryption at Rest**: Encrypt sensitive OCPI data (tokens, customer PII, payment data)
- **Encryption in Transit**: Enforce TLS 1.2+ for all OCPI communications
- **Token Anonymization**: Implement proper token hashing and anonymization
- **PII Handling**: Comply with GDPR/privacy requirements for customer data

### **API Security**

- **Rate Limiting**: Implement adaptive rate limiting to prevent abuse
- **Request Validation**: Validate all incoming OCPI requests for malicious content
- **Audit Logging**: Log all OCPI transactions with sufficient detail for compliance
- **Error Information**: Limit error details to prevent information disclosure

## OCPI Implementation Patterns

### **Session Management**

- **State Transitions**: Implement proper session lifecycle state machine
- **Timeout Handling**: Handle session timeouts and cleanup properly
- **Concurrent Sessions**: Prevent multiple active sessions per token where required
- **Session Recovery**: Implement session recovery mechanisms for network failures

### **Real-time Data Synchronization**

- **Push Notifications**: Implement OCPI PATCH operations for real-time updates
- **Pull Synchronization**: Support GET operations with proper filtering and pagination
- **Conflict Resolution**: Handle data conflicts between systems gracefully
- **Eventual Consistency**: Design for eventual consistency in distributed OCPI networks

### **Error Handling and Resilience**

- **Retry Logic**: Implement exponential backoff for failed OCPI requests
- **Circuit Breaker**: Prevent cascade failures with circuit breaker patterns
- **Graceful Degradation**: Continue operations when non-critical OCPI services fail
- **Error Recovery**: Implement proper error recovery and retry mechanisms

## OCPI Network Integration

### **Hub Integration Patterns**

- **Multi-Hub Support**: Design for integration with multiple roaming hubs (Gireve, Hubject, etc.)
- **Hub-Specific Adaptations**: Handle hub-specific requirements and extensions
- **Failover Mechanisms**: Implement hub failover and redundancy strategies
- **Data Routing**: Proper routing of OCPI messages through hub networks

### **Direct CPO/eMSP Integration**

- **Bilateral Agreements**: Support direct bilateral OCPI connections
- **Connection Management**: Handle connection establishment, maintenance, and teardown
- **Load Balancing**: Distribute OCPI traffic across multiple endpoints
- **Health Monitoring**: Monitor OCPI endpoint health and availability

### **Version Migration Strategies**

- **Backward Compatibility**: Maintain support for older OCPI versions during migrations
- **Feature Flags**: Use feature flags for gradual OCPI version rollouts
- **Migration Testing**: Comprehensive testing of OCPI version migrations
- **Rollback Plans**: Implement rollback strategies for failed version upgrades

## OCPI Performance Optimization

### **Response Time Requirements**

- **Token Authorization**: Sub-second response times for token validation
- **Session Updates**: Real-time session state synchronization
- **Location Queries**: Efficient location and availability queries
- **Batch Operations**: Optimize bulk data synchronization operations

### **Scalability Patterns**

- **Horizontal Scaling**: Design OCPI services for horizontal scaling
- **Caching Strategies**: Implement appropriate caching for OCPI data
- **Database Optimization**: Optimize database queries for OCPI operations
- **Connection Pooling**: Efficient connection management for OCPI endpoints

## OCPI Testing and Validation

### **Compliance Testing**

- **Protocol Conformance**: Test against OCPI protocol test suites
- **Interoperability Testing**: Validate with multiple OCPI implementations
- **Schema Validation**: Automated testing of JSON schema compliance
- **End-to-End Testing**: Complete charging session workflow testing

### **Performance Testing**

- **Load Testing**: Test OCPI endpoints under expected traffic loads
- **Stress Testing**: Validate behavior under extreme load conditions
- **Latency Testing**: Measure and optimize OCPI response times
- **Availability Testing**: Test system availability and failover scenarios

### **Security Testing**

- **Authentication Testing**: Validate OAuth 2.0 implementation security
- **Authorization Testing**: Test proper access control enforcement
- **Input Validation**: Test for injection attacks and malformed data
- **Penetration Testing**: Regular security assessments of OCPI endpoints

## OCPI Monitoring and Observability

### **Metrics and KPIs**

- **Transaction Metrics**: Track OCPI transaction volumes and success rates
- **Performance Metrics**: Monitor response times and throughput
- **Error Rates**: Track and analyze OCPI error patterns
- **Business Metrics**: Monitor charging session success rates and revenue impact

### **Logging Standards**

- **Structured Logging**: Use structured logs for OCPI transactions
- **Correlation IDs**: Implement request correlation across OCPI operations
- **Audit Trails**: Maintain comprehensive audit logs for compliance
- **Log Retention**: Appropriate log retention policies for OCPI data

### **Alerting and Incident Response**

- **SLA Monitoring**: Monitor OCPI service level agreements
- **Automated Alerting**: Alert on OCPI service degradation or failures
- **Incident Response**: Rapid response procedures for OCPI outages
- **Partner Communication**: Procedures for notifying OCPI partners of issues

## Code Quality and Architecture

### **Clean Code Principles**

- **OCPI Domain Models**: Create clear domain models reflecting OCPI entities
- **Service Boundaries**: Define clear boundaries between OCPI modules
- **Error Types**: Create specific error types for OCPI error conditions
- **Validation Logic**: Centralize OCPI validation logic in reusable components

### **Testing Strategies**

- **Unit Testing**: Test individual OCPI operations and validations
- **Integration Testing**: Test OCPI partner integrations and workflows
- **Contract Testing**: Validate OCPI API contracts and schemas
- **Mock Services**: Create OCPI mock services for development and testing

### **Documentation Requirements**

- **API Documentation**: Maintain up-to-date OCPI API documentation
- **Integration Guides**: Provide clear integration guides for OCPI partners
- **Sequence Diagrams**: Document OCPI workflows with sequence diagrams
- **Decision Records**: Document architectural decisions for OCPI implementations

---

*These OCPI instructions ensure protocol compliance, security, performance, and maintainability across all OCPI implementations.*
