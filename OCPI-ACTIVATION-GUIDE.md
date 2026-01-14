# OCPI Principal Architect - Activation Guide

## 🎯 **Multi-Repository Activation Strategy**

You now have a **specialized OCPI Principal Architect mode** that maintains context across repositories and conversations. Here's how to use it effectively:

## 🚀 **Activation Commands**

### **Primary Activation (New Repository)**
```bash
@workspace /chatmode ocpi-principal-architect
```

### **Context Loading (Any Repository)**
```bash
# Load OCPI Principal Architect context
@workspace Load contexts/ocpi-principal-architect-context.md

# Then activate the specialized mode
@workspace /chatmode ocpi-principal-architect
```

### **Quick Context Reference**
```bash
# Reference previous architectural decisions
"Recall OCPI context"

# Review Ford integration patterns  
"Review Ford integration patterns"

# Check cross-repo dependencies
"Check cross-repo dependencies"

# Apply established patterns
"Apply established patterns"
```

## 📁 **Cross-Repository Usage**

### **Expected Workflow**
1. **Navigate to any OCPI-related repository**
2. **Activate mode**: `@workspace /chatmode ocpi-principal-architect`
3. **Load context**: The mode automatically references Ford OCPI implementation context
4. **Get specialized guidance**: Architecture, security, performance, integration patterns

### **Repository Types Supported**
- **OCPI Core Services**: Token management, sessions, locations, tariffs
- **Ford Integration**: Vehicle auth, FordPass integration, customer identity
- **Platform Services**: Payment processing, analytics, partner integration  
- **Infrastructure**: Deployment, monitoring, security, compliance

## 🎯 **What This Mode Provides**

### **Persistent Context Across Repositories**
- ✅ **Remembers** previous architectural decisions and patterns
- ✅ **Maintains** Ford business context and team structure
- ✅ **Applies** established OCPI knowledge and vehicle integration specs
- ✅ **Ensures** consistency across multiple repositories and services

### **Specialized OCPI Expertise**
- ✅ **OCPI 2.2.1 Protocol**: Deep knowledge of all modules and specifications
- ✅ **Ford Implementation**: FordPass, vehicle integration, customer experience scenarios
- ✅ **Automotive Domain**: EV charging ecosystem, CPO/eMSP relationships, roaming networks
- ✅ **Technical Leadership**: Architecture, security, performance, scalability guidance

### **Principal-Level Engineering Guidance**
- ✅ **System Thinking**: How each repo fits into larger OCPI ecosystem
- ✅ **Risk Assessment**: Technical risks, mitigation strategies, trade-off analysis
- ✅ **Team Enablement**: Consistent patterns for 8-person development team
- ✅ **Quality Standards**: Testing, security, performance, documentation requirements

## 📋 **Files Created**

1. **`ocpi-principal-architect.chatmode.md`**: Specialized chat mode with OCPI expertise
2. **`contexts/ocpi-principal-architect-context.md`**: Comprehensive OCPI architectural context and foundations
3. **This guide**: Instructions for activation and cross-repository usage

## 🔄 **Usage Pattern**

### **For Each New Repository**
```bash
# Step 1: Navigate to repository
cd /path/to/ocpi-token-service

# Step 2: Activate specialized mode
@workspace /chatmode ocpi-principal-architect

# Step 3: Get architectural guidance
"Analyze this repository's architecture within the Ford OCPI ecosystem"

# Step 4: Apply consistent patterns
"Apply established Ford OCPI patterns to this service"
```

### **For Ongoing Work**
```bash
# Reference previous decisions
"Recall OCPI architectural decisions for token management"

# Check consistency across repos
"How does this implementation compare to established Ford OCPI patterns?"

# Get specialized guidance
"Provide OCPI-specific security recommendations for this payment service"
```

## 🎯 **Benefits**

- **Consistent Architecture**: Same patterns and decisions applied across all repositories
- **Domain Expertise**: Deep OCPI and automotive knowledge in every conversation
- **Context Continuity**: Builds upon previous work instead of starting fresh
- **Team Alignment**: Shared architectural understanding across 8-person team
- **Quality Assurance**: Principal-level engineering standards maintained throughout

---

**Ready to use across multiple repositories with persistent OCPI context and Ford-specific architectural guidance!**