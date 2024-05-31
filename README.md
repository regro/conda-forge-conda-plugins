# conda-forge-conda-plugins

conda plugins for the `conda-forge` ecosystem

## Current Plugins

### OpenMPI Virtual Package

This plugin provides the `__openmpi` virtual package to be used in conjunction with the `external*` builds of the `conda-forge` `openmpi` package. If the `ompi_info` command is found in the path, the `__openmpi` virtual package is set to the installed version of OpenMPI. You can override the version by setting the `CONDA_OVERRIDE_OPENMPI` environment variable.
