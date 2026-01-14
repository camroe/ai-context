# Token Types & Authentication Methods

> **Parent Page**: OCPI 2.2.1 Implementation Guide  
> **Document Focus**: Detailed analysis of OCPI token types and Ford implementation strategy

---

## Overview: Four Token Types for Universal Access

Ford will implement **four distinct authentication methods** to ensure every Ford customer can charge anywhere, using their preferred method:

{panel:title=Ford Token Strategy|borderStyle=solid|borderColor=#0066cc|titleBGColor=#e6f3ff|bgColor=#ffffff}
**Goal**: Seamless charging regardless of customer preference, device availability, or technical capability
{panel}

---

## 🔑 Token Type #1: RFID Tokens (Physical Cards)

### Technical Specification

- **Standard**: ISO 14443 Type A/B contactless cards
- **Identifier**: Unique UID linked to Ford account
- **Range**: 4cm proximity reading

### Ford Implementation Strategy

{expand:title=RFID Card Types & Use Cases}
**FordPass RFID Card**

- Physical card mailed to customers after EV purchase
- Pre-linked to Ford account and payment method
- Backup authentication when phone unavailable

**Fleet Cards**  

- Corporate cards for Ford fleet vehicles
- Centralized billing and reporting
- Driver assignment tracking

**Family Sharing Cards**

- Multiple cards per household
- All linked to single Ford account
- Spending limits and notifications
{expand}

### Customer Experience Flow

```
Step 1: Customer receives FordPass RFID card in mail
Step 2: Card pre-linked to Ford account automatically  
Step 3: At station → Tap card on reader
Step 4: CPO queries Ford: "Is token authorized?"
Step 5: Ford responds: "Yes, bill Ford account [xxx]"
Step 6: Charging starts immediately
Step 7: Push notification sent to FordPass app
Step 8: Session appears in app with real-time status
```

---

## 📱 Token Type #2: Mobile App Tokens (Digital)

### Technical Specification

- **Generation**: Dynamic tokens created by FordPass app
- **Security**: Time-limited, single-use authentication codes
- **Methods**: QR codes, NFC tags, Bluetooth proximity

### Ford Implementation Strategy

{info:title=Mobile Authentication Options}
**QR Codes**: App-generated codes for station scanners  
**NFC Tags**: Phone-based NFC via FordPass app  
**Bluetooth**: Vehicle-to-charger using phone as proxy  
**Vehicle Integration**: Direct vehicle authentication (no phone needed)
{info}

### Enhanced Customer Experience Flow

```
Step 1: Customer approaches charging station
Step 2: FordPass app auto-detects nearby charger (geolocation)
Step 3: App displays: "Start charging at ChargePoint #1234?"
Step 4: Customer taps "Start" → App generates session token
Step 5: Token validated with Ford via OCPI
Step 6: Charging begins, real-time monitoring in app
Step 7: Customer controls: pause, adjust speed, schedule completion
Step 8: Automatic payment, receipt delivered via app
```

---

## 💳 Token Type #3: Contract ID Tokens (Subscriptions)

### Business Model Integration

- **Purpose**: Link charging sessions to Ford service contracts
- **Billing**: Subscription plans and corporate agreements
- **Flexibility**: Multiple pricing models and partnership deals

### Ford Implementation Strategy

{expand:title=Contract Token Applications}
**FordPass Charging Plans**

- Example: "$19/month unlimited Level 2 charging"
- Tiered plans: Basic, Premium, Fleet
- Family plans with shared quotas

**Corporate Contracts**

- Fleet agreements with pre-negotiated rates
- Employee benefit programs
- Volume discounts for large deployments

**Partnership Plans**  

- Special rates via Ford partnerships
- Example: "Ford + Costco Charging Plan"
- Co-branded offerings with retailers/employers
{expand}

---

## 💰 Token Type #4: Credit Card PAN Tokens (Guest Payment)

### Technical Specification

- **Security**: Tokenized Primary Account Numbers (PAN)
- **Compliance**: PCI DSS standards for card data
- **Integration**: Ford payment processing system

### Ford Implementation Strategy

{note:title=Guest Charging & Backup Payment}
**Guest Charging**: Non-Ford customers using Ford payment processing  
**Backup Payment**: Fallback when FordPass authentication fails  
**Corporate Travel**: Employees using corporate cards for personal vehicles
{note}

---

## 🚗 Advanced Authentication: Vehicle-Integrated Tokens

### The "Tesla-Like" Seamless Experience

{panel:title=Zero-Touch Authentication|borderStyle=solid|borderColor=#00aa00|titleBGColor=#e6ffe6|bgColor=#ffffff}
**Vision**: Customer plugs in cable → Charging starts automatically → No apps, cards, or interaction needed
{panel}

### Technical Implementation

- **Vehicle Identifier**: VIN used as OCPI token
- **Communication**: Encrypted cellular connection to Ford backend
- **Validation**: Real-time vehicle identity and account verification
- **Integration**: Works with Mach-E, F-150 Lightning, E-Transit

### Customer Experience

```
Step 1: Ford vehicle pulls into any OCPI-compatible station
Step 2: Vehicle automatically authenticates via built-in cellular
Step 3: Cable connection triggers immediate session start
Step 4: FordPass app shows progress automatically
Step 5: Customer walks away, receives completion notifications
Step 6: Payment processed via saved Ford account
Step 7: Receipt delivered via app and email
```

---

## Token Security & Lifecycle Management

### Security Features

{expand:title=Multi-Layer Security Architecture}
**Token Rotation**: Dynamic tokens refreshed every 30 days  
**Geofencing**: Regional/country usage restrictions  
**Velocity Limits**: Maximum charging frequency controls  
**Fraud Detection**: ML-based anomaly detection  
**Emergency Revocation**: Instant blocking for compromised tokens
{expand}

### Status Management

- **VALID**: Active account, payment method confirmed
- **BLOCKED**: Customer request, fraud, or payment failure  
- **EXPIRED**: Account closure or service termination
- **SUSPENDED**: Temporary hold for maintenance/issues

---

## Multi-Token Strategy Benefits

### Customer Flexibility

- **Primary**: Vehicle-integrated (seamless experience)
- **Secondary**: Mobile app (universal compatibility)  
- **Backup**: RFID card (phone-independent)
- **Emergency**: Credit card (guest payment option)

### Business Intelligence

- **Usage Analytics**: Which authentication methods customers prefer
- **Geographic Patterns**: Token usage by region/station type
- **Customer Segmentation**: Different strategies for different user types
- **Partnership Insights**: Which CPO integrations drive most value

---

**Related Pages:**

- [Customer Experience Scenarios](03-customer-experience-scenarios.confluence.md)
- [Implementation Architecture](04-implementation-architecture.confluence.md)
- [Security & Compliance Framework](05-security-compliance.confluence.md)

---

Last Updated: October 27, 2025
