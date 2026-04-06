import subprocess
from typing import Tuple


def run_command(command: list[str], timeout: int = 20) -> Tuple[int, str, str]:
    """
    Run a system command safely and return (returncode, stdout, stderr).
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"Command timed out after {timeout} seconds"
    except FileNotFoundError:
        return 127, "", f"Command not found: {command[0]}"
    except Exception as exc:
        return 1, "", f"Unexpected error: {exc}"
