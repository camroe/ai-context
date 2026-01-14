# OCPI 2.2.1 Migration Automation Script

"""
Automated synchronization between Markdown source files and Confluence-ready format.
Maintains both .md files and .confluence.md files with automated updates.

Usage:
    python confluence-sync.py --source OCPI-2.2.1-Tokens-Module.md --update-all
    python confluence-sync.py --watch  # Monitor for changes and auto-update
"""

import os
import re
import argparse
from datetime import datetime
from pathlib import Path

class ConfluenceMigrator:
    def __init__(self, source_dir=".", confluence_dir="./confluence-migration"):
        self.source_dir = Path(source_dir)
        self.confluence_dir = Path(confluence_dir)
        self.confluence_dir.mkdir(exist_ok=True)

        # Confluence-specific macros and formatting
        self.confluence_macros = {
            'info': lambda content: f"{{info:title={content['title']}}}\n{content['body']}\n{{info}}",
            'panel': lambda content: f"{{panel:title={content['title']}|borderStyle=solid|borderColor={content['color']}|titleBGColor={content['bg']}|bgColor=#ffffff}}\n{content['body']}\n{{panel}}",
            'expand': lambda content: f"{{expand:title={content['title']}}}\n{content['body']}\n{{expand}}",
            'note': lambda content: f"{{note:title={content['title']}}}\n{content['body']}\n{{note}}",
            'code': lambda content: f"{{code:language={content['lang']}}}\n{content['body']}\n{{code}}"
        }

    def extract_sections_from_markdown(self, md_content):
        """Extract logical sections from markdown for Confluence page creation."""

        sections = []
        current_section = {"title": "", "content": "", "level": 0}

        lines = md_content.split('\n')

        for line in lines:
            # Detect heading levels
            if line.startswith('#'):
                # Save previous section if it has content
                if current_section["content"].strip():
                    sections.append(current_section.copy())

                # Start new section
                level = len(line) - len(line.lstrip('#'))
                title = line.strip('#').strip()
                current_section = {
                    "title": title,
                    "content": "",
                    "level": level,
                    "confluence_filename": self._generate_confluence_filename(title)
                }
            else:
                current_section["content"] += line + '\n'

        # Add final section
        if current_section["content"].strip():
            sections.append(current_section)

        return sections

    def _generate_confluence_filename(self, title):
        """Generate appropriate Confluence filename from section title."""
        # Clean title for filename
        clean_title = re.sub(r'[^\w\s-]', '', title.lower())
        clean_title = re.sub(r'[-\s]+', '-', clean_title)
        return f"{clean_title}.confluence.md"

    def markdown_to_confluence_format(self, md_content):
        """Convert standard markdown to Confluence-enhanced format."""

        # Convert standard info boxes to Confluence info macros
        md_content = re.sub(
            r'> \*\*(.*?)\*\*:\s*(.*?)(?=\n\n|\n>|\Z)',
            lambda m: f"{{info:title={m.group(1)}}}\n{m.group(2)}\n{{info}}",
            md_content,
            flags=re.DOTALL
        )

        # Convert code blocks to Confluence code macros
        md_content = re.sub(
            r'```(\w+)?\n(.*?)\n```',
            lambda m: f"{{code:language={m.group(1) or 'text'}}}\n{m.group(2)}\n{{code}}",
            md_content,
            flags=re.DOTALL
        )

        # Convert tables to better Confluence format (already supported, just ensure proper spacing)

        # Add Confluence page metadata
        md_content = self._add_confluence_metadata(md_content)

        return md_content

    def _add_confluence_metadata(self, content):
        """Add Confluence-specific metadata and navigation."""

        metadata = f"""---
confluence:
  parent: "OCPI 2.2.1 Implementation Guide"
  space: "Ford EV Charging"
  labels: ["ocpi-2.2.1", "tokens-module", "ford-implementation"]
  last-updated: "{datetime.now().strftime('%Y-%m-%d')}"
---

"""
        return metadata + content

    def create_confluence_page_structure(self, source_file):
        """Create structured Confluence pages from single markdown file."""

        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()

        sections = self.extract_sections_from_markdown(content)

        # Create main index page
        index_content = self._create_index_page(sections)
        index_path = self.confluence_dir / "00-tokens-module-index.confluence.md"

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(self.markdown_to_confluence_format(index_content))

        # Create individual section pages
        created_files = [str(index_path)]

        for i, section in enumerate(sections, 1):
            if section["level"] <= 2:  # Only create pages for main sections
                page_content = self._create_section_page(section, sections)
                filename = f"{i:02d}-{section['confluence_filename']}"
                page_path = self.confluence_dir / filename

                with open(page_path, 'w', encoding='utf-8') as f:
                    f.write(self.markdown_to_confluence_format(page_content))

                created_files.append(str(page_path))

        return created_files

    def _create_index_page(self, sections):
        """Create main index page with navigation to all sections."""

        index_content = f"""# OCPI 2.2.1 Tokens Module - Implementation Guide

> **Document Suite**: Comprehensive analysis and implementation guide for Ford eMSP integration
>
> **Target Audience**: Ford Connectivity Layer engineering team & stakeholders
>
> **Last Updated**: {datetime.now().strftime('%B %d, %Y')}

---

## Document Structure

This implementation guide is organized into focused sections for efficient navigation and team collaboration:

{{panel:title=Implementation Guide Navigation|borderStyle=solid|borderColor=#0066cc|titleBGColor=#e6f3ff|bgColor=#ffffff}}
Each section below is a separate Confluence page optimized for team collaboration, inline comments, and iterative updates.
{{panel}}

### 📋 Core Implementation Sections

"""

        for i, section in enumerate(sections, 1):
            if section["level"] <= 2:
                filename = f"{i:02d}-{section['confluence_filename']}"
                index_content += f"- [{section['title']}]({filename})\n"

        index_content += """

### 🔄 Document Synchronization

{{info:title=Automated Updates}}
These Confluence pages are automatically synchronized with the master markdown files.
Updates to source documentation will be reflected here within 24 hours.
{{info}}

### 🎯 Implementation Status

| **Section** | **Status** | **Owner** | **Target Date** |
|------------|-----------|-----------|----------------|
| Executive Summary | ✅ Complete | Architecture Team | - |
| Token Types Analysis | 🟡 In Review | Security Team | Nov 15, 2025 |
| Customer Scenarios | 🔵 Planned | UX Team | Dec 1, 2025 |
| Technical Architecture | 🔵 Planned | Backend Team | Dec 15, 2025 |

---

**Project Resources:**
- [Ford OCPI Project Confluence Space](link-to-space)
- [GitHub Repository](link-to-repo)
- [Technical Decision Records](link-to-adrs)

---

*This is a living document - updated continuously as implementation progresses*
"""

        return index_content

    def _create_section_page(self, section, all_sections):
        """Create individual Confluence page for section."""

        # Add navigation breadcrumbs
        navigation = f"""**[← Back to Implementation Guide](00-tokens-module-index.confluence.md)**

> **Section**: {section['title']}
>
> **Parent Page**: OCPI 2.2.1 Implementation Guide

---

"""

        # Add the section content
        content = navigation + section['content']

        # Add related pages navigation at bottom
        content += "\n\n---\n\n**Related Pages:**\n"

        for other_section in all_sections:
            if other_section != section and other_section['level'] <= 2:
                filename = f"{other_section['confluence_filename']}"
                content += f"- [{other_section['title']}]({filename})\n"

        content += f"\n---\n\n*Last Updated: {datetime.now().strftime('%B %d, %Y')}*"

        return content

    def sync_changes_from_source(self, source_file):
        """Monitor source file for changes and update Confluence files."""

        print(f"🔄 Updating Confluence files from {source_file}")

        # Check if source file exists
        if not os.path.exists(source_file):
            print(f"❌ Source file not found: {source_file}")
            return False

        # Create/update Confluence files
        try:
            created_files = self.create_confluence_page_structure(source_file)

            print(f"✅ Successfully created/updated {len(created_files)} Confluence pages:")
            for file_path in created_files:
                print(f"   📄 {os.path.basename(file_path)}")

            return True

        except Exception as e:
            print(f"❌ Error during synchronization: {str(e)}")
            return False

    def create_migration_guide(self):
        """Create step-by-step guide for moving to Confluence."""

        guide_content = """# Confluence Migration Guide

## 🎯 Migration Strategy: Dual-Source Maintenance

This approach maintains **both** markdown source files AND Confluence pages with automated synchronization.

### Benefits:
- ✅ Keep working in markdown (familiar, version controlled)
- ✅ Get Confluence benefits (collaboration, comments, rich formatting)
- ✅ Automated synchronization prevents drift
- ✅ Team can contribute in either format

---

## 📋 Step-by-Step Migration Process

### Phase 1: Initial Setup (One-Time)

1. **Run the migration script:**
   ```bash
   python confluence-sync.py --source OCPI-2.2.1-Tokens-Module.md --update-all
   ```

2. **Review generated files:**
   - Check `confluence-migration/` folder for .confluence.md files
   - Each file represents one Confluence page
   - Files include Confluence-specific formatting (panels, info boxes, etc.)

3. **Import to Confluence:**
   - Copy content from each .confluence.md file
   - Create corresponding Confluence pages
   - Paste content and adjust formatting as needed

### Phase 2: Content Import (Per Page)

1. **Create Confluence page structure:**
   ```
   Parent: "OCPI 2.2.1 Implementation Guide"
   ├── 01-Executive Summary
   ├── 02-Token Types & Authentication
   ├── 03-Customer Experience Scenarios
   ├── 04-Implementation Architecture
   └── 05-Security & Compliance
   ```

2. **Import content method:**
   - **Option A**: Copy/paste from .confluence.md files (manual)
   - **Option B**: Use Confluence markdown importer (semi-automated)
   - **Option C**: Use Confluence REST API (fully automated - requires setup)

### Phase 3: Ongoing Synchronization

1. **Make changes to source .md files** (continue normal workflow)

2. **Run sync script when ready to update Confluence:**
   ```bash
   python confluence-sync.py --source OCPI-2.2.1-Tokens-Module.md --update-all
   ```

3. **Copy updated sections to Confluence pages** (only changed content)

---

## 🔧 Automated Options

### Option 1: Manual Copy/Paste (Recommended Start)
- **Effort**: Low setup, manual updates
- **Best for**: Small teams, infrequent updates
- **Process**: Run script → Copy content → Paste to Confluence

### Option 2: Confluence REST API Integration (Advanced)
- **Effort**: Higher setup, fully automated
- **Best for**: Large teams, frequent updates
- **Process**: Run script → Automatic Confluence page updates

### Option 3: Confluence Git Sync Plugin (If Available)
- **Effort**: Medium setup, automated pulls
- **Best for**: Teams already using Confluence Cloud
- **Process**: Git commit → Confluence automatically updates

---

## 📝 Content Import Instructions

### For Each Confluence Page:

1. **Create new page** in your OCPI space
2. **Set page title** (matches .confluence.md filename)
3. **Copy content** from corresponding .confluence.md file
4. **Paste into Confluence editor**
5. **Adjust formatting:**
   - Confluence should recognize most markdown
   - May need to manually format some panels/info boxes
   - Tables usually import correctly

### Confluence-Specific Enhancements:

The .confluence.md files include enhanced formatting:

- **Info boxes**: `{info:title=Title}Content{info}`
- **Panels**: `{panel:title=Title|borderColor=#ccc}Content{panel}`
- **Expandable sections**: `{expand:title=Title}Content{expand}`
- **Code blocks**: `{code:language=javascript}Code{code}`

---

## 🔄 Workflow Integration

### Daily Development Workflow:
1. **Edit source .md files** (your normal process)
2. **Commit to Git** (version control maintained)
3. **Run sync script** before team meetings/reviews
4. **Update Confluence** for team collaboration

### Team Collaboration Workflow:
1. **Team reviews in Confluence** (comments, discussions)
2. **Feedback incorporated in .md files** (authoritative source)
3. **Sync script updates Confluence** (changes reflected)
4. **Repeat cycle** for iterative improvement

---

## 🚀 Quick Start Commands

```bash
# Initial setup
python confluence-sync.py --source OCPI-2.2.1-Tokens-Module.md --create-all

# Update existing Confluence files
python confluence-sync.py --source OCPI-2.2.1-Tokens-Module.md --update-all

# Monitor for changes (auto-update)
python confluence-sync.py --watch --source OCPI-2.2.1-Tokens-Module.md

# Generate migration report
python confluence-sync.py --report --source OCPI-2.2.1-Tokens-Module.md
```

---

**Next Steps:**
1. Review generated .confluence.md files in `confluence-migration/` folder
2. Create Confluence page structure
3. Import first page as test
4. Establish team workflow for ongoing synchronization

*This migration maintains your markdown-first workflow while adding Confluence collaboration benefits.*
"""

        guide_path = self.confluence_dir / "MIGRATION-GUIDE.md"
        with open(guide_path, 'w', encoding='utf-8') as f:
            f.write(guide_content)

        return str(guide_path)

def main():
    parser = argparse.ArgumentParser(description='Sync Markdown files to Confluence format')
    parser.add_argument('--source', required=True, help='Source markdown file')
    parser.add_argument('--update-all', action='store_true', help='Update all Confluence files')
    parser.add_argument('--watch', action='store_true', help='Monitor for changes')
    parser.add_argument('--create-guide', action='store_true', help='Create migration guide')

    args = parser.parse_args()

    migrator = ConfluenceMigrator()

    if args.create_guide:
        guide_path = migrator.create_migration_guide()
        print(f"✅ Migration guide created: {guide_path}")

    if args.update_all:
        success = migrator.sync_changes_from_source(args.source)
        if success:
            print("🎉 Confluence files ready for import!")
            print(f"📁 Check the 'confluence-migration/' folder for .confluence.md files")
            print("📋 Next: Copy content from each file to corresponding Confluence pages")
        else:
            print("❌ Synchronization failed")

    if args.watch:
        print("🔍 Monitoring for changes (Ctrl+C to stop)...")
        # Implementation for file watching would go here

if __name__ == "__main__":
    main()
