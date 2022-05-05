# Installation

This doc provides instructions to get started.

## Install CARLA
* Install [git lfs](https://git-lfs.github.com/).
* Download this repo `git clone --recurse-submodules git@github.com:dotchen/LAV.git`
* Download and unzip [CARLA 0.9.10.1](https://github.com/carla-simulator/carla/releases/tag/0.9.10.1)

## Install dependencies
* First, inside the repo, create a dedicated conda environment. Refer [here](https://www.anaconda.com/products/individual#Downloads) if you do not have conda.
```
conda env create -f environment.yaml
```
* Inside the conda environment, install the CARLA PythonAPI `easy_install [PATH TO CARLA EGG]`. Refer to [this link](https://leaderboard.carla.org/get_started/) if you are confused at this step.
* `conda install pytorch-scatter -c pyg`

## Configure environment variables

In your conda env set the following in [conda env source]/etc/conda/activate.d/env_vars.sh
```bash
#!/bin/bash

export CARLA_ROOT=/home/anthony/softwares/CARLA_0.9.10
export LEADERBOARD_ROOT=/home/anthony/other_githubs/LAV/leaderboard
export SCENARIO_RUNNER_ROOT=/home/anthony/other_githubs/LAV/scenario_runner
export CARLA_AGENTS_ROOT=/home/anthony/other_githubs/LAV/carla_agents
export CARLA_API="${CARLA_ROOT}/PythonAPI/carla/"
export PYTHONPATH="${CARLA_API}":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}":"${CARLA_AGENTS_ROOT}"
export TEAM_AGENT=/home/anthony/other_githubs/LAV/team_code/lav_agent.py
export TEAM_CONFIG=/home/anthony/other_githubs/LAV/team_code/config.yaml
export SCENARIOS=${LEADERBOARD_ROOT}/data/all_towns_traffic_scenarios_public.json
export REPETITIONS=1
export DEBUG_CHALLENGE=0
export CHALLENGE_TRACK_CODENAME=SENSORS
```

Now, you can treat this conda environment the dedicated one (by defauld named `LAV-env`).
