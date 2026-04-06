from pathlib import Path
import re


SUSPICIOUS_KEYWORDS = [
    "/OpenAction",
    "/AA",
    "/JS",
    "/JavaScript",
    "/Launch",
    "/EmbeddedFiles",
]


def read_text_file(path: str) -> str:
    """
    Read a text file safely with UTF-8 fallback behavior.
    """
    return Path(path).read_text(encoding="utf-8", errors="ignore")


def find_suspicious_keywords(report_text: str) -> dict:
    """
    Count suspicious PDF-related keywords inside a text report.
    """
    findings = {}
    for keyword in SUSPICIOUS_KEYWORDS:
        findings[keyword] = report_text.count(keyword)
    return findings


def extract_object_block(raw_text: str, object_number: int) -> str:
    """
    Extract a simple object block from peepdf-style text output if present.
    This is a lightweight text-based parser for report files.
    """
    pattern = rf"object {object_number}(.*?)(?=object \d+|$)"
    match = re.search(pattern, raw_text, re.DOTALL | re.IGNORECASE)
    return match.group(0).strip() if match else ""


def summarize_report(report_path: str) -> dict:
    """
    Build a small summary from the report text.
    """
    text = read_text_file(report_path)
    findings = find_suspicious_keywords(text)

    return {
        "report_path": report_path,
        "suspicious_keywords": findings,
        "object_9_present": "object 9" in text.lower(),
        "object_10_present": "object 10" in text.lower(),
    }


if __name__ == "__main__":
    report = "reports/peepdf_report.txt"
    summary = summarize_report(report)
    print(summary)
