import os
import subprocess

from conda.plugins import CondaVirtualPackage, hookimpl


@hookimpl
def conda_virtual_packages():
    # openmpi virtual package
    openmpi_version = None
    if "CONDA_OVERRIDE_OPENMPI" in os.environ:
        openmpi_version = os.environ["CONDA_OVERRIDE_OPENMPI"]
    else:
        try:
            ret = subprocess.run(
                ["ompi_info", "--parsable"], capture_output=True, text=True
            )
            if ret.returncode == 0:
                for line in ret.stdout.splitlines():
                    if line.startswith("ompi:version:full:"):
                        openmpi_version = line.strip().split(":")[3]
                        break
        except Exception:
            pass

    if openmpi_version:
        yield CondaVirtualPackage(
            name="openmpi",
            version=openmpi_version,
            build=None,
        )
