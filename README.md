## Note
* To run CARLA and train the models, make sure you are using a machine with **at least** a mid-end GPU.

## Install CARLA
* Install [git lfs](https://git-lfs.github.com/).
* Download this repo and it's submodules
* Download and unzip [CARLA 0.9.10.1](https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.10.1.tar.gz)

## Install dependencies
* First, inside the repo, create a dedicated conda environment. Refer [here](https://www.anaconda.com/products/individual#Downloads) if you do not have conda.
```
conda env create -f environment.yaml
```
* Inside the conda environment, install the carla package `easy_install {CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg`.
* Install pytorch-scatter `conda install pytorch-scatter -c pyg`


## Configure environment variables

In your conda env set the following in [conda env source]/etc/conda/activate.d/env_vars.sh
```bash
#!/bin/bash

export CARLA_ROOT={Path to your CARLA root directory}
export MILE_CODE_ROOT={Path to the root of this repo}
export LEADERBOARD_ROOT=${MILE_CODE_ROOT}/leaderboard
export SCENARIO_RUNNER_ROOT=${MILE_CODE_ROOT}/scenario_runner
export CARLA_API="${CARLA_ROOT}/PythonAPI/carla/"
export PYTHONPATH="${CARLA_API}":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}"
export TEAM_CODE_ROOT=${MILE_CODE_ROOT}/team_code
export TEAM_AGENT=${TEAM_CODE_ROOT}/mile_agent.py
export TEAM_CONFIG=${TEAM_CODE_ROOT}/config.yaml
export SCENARIOS=${LEADERBOARD_ROOT}/data/all_towns_traffic_scenarios_public.json
export REPETITIONS=1
export DEBUG_CHALLENGE=0
export CHALLENGE_TRACK_CODENAME=SENSORS
```
Now, you can treat this conda environment the dedicated one (by defauld named `MILE-env`).


## Docker
1) Build docker container running
```bash
./make_docker.sh
```
2) In a different terminal start the CARLA server
```bash
CUDA_VISIBLE_DEVICES=0 bash $CARLA_ROOT/CarlaUE4.sh -RenderOffScreen -quality-level=Epic -carla-streaming-port=0 -nosound -opengl
```
3) Get into the docker container and run the benchmark
```bash
docker run -it --network=host leaderboard-user:latest # Network=host required to talk to CARLA server running outside docker container
# Once inside the container...
./leaderboard/scripts/run_evaluation.sh
```