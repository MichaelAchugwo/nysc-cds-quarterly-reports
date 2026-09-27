# NYSC CDS Report Templates & Reusability Guide

This directory provides standardized HTML templates for generating official National Youth Service Corps (NYSC) Community Development Service (CDS) Quarterly and Key Performance Indicator (KPI) reports.

---

## 📁 Available Templates

1. **`quarterly-report-template.html`**
   - **Page Orientation:** Landscape (Single Page Letter).
   - **Usage:** Standard official 1-page quarterly submission table.
   - **Features:** Balanced column widths (no split headers), dual-logo support (NYSC crest + optional project/partner crest), formatted metadata row, and schedule officer sign-off line.

2. **`kpi-report-template.html`**
   - **Page Orientation:** Landscape (Multi-Page Letter with Cover Page & Photo Gallery).
   - **Usage:** Comprehensive monthly performance matrix and high-resolution photo evidence gallery.
   - **Features:**
     - Page 1: Official cover page with dual-signatory blocks (Schedule Officer & State Coordinator).
     - Page 2: KPI matrix table with gender breakdown (Male/Female/Total), activity descriptions, and item donations.
     - Page 3+: 2-column responsive photo evidence galleries per active month.

---

## 🛠️ Placeholder Variables Reference

### Quarterly Report Template
| Placeholder | Description | Example |
| :--- | :--- | :--- |
| `{{REPORT_TITLE}}` | Browser/PDF Document Title | `DLC THIRD QUARTER REPORT 2026` |
| `{{GROUP_NAME_UPPER}}` | Official CDS Group Name | `DIGITAL LITERACY CDS GROUP` |
| `{{OPTIONAL_RIGHT_LOGO}}`| Partner / Initiative Logo Tag | `<img src="../_sources/dl4all_logo.jpg" class="header-logo-right">` |
| `{{STATE}}` | State of Deployment | `CROSS RIVER` |
| `{{ZONE}}` | Administrative Zone | `OBUDU` |
| `{{QUARTER}}` | Current Quarter | `3RD QUARTER` |
| `{{YEAR}}` | Report Year | `2026` |
| `{{TABLE_ROWS}}` | `<tr>` blocks for each month | See `_sources/*.html` for examples |
| `{{SCHEDULE_OFFICER}}` | CDS Schedule Officer Name | `OKO JOHN` |
| `{{SIGN_DATE}}` | Submission / Sign-off Date | `24/9/2026` |

### KPI Report Template
| Placeholder | Description | Example |
| :--- | :--- | :--- |
| `{{QUARTER_TITLE}}` | Centered Cover Page Title | `3RD QUARTER CDS KEY PERFORMANCE INDICATOR REPORT, 2026` |
| `{{LGA_STATE_UPPER}}` | LGA and State designation | `OBUDU L.G.A, CROSS RIVER` |
| `{{STATE_COORDINATOR}}`| NYSC State Coordinator Name | `OYENUGA MUJISOLA JOKE` |
| `{{QUARTER_SHORT}}` | Short quarter identifier | `Q3 2026` |
| `{{TOTAL_MALE}}` | Sum of male beneficiaries | `75` |
| `{{TOTAL_FEMALE}}` | Sum of female beneficiaries | `97` |
| `{{TOTAL_BENEFICIARIES}}`| Grand total beneficiaries | `172` |
| `{{TOTAL_DONATIONS}}` | Summary of all donated items | `NIL` or `Baskets, Brooms, Packers and Mop` |
| `{{GALLERY_PAGES}}` | `<div class="page">` gallery cards | Structured 2-card photographic layout |

---

## 🚀 How to Compile to PDF

Use `Generate-Reports.ps1` at the root of this project:
```powershell
powershell -ExecutionPolicy Bypass -File .\Generate-Reports.ps1
```
This automatically invokes Google Chrome in headless mode:
`--headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf="output.pdf" "input.html"`
