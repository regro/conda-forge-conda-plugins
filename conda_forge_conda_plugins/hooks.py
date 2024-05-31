import logging
import os
import shutil
import subprocess

from conda.base.context import context
from conda.core.envs_manager import list_all_known_prefixes
from conda.plugins import CondaVirtualPackage, hookimpl

logger = logging.getLogger(__name__)


def _real_abs_path(path):
    if path is None:
        return None
    return os.path.realpath(os.path.abspath(path))


def _find_command_not_in_a_conda_prefix(cmd):
    pth = _real_abs_path(shutil.which(cmd))

    if (
        pth is None
        or pth.startswith(_real_abs_path(context.root_prefix))
        or pth.startswith(
            tuple(_real_abs_path(_pth) for _pth in list_all_known_prefixes())
        )
    ):
        return None

    return pth


@hookimpl
def conda_virtual_packages():
    # openmpi virtual package
    openmpi_version = None
    if "CONDA_OVERRIDE_OPENMPI" in os.environ:
        openmpi_version = os.environ["CONDA_OVERRIDE_OPENMPI"]
    else:
        try:
            ompi_info_pth = _find_command_not_in_a_conda_prefix("ompi_info")
            if ompi_info_pth is not None:
                ret = subprocess.run(
                    [ompi_info_pth, "--parsable"], capture_output=True, text=True
                )
                if ret.returncode == 0:
                    for line in ret.stdout.splitlines():
                        if line.startswith("ompi:version:full:"):
                            openmpi_version = line.strip().split(":")[3].strip()
                            break
        except Exception as e:
            logger.error(f"Error while trying to find openmpi version: {e}", exc_info=e)
            pass

    if openmpi_version:
        yield CondaVirtualPackage(
            name="openmpi",
            version=openmpi_version,
            build=None,
        )

    # mpich virtual package
    mpich_version = None
    if "CONDA_OVERRIDE_MPICH" in os.environ:
        mpich_version = os.environ["CONDA_OVERRIDE_MPICH"]
    else:
        try:
            mpichversion_pth = _find_command_not_in_a_conda_prefix("mpichversion")
            if mpichversion_pth is not None:
                ret = subprocess.run(
                    [mpichversion_pth, "--version"], capture_output=True, text=True
                )
                if ret.returncode == 0:
                    for line in ret.stdout.splitlines():
                        if line.startswith("MPICH Version:"):
                            mpich_version = line.strip().split(":")[1].strip()
                            break
        except Exception as e:
            logger.error(f"Error while trying to find openmpi version: {e}", exc_info=e)
            pass

    if mpich_version:
        yield CondaVirtualPackage(
            name="mpich",
            version=mpich_version,
            build=None,
        )
