# NYSC CDS Quarterly Reports (Q3 2026) & Reusable Generator

This repository contains the official, verified quarterly reports and Key Performance Indicator (KPI) documentation for the National Youth Service Corps (NYSC) CDS groups in **Obudu LGA, Cross River State (Zone: Obudu / Ogoja)**.

Included are source files, editable documents, templates, rules, and compilers for both:
1. **Digital Literacy CDS Group (DLC)**
2. **Environmental Protection & Sanitation CDS Group**

All report structures strictly adhere to official NYSC directorate standards: high-resolution headers, balanced single-page landscape table formatting, embedded photo evidence galleries, and authenticated Schedule Officer / State Coordinator sign-offs.

---

## 🤖 For AI Agents & Contributors: How to Recreate PDF Deliverables

To keep this repository clean, lightweight, and diff-friendly, compiled binary PDFs are gitignored. All master HTML sources and high-resolution assets are fully maintained in `_sources/`.

Any agent, CI environment, or human can instantly recreate all 4 publication-ready PDFs using any of the following methods:

### Option 1: PowerShell (Windows)
```powershell
powershell -ExecutionPolicy Bypass -File .\Generate-Reports.ps1
```

### Option 2: Python (Cross-Platform: Windows / Linux / macOS)
```bash
python generate_reports.py
```
*(Automatically locates Chrome, Chromium, or Microsoft Edge)*

### Option 3: Manual Headless Chrome Command
```bash
chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf="DLC THIRD QUARTER REPORT 2026.pdf" "file:///full/path/to/_sources/DLC THIRD QUARTER REPORT 2026.html"
```

---

## 📌 Deliverables & File Structure

### 1. Digital Literacy CDS Group (DLC)
* 📄 **`DLC THIRD QUARTER REPORT 2026.pdf`** *(Recreatable)* — Official 1-page landscape quarterly report table (Month 1: 40 beneficiaries, Month 2: 22, Month 3: 110; Grand Total: 172). Master: `_sources/DLC THIRD QUARTER REPORT 2026.html`.
* 📝 [**`DLC THIRD QUARTER REPORT 2026.doc`**](DLC%20THIRD%20QUARTER%20REPORT%202026.doc) — Editable Microsoft Word document with embedded logos.
* 📊 **`DLC KPI THIRD QUARTER REPORT 26.pdf`** *(Recreatable)* — Comprehensive 5-page submission pack (Cover page, KPI performance matrix, and 3 monthly photo galleries for July, August, and September). Master: `_sources/DLC KPI THIRD QUARTER REPORT 26.html`.
* 📝 [**`DLC KPI THIRD QUARTER REPORT 26.doc`**](DLC%20KPI%20THIRD%20QUARTER%20REPORT%2026.doc) — Editable Microsoft Word document for the KPI report.

### 2. Environmental Protection & Sanitation CDS Group
* 📄 **`ENVIRONMENTAL CDS THIRD QUARTER REPORT 2026.pdf`** *(Recreatable)* — Official 1-page landscape quarterly report table (July: 55, August: `-`, Sept: 35; Grand Total: 90; Donated: *Baskets, Brooms, Packers and Mop*). Master: `_sources/ENVIRONMENTAL CDS THIRD QUARTER REPORT 2026.html`.
* 📝 [**`ENVIRONMENTAL CDS THIRD QUARTER REPORT 2026.doc`**](ENVIRONMENTAL%20CDS%20THIRD%20QUARTER%20REPORT%202026.doc) — Editable Microsoft Word document.
* 📊 **`ENVIRONMENTAL CDS KPI THIRD QUARTER REPORT 26.pdf`** *(Recreatable)* — Comprehensive 4-page submission pack (Cover page, KPI performance matrix, and monthly photo galleries for July and September; August marked `-`). Master: `_sources/ENVIRONMENTAL CDS KPI THIRD QUARTER REPORT 26.html`.
* 📝 [**`ENVIRONMENTAL CDS KPI THIRD QUARTER REPORT 26.doc`**](ENVIRONMENTAL%20CDS%20KPI%20THIRD%20QUARTER%20REPORT%2026.doc) — Editable Microsoft Word document for the KPI report.

### 3. Automation Scripts & Templates
* ⚙️ [**`Generate-Reports.ps1`**](Generate-Reports.ps1): Automated PowerShell script for local Chrome PDF compilation.
* 🐍 [**`generate_reports.py`**](generate_reports.py): Cross-platform Python generator script for automated pipelines.
* 📐 [**`templates/`**](templates/): Generic, parameterized HTML templates for Quarterly and KPI reports reusable for any NYSC CDS group or quarter.
* 📜 [**`RULES.md`**](RULES.md): Official repo standards, compliance rules (uniform footwear cropping, aggregated beneficiaries, inactive months, layout integrity).
* 🗃️ **`_sources/`**: Master HTML files, embedded high-resolution graphics, and official NYSC crests.

---

## 📊 Summary of Q3 2026 CDS Data

### A. Digital Literacy CDS Group
| Month | Activity / Focus | Location | C/Ms | Male | Female | Total | Donated Items |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **July 2026** | E-learning navigation & mobile educational tools | St. Joseph's Vicinity, Obudu | 2 | 20 | 20 | 40 | NIL |
| **August 2026** | New champions training & public sector advocacy | Obudu Urban Dev. Authority (OUDA) | 11 | 11 | 11 | 22 | NIL |
| **Sept 2026** | Trader financial inclusion & mobile scam avoidance | Obudu Main Market | 11 | 44 | 66 | 110 | NIL |
| **Total** | | | | **75** | **97** | **172** | **NIL** |

### B. Environmental Protection & Sanitation CDS Group
| Month | Activity / Focus | Location | C/Ms | Male | Female | Total | Donated Items |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **July 2026** | Street sweeping, refuse disposal & hygiene sensitization | Ogoja Road, Obudu | 11 | 30 | 25 | 55 | NIL |
| **August 2026** | *Recess / Inactive Month* | - | - | - | - | - | - |
| **Sept 2026** | School waste management & hygiene outreach | Handmaids Int'l Nursery/Primary School | 3 | 15 | 20 | 35 | Baskets, Brooms, Packers and Mop |
| **Total** | | | | **45** | **45** | **90** | **Baskets, Brooms, Packers and Mop** |

---

## ✍️ Official Sign-Off Information
* **Schedule Officer:** `OKO JOHN`
* **State Coordinator:** `OYENUGA MUJISOLA JOKE`
* **Official Date:** `24/9/2026`

---

## 📋 Core Submission Rules & Guidelines

Detailed operational guidelines are in [`RULES.md`](RULES.md). Key highlights:
1. **Uniform & Footwear Compliance:** Non-regulation footwear (e.g. white sneakers) worn with khakis must be cropped out of all official gallery photographs while preserving GPS timestamp overlays.
2. **Aggregated Numbers:** Internal meeting schedules (e.g. "2 CDS days") are never mentioned in narrative texts; all metrics are published as consolidated monthly totals.
3. **Inactive Month Standard:** Months with no activities use a single dash (`-`) across all row cells and omit gallery pages.
4. **Single-Page Table Format:** Quarterly report tables strictly fit on one landscape page without text wrapping mid-word.