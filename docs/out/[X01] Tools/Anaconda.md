<link rel="stylesheet" href="../stylesheet.css">

# Anaconda

## Setup
<u-b>1. CREATE ENV</u-b>
```sh
$ conda create --name <env_name> python=3.8
```

<u-b>2. ACTIVATE</u-b>
```sh
$ conda activate <env_name>
```

<u-b>3. INIT SHELL</u-b>
> It sets up the shell configuration files to include conda's functionality, making it easier to use conda commands directly in your command prompt or terminal.
```sh
$ conda init 
```

<u-b>4. INSTALL PKG</u-b>
```sh
$ conda install <pkg>
```

<u-b>5. DEL ENV</u-b>
```sh
$ conda env remove --name <env_name>
```
 
## Extras
<u-b>UPDATE CONDA</u-b>
```sh
conda update -n base -c defaults conda
```