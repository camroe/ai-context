#!/bin/bash

# OCPI Repository Checkout Script
# Comprehensive script to clone all OCPI-related repositories for Ford OCPI implementation

# Set up directory structure
OCPI_ROOT_DIR="$HOME/ocpi-workspace"
OFFICIAL_DIR="$OCPI_ROOT_DIR/official"
IMPLEMENTATIONS_DIR="$OCPI_ROOT_DIR/implementations"
TOOLS_DIR="$OCPI_ROOT_DIR/tools"
SPECS_DIR="$OCPI_ROOT_DIR/specifications"

echo "🔋 OCPI Repository Checkout Script"
echo "=================================="
echo "Creating OCPI workspace at: $OCPI_ROOT_DIR"

# Create directory structure
mkdir -p "$OFFICIAL_DIR"
mkdir -p "$IMPLEMENTATIONS_DIR"
mkdir -p "$TOOLS_DIR"
mkdir -p "$SPECS_DIR"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

clone_repo() {
    local repo_url="$1"
    local target_dir="$2"
    local repo_name=$(basename "$repo_url" .git)
    
    echo -e "${BLUE}📥 Cloning: ${repo_name}${NC}"
    
    if [ -d "$target_dir/$repo_name" ]; then
        echo -e "${YELLOW}⚠️  Directory already exists: $target_dir/$repo_name${NC}"
        echo -e "${YELLOW}   Updating existing repository...${NC}"
        cd "$target_dir/$repo_name" && git pull origin main 2>/dev/null || git pull origin master 2>/dev/null
        cd - > /dev/null
    else
        git clone "$repo_url" "$target_dir/$repo_name"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ Successfully cloned: $repo_name${NC}"
        else
            echo -e "${RED}❌ Failed to clone: $repo_name${NC}"
        fi
    fi
    echo ""
}

echo -e "${GREEN}1. Official OCPI Specifications${NC}"
echo "================================"

# Official OCPI Protocol Specifications
clone_repo "https://github.com/ocpi/ocpi.git" "$OFFICIAL_DIR"

# OCPI 3.0 Development (if accessible)
echo -e "${YELLOW}Note: OCPI 3.0 repository requires EV Roaming Foundation membership${NC}"

echo -e "${GREEN}2. OCPI Implementation Examples${NC}"
echo "==============================="

# Known OCPI implementations and libraries
IMPLEMENTATION_REPOS=(
    "https://github.com/NewMotion/ocpi-endpoints.git"
    "https://github.com/extrawest/Extrawest-OCPI-2.2.1-CPO-Server.git"
    "https://github.com/extrawest/Extrawest-OCPI-2.2.1-EMSP-Server.git"
    "https://github.com/thenewmotion/ocpi-circe.git"
    "https://github.com/ShellRechargeSolutionsEU/ocpi-protocol.git"
    "https://github.com/NOWUM/ocpi.git"
    "https://github.com/marcelblijleven/ocpi.git"
    "https://github.com/ocpi-lib/ocpi-lib.git"
    "https://github.com/ZuhraCodes/ocpi.git"
)

for repo in "${IMPLEMENTATION_REPOS[@]}"; do
    clone_repo "$repo" "$IMPLEMENTATIONS_DIR"
done

echo -e "${GREEN}3. OCPI Testing and Validation Tools${NC}"
echo "===================================="

# Testing and validation tools
TOOL_REPOS=(
    "https://github.com/ocpi/ocpi-test-tool.git"
    "https://github.com/NewMotion/ocpi-test.git"
    "https://github.com/Switch2Energy/ocpi-test.git"
)

for repo in "${TOOL_REPOS[@]}"; do
    clone_repo "$repo" "$TOOLS_DIR"
done

echo -e "${GREEN}4. Additional OCPI Resources${NC}"
echo "==========================="

# Additional specification and documentation repositories
SPEC_REPOS=(
    "https://github.com/evroaming/ocpi-specification.git"
    "https://github.com/hubject/ocpi-spec.git"
)

for repo in "${SPEC_REPOS[@]}"; do
    clone_repo "$repo" "$SPECS_DIR"
done

# Search for additional OCPI repositories
echo -e "${BLUE}5. Searching for Additional OCPI Repositories${NC}"
echo "============================================="

echo "Searching GitHub API for OCPI-related repositories..."
SEARCH_RESULTS=$(curl -s "https://api.github.com/search/repositories?q=OCPI+electric+vehicle+charging&sort=stars&order=desc&per_page=50" 2>/dev/null)

