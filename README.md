# Using the Central Spack Instance on RCC Midway3

**Spack Root (Midway3):** `/software/sw/spack-mw3/`
**Maintainer (Midway3 Spack Instance):** Parmanand Sinha


## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started: Accessing Spack](#getting-started-accessing-spack)
3. [Basic Usage of Spack](#basic-usage-of-spack)
4. [Key Configuration Details (Midway3 Spack)](#key-configuration-details-midway3-spack)
5. [Best Practices on Midway3](#best-practices-on-midway3)
6. [Troubleshooting](#troubleshooting)
7. [Contributing / Requesting Software](#contributing--requesting-software)
8. [Further Reading & References](#further-reading--references)
9. [Future Directions: CI/CD and Automation](#future-directions-cicd-and-automation)

---

## 1. Introduction

### What is Spack?
Spack is a flexible, powerful package manager designed for HPC, enabling the installation and management of multiple software versions and configurations. It simplifies handling compilers, dependencies, and build variations.

### The Midway3 Central Spack Instance
RCC Midway3 provides a centrally managed Spack instance, maintained by Parmanand Sinha. This instance offers curated software packages, consistent configurations, integration with Lmod, and custom packages tailored for RCC. This documentation focuses on *using* this central instance for software management and module loading.

### Loading Spack-based Modules
Users can load Spack-based environment modules using the `spack.modules` modulefile:

```bash
ml show spack.modules
```

This modulefile (`/software/modulefiles/spack.modules`) adds the Spack-generated modulefiles directory to your `MODULEPATH` and initializes the environment modules system. The relevant excerpt from the modulefile:

```tcl
#%Module1.0#########################################################
## spack.module modulefile
proc ModulesHelp { } {
    global rkoversion
    puts stderr "\tThis module file will add spack generated modules to the"
    puts stderr "\tlist of directories that the module command will search"
    puts stderr "\tfor modules.  Place your own module files here."
    puts stderr "\tThis module, when loaded, will create this directory"
    puts stderr "\tif necessary."
    puts stderr "\n\tVersion $rkoversion\n"
}
module-whatis   "adds spack modulefiles directory to MODULEPATH"
set     rkoversion      3.2.7
source-sh bash /software/envmodule-4.7.1-el8-x86_64/init/bash
set     spackmoddir       /software/sw/spack-mw3/modulefiles
module use --prepend $spackmoddir
```

> **Note:** Loading `spack.modules` overrides the centrally available Environment Modules version **4.6.1** on Midway3 with version **4.7.1**. This does not require root privileges and can be done by any user. For a detailed comparison of module versions, see the [Environment Modules releases](https://github.com/envmodules/modules/releases/).

#### Advantages of Environment Modules 4.7.1
- **Hidden Modules:** Version 4.7.1 supports hidden modules, allowing users to hide deprecated or internal modules from standard `module avail` listings, reducing clutter and confusion.
- **Improved Features:** Enhanced error messages, better TCL support, and more flexible modulepath management.

#### Module System Structure
- The current module system is **flat** (no hierarchy); all modules are in a single directory.
- Future upgrades to the module system and modulefile generator can enable hierarchical module layouts, which help organize modules by compiler, MPI, or other criteria for large software stacks.

- **Configuration Files:** `/software/sw/spack-mw3/etc/spack/`
- **Custom Spack Packages:** `/software/sw/spack-mw3/local/midway3`
- **Shared Spack Environments:** `/software/sw/shared/spackenv`
- **User-Specific Caches:** `/scratch/midway3/$USER/`
- **Job-Specific Build Stage:** `$TMPDIR/spack-stage` (within Slurm jobs)

---

## 2. Getting Started: Accessing Spack

### Prerequisites
- RCC Midway3 account

### Loading the Midway3 Spack Environment
To use Spack interactively or in scripts:
```bash
source /software/sw/spack-mw3/share/spack/setup-env.sh
# OR, if an RCC module exists:
# module load spack-mw3
```

user facing modules are available via `module avail spack.modules`

### Verifying the Setup
- **Spack:**
  ```bash
  which spack
  spack --version
  spack config get config:install_tree:root
  # Should be /software/sw/spack-mw3/apps
  ```

### Important Spack Configuration Note (`SPACK_DISABLE_LOCAL_CONFIG`)
The central Midway3 Spack instance uses `SPACK_DISABLE_LOCAL_CONFIG=true`. Your personal configs in `~/.spack/` are ignored, ensuring consistency via central settings.

---

## 3. Basic Usage of Spack
- **Finding Packages:** `spack find` or `spack info <package>`
- **Loading Packages:** `spack load <package>` or use modules via Lmod
- **Viewing Installed Packages:** `spack find`
- **Using Spack Aliases:** (e.g., `spktv`, `concre`, `rm`) as defined by admin

---

## 4. Key Configuration Details (Midway3 Spack)

### Key Locations for Midway3 Spack
- **Spack Installation Root (`SPACK_ROOT`):** `/software/sw/spack-mw3/`
- **Installed Software:** `/software/sw/spack-mw3/apps`
- **Environment Modulefiles:** `/software/sw/spack-mw3/modulefiles`

### Loading Spack-based Modules
Users can load Spack-based environment modules using the `spack.modules` modulefile:

```bash
ml avail spack.modules
ml load spack.modules
```

This modulefile (`/software/modulefiles/spack.modules`) adds the Spack-generated modulefiles directory to your `MODULEPATH` and initializes the environment modules system. The relevant excerpt from the modulefile:

```tcl
#%Module1.0#########################################################
## spack.module modulefile
proc ModulesHelp { } {
    global rkoversion
    puts stderr "\tThis module file will add spack generated modules to the"
    puts stderr "\tlist of directories that the module command will search"
    puts stderr "\tfor modules.  Place your own module files here."
    puts stderr "\tThis module, when loaded, will create this directory"
    puts stderr "\tif necessary."
    puts stderr "\n\tVersion $rkoversion\n"
}
module-whatis   "adds spack modulefiles directory to MODULEPATH"
set     rkoversion      3.2.7
source-sh bash /software/envmodule-4.7.1-el8-x86_64/init/bash
set     spackmoddir       /software/sw/spack-mw3/modulefiles
module use --prepend $spackmoddir
```

> **Note:** Loading `spack.modules` overrides the centrally available Environment Modules version **4.6.1** on Midway3 with version **4.7.1**. This does not require root privileges and can be done by any user. For a detailed comparison of module versions, see the [Environment Modules releases](https://github.com/envmodules/modules/releases/).

#### Advantages of Environment Modules 4.7.1
- **Hidden Modules:** Version 4.7.1 supports hidden modules, allowing users to hide deprecated or internal modules from standard `module avail` listings, reducing clutter and confusion.
- **Improved Features:** Enhanced error messages, better TCL support, and more flexible modulepath management.

#### Module System Structure
- The current module system is **flat** (no hierarchy); all modules are in a single directory.
- Future upgrades to the module system and modulefile generator can enable hierarchical module layouts, which help organize modules by compiler, MPI, or other criteria for large software stacks.

- **Configuration Files:** `/software/sw/spack-mw3/etc/spack/`
- **Custom Spack Packages:** `/software/sw/spack-mw3/local/midway3`
- **Shared Spack Environments:** `/software/sw/shared/spackenv`
- **User-Specific Caches:** `/scratch/midway3/$USER/`
- **Job-Specific Build Stage:** `$TMPDIR/spack-stage` (within Slurm jobs)

---

## 5. Best Practices on Midway3
- Prefer pre-installed Spack packages/modules
- Leverage shared Spack environments
- Use containers for portability/complex dependencies


---

## 6. Troubleshooting

### Spack Issues
- Check logs, environment, permissions, and module conflicts

### GitLab CI/Jacamar Issues
- **Pipeline not starting:** Check `.gitlab-ci.yml` syntax and runner tags
- **Job pending:** Runners may be busy or tags mismatched
- **Job failing:** Check job logs, Jacamar logs, script permissions, and paths

### Container Execution Issues
- **Image not found:** Check image/tag and registry access
- **Errors inside container:** Debug as you would locally, but inside the container context
- **File system/mount issues:** Check Jacamar/Singularity docs for mount points


---


## 7. Further Reading & References
- [ECP CI Initiative](https://ecp-ci.gitlab.io/index.html)
- [ECP CI Tutorials](https://ecp-ci.gitlab.io/docs/tutorial.html)
- [Official Spack Documentation](https://spack.readthedocs.io/)
- [Official GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Singularity/Apptainer Documentation](https://apptainer.org/docs/)

---

### About this Repository
This repo tracks local customizations of Spack YAML files for Midway3. Symbolic links from `$SPACK_ROOT/etc/spack/*.yaml` point to files in `spack_yaml_config/mw3/`.
