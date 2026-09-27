# ==============================================================================
# NYSC CDS Reports - Automated Generator & Builder
# Compiles HTML reports from _sources into high-resolution PDFs in this folder.
# ==============================================================================

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourcesDir = Join-Path $scriptDir "_sources"

function Convert-HtmlToPdf($htmlFile, $pdfFile) {
    if (-not (Test-Path $chromePath)) {
        Write-Warning "Google Chrome not found. Cannot auto-compile PDF. You can open HTML in browser and Print -> Save as PDF."
        return
    }
    $fullHtml = [System.IO.Path]::GetFullPath($htmlFile)
    $fullPdf = [System.IO.Path]::GetFullPath($pdfFile)
    
    Write-Host "Rendering: $(Split-Path $pdfFile -Leaf)..."
    $proc = Start-Process -FilePath $chromePath -ArgumentList "--headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=`"$fullPdf`" `"file:///$fullHtml`"" -Wait -PassThru
    if ($proc.ExitCode -eq 0) {
        Write-Host " [OK] Successfully generated: $(Split-Path $pdfFile -Leaf)" -ForegroundColor Green
    } else {
        Write-Error "Failed to generate $(Split-Path $pdfFile -Leaf)"
    }
}

Write-Host "=== Compiling NYSC Digital Literacy CDS Reports ===" -ForegroundColor Cyan
Convert-HtmlToPdf "$sourcesDir\DLC THIRD QUARTER REPORT 2026.html" "$scriptDir\DLC THIRD QUARTER REPORT 2026.pdf"
Convert-HtmlToPdf "$sourcesDir\DLC KPI THIRD QUARTER REPORT 26.html" "$scriptDir\DLC KPI THIRD QUARTER REPORT 26.pdf"

Write-Host "`n=== Compiling NYSC Environmental CDS Reports ===" -ForegroundColor Cyan
Convert-HtmlToPdf "$sourcesDir\ENVIRONMENTAL CDS THIRD QUARTER REPORT 2026.html" "$scriptDir\ENVIRONMENTAL CDS THIRD QUARTER REPORT 2026.pdf"
Convert-HtmlToPdf "$sourcesDir\ENVIRONMENTAL CDS KPI THIRD QUARTER REPORT 26.html" "$scriptDir\ENVIRONMENTAL CDS KPI THIRD QUARTER REPORT 26.pdf"

Write-Host "`nAll reports compiled successfully!" -ForegroundColor Green