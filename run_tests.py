import sys

import subprocess
from dotenv import load_dotenv

from config import ENVS_ROOT


def run_tests(platform: str):
    env_file = ENVS_ROOT / f"{platform}.env"

    if not env_file.exists():
        print(f"Error: Environment file for {platform} not found.")
        sys.exit(1)

    load_dotenv(env_file)
    subprocess.run(["pytest", "tests"], check=True)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"android", "ios"}:
        print("Usage: python run_tests.py <android|ios>")
        sys.exit(1)

    run_tests(sys.argv[1])
