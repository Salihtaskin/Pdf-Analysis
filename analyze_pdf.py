import hashlib
import os
import subprocess

PDF_PATH = "samples/evil.pdf"
PAYLOAD_PATH = "extracted/template_payload.bin"

def sha256sum(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def run_command(cmd: list[str], output_file: str) -> None:
    with open(output_file, "w", encoding="utf-8") as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, text=True)

def main() -> None:
    os.makedirs("reports", exist_ok=True)

    print("[+] PDF SHA256:", sha256sum(PDF_PATH))

    run_command(
        ["python2", os.path.expanduser("~/.msf4/local/peepdf/peepdf.py"), PDF_PATH],
        "reports/peepdf_report.txt",
    )

    run_command(
        ["strings", PAYLOAD_PATH],
        "reports/payload_strings.txt",
    )

    run_command(
        ["file", PAYLOAD_PATH],
        "reports/payload_filetype.txt",
    )

    with open("reports/hashes.txt", "w", encoding="utf-8") as f:
        f.write(f"{PDF_PATH} SHA256: {sha256sum(PDF_PATH)}\n")
        f.write(f"{PAYLOAD_PATH} SHA256: {sha256sum(PAYLOAD_PATH)}\n")

    print("[+] Analysis reports generated under reports/")

if __name__ == "__main__":
    main()
