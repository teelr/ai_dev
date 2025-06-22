# 🧪 Conda Command Cheat Sheet

This cheat sheet covers essential Conda commands for managing environments, packages, and configurations.

---

## 🟢 Environment Management

| Task                         | Command                                      |
|------------------------------|----------------------------------------------|
| Create a new environment     | `conda create -n myenv python=3.10`         |
| Activate an environment      | `conda activate myenv`                      |
| Deactivate current environment | `conda deactivate`                        |
| Remove an environment        | `conda env remove -n myenv`                |
| Clone an environment         | `conda create --name newenv --clone oldenv` |
| List all environments        | `conda env list` or `conda info --envs`    |

## 🟡 Package Management

| Task                         | Command                                    |
|------------------------------|--------------------------------------------|
| Install a package            | `conda install numpy`                      |
| Install from specific channel| `conda install -c conda-forge numpy`       |
| Install from .yml file       | `conda env create -f environment.yml`      |
| Export environment to .yml   | `conda env export > environment.yml`       |
| Update a package             | `conda update numpy`                       |
| Update Conda itself          | `conda update conda`                       |
| Remove a package             | `conda remove numpy`                       |
| List installed packages      | `conda list`                               |

## 🔵 Search & Info

| Task                         | Command                                     |
|------------------------------|---------------------------------------------|
| Search for a package         | `conda search numpy`                        |
| Show package info            | `conda show numpy`                          |

## 🔴 Environment Export Options

| Task                         | Command                                     |
|------------------------------|---------------------------------------------|
| Export explicit specs        | `conda list --explicit > spec.txt`          |
| Create env from spec file    | `conda create --name myenv --file spec.txt` |

## ⚙️ Configuration & Cleanup

| Task                         | Command                                     |
|------------------------------|---------------------------------------------|
| View current config          | `conda config --show`                       |
| Add default channel          | `conda config --add channels conda-forge`   |
| Clean unused packages/cache  | `conda clean --all`                         |