if [ $? -eq 0 ]; then
    # Extract repository clone URLs
    ADDITIONAL_REPOS=$(echo "$SEARCH_RESULTS" | grep -o '"clone_url": "[^"]*"' | cut -d'"' -f4 | head -20)
    
    echo "Found additional OCPI repositories:"
    echo "$ADDITIONAL_REPOS" | nl
    
    echo ""
    echo -e "${YELLOW}Would you like to clone additional repositories? (y/n)${NC}"
    read -r response
    
    if [[ "$response" =~ ^[Yy]$ ]]; then
        mkdir -p "$OCPI_ROOT_DIR/additional"
        echo "$ADDITIONAL_REPOS" | while read -r repo; do
            if [[ ! "$repo" =~ (ocpi/ocpi|NewMotion/ocpi-endpoints|extrawest|thenewmotion/ocpi-circe) ]]; then
                clone_repo "$repo" "$OCPI_ROOT_DIR/additional"
            fi
        done
    fi
else
    echo -e "${YELLOW}⚠️  Could not search GitHub API (rate limit or network issue)${NC}"
fi

# Create workspace overview
echo -e "${GREEN}6. Creating Workspace Overview${NC}"
echo "=============================="

cat > "$OCPI_ROOT_DIR/README.md" << 'EOF'
# OCPI Development Workspace

This workspace contains all OCPI-related repositories for Ford's EV charging implementation.

## Directory Structure

- **official/**: Official OCPI protocol specifications from EVRoaming Foundation
- **implementations/**: Reference implementations and libraries
- **tools/**: Testing, validation, and development tools
- **specifications/**: Additional specification repositories
- **additional/**: Other OCPI-related repositories

## Key Repositories

### Official Specifications
- `official/ocpi/`: The main OCPI protocol specification (2.2.1, 2.3.0, etc.)

### Reference Implementations
- `implementations/ocpi-endpoints/`: NewMotion OCPI endpoints implementation
- `implementations/Extrawest-OCPI-*-Server/`: Complete CPO/eMSP server implementations
- `implementations/ocpi-protocol/`: Shell Recharge Solutions protocol implementation

### Testing Tools
- `tools/ocpi-test-tool/`: Official OCPI testing framework
- `tools/ocpi-test/`: NewMotion testing utilities

## Ford OCPI Implementation Context

This workspace supports Ford's OCPI 2.2.1 implementation with:
- FordPass integration
- Vehicle authentication (Mach-E, F-150 Lightning, E-Transit)
- GCP platform deployment
- Hub integration (Gireve, Hubject)
- Real-time charging session management

## Getting Started

1. Review the official specification in `official/ocpi/`
2. Examine reference implementations for architecture patterns
3. Use testing tools to validate OCPI compliance
4. Follow Ford-specific architectural guidelines from the OCPI Principal Architect

## Branch Strategy

Each repository may have different branch structures:
- `main`/`master`: Latest stable release
- `develop`: Active development
- `release-*`: Version-specific releases
- `feature/*`: Feature development branches

## Updates

Run `./checkout-ocpi-repos.sh` again to update all repositories with latest changes.
EOF

# Create update script
cat > "$OCPI_ROOT_DIR/update-all-repos.sh" << 'EOF'
#!/bin/bash
# Update all OCPI repositories

find . -name ".git" -type d | while read -r git_dir; do
    repo_dir=$(dirname "$git_dir")
    echo "Updating: $repo_dir"
    cd "$repo_dir" && git pull
    cd - > /dev/null
done
EOF

chmod +x "$OCPI_ROOT_DIR/update-all-repos.sh"

# Summary
echo -e "${GREEN}✅ OCPI Repository Checkout Complete!${NC}"
echo "===================================="
echo ""
echo "📁 Workspace Location: $OCPI_ROOT_DIR"
echo ""
echo "📋 Summary:"
echo "   - Official specifications: $(find "$OFFICIAL_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ') repositories"
echo "   - Implementation examples: $(find "$IMPLEMENTATIONS_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ') repositories"  
echo "   - Testing tools: $(find "$TOOLS_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ') repositories"
echo "   - Specifications: $(find "$SPECS_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ') repositories"
echo ""
echo "🚀 Next Steps:"
echo "   1. cd $OCPI_ROOT_DIR"
echo "   2. Review README.md for workspace overview"
echo "   3. Start with official/ocpi/ for OCPI 2.2.1 specification"
echo "   4. Examine implementations/ for reference architectures"
echo ""
echo "🔄 To update all repositories: cd $OCPI_ROOT_DIR && ./update-all-repos.sh"
echo ""
echo -e "${BLUE}Happy OCPI development! 🔋⚡${NC}"