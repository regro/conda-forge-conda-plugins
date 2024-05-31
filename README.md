# conda-forge-conda-plugins
[![tests](https://github.com/regro/conda-forge-conda-plugins/actions/workflows/tests.yml/badge.svg)](https://github.com/regro/conda-forge-conda-plugins/actions/workflows/tests.yml) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/regro/conda-forge-conda-plugins/main.svg)](https://results.pre-commit.ci/latest/github/regro/conda-forge-conda-plugins/main)

conda plugins for the `conda-forge` ecosystem

## Current Plugins

### OpenMPI Virtual Package

This plugin provides the `__openmpi` virtual package to be used in conjunction with the `external*` builds of the `conda-forge` `openmpi` package. If the `ompi_info` command is found in the path, the `__openmpi` virtual package is set to the installed version of OpenMPI. You can override the version by setting the `CONDA_OVERRIDE_OPENMPI` environment variable.
