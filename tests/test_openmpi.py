import json
import os
import subprocess


def test_openmpi_override():
    env = {"CONDA_OVERRIDE_OPENMPI": "10.0.0"}
    env.update(dict(os.environ))
    ret = subprocess.run(
        ["conda", "info", "--json"],
        capture_output=True,
        text=True,
        env=env,
    )
    assert ret.returncode == 0
    info = json.loads(ret.stdout)
    pkg = None
    for _pkg in info["virtual_pkgs"]:
        if _pkg[0] == "__openmpi":
            pkg = _pkg
            break
    assert pkg is not None, info["virtual_pkgs"]
    assert pkg[1] == "10.0.0", pkg
