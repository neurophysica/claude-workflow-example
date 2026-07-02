"""Tests for the unitconv command-line interface."""

import subprocess
import sys

from unitconv.__main__ import main


def test_main_prints(capsys):
    rc = main(["10", "km", "mi"])
    out = capsys.readouterr().out.strip()
    assert rc == 0
    assert out == "6.21371 mi"


def test_cli_module_runs():
    proc = subprocess.run(
        [sys.executable, "-m", "unitconv", "1", "m", "cm"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0
    assert proc.stdout.strip() == "100 cm"
