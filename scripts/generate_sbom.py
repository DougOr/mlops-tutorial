import subprocess
import shutil
import sys

# Check if syft is installed
if not shutil.which("syft"):
    print("Error: syft is not installed. Please install syft to generate SBOM.")
    print("Installation instructions: https://github.com/anchore/syft")
    sys.exit(1)

# Generate SBOM for the project directory
try:
    subprocess.run(
        ["syft", ".", "--output", "spdx-json=sbom.json"],  # Analyze the current directory
        check=True
    )
    print("SBOM generated successfully as sbom.json")
except subprocess.CalledProcessError as e:
    print(f"Error generating SBOM: {e}")
    sys.exit(1)
