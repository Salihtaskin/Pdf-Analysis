import argparse
import sys

from src.utils.config import load_json_config, get_env_config
from src.core.analyzer import PDFAnalyzer
from src.core.reporter import ReportWriter


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="PDF malware triage and forensic analysis tool"
    )
    parser.add_argument(
        "--pdf",
        required=True,
        help="Path to target PDF file"
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output directory for reports"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()

    try:
        json_config = load_json_config()
        env_config = get_env_config()

        output_dir = args.output or env_config["DEFAULT_OUTPUT_DIR"]

        analyzer = PDFAnalyzer(env_config, json_config)
        reporter = ReportWriter(json_config)

        result = analyzer.analyze(args.pdf)
        reporter.write_reports(result, output_dir)

        enriched = reporter.enrich_result(result)

        print("[+] Analysis completed successfully")
        print(f"[+] File: {enriched['file_name']}")
        print(f"[+] SHA256: {enriched['sha256']}")
        print(f"[+] Risk Score: {enriched['risk_assessment']['score']}/100")
        print(f"[+] Verdict: {enriched['risk_assessment']['verdict']}")
        print(f"[+] Reports saved to: {output_dir}")

        return 0

    except FileNotFoundError as exc:
        print(f"[-] {exc}")
        return 1
    except Exception as exc:
        print(f"[-] Unexpected error: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
