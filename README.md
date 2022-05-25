## Setup
* To run CARLA and train the models, make sure you are using a machine with **at least** a mid-end GPU.
* Please follow [INSTALL.md](docs/INSTALL.md) to setup the environment.


## Evaluation
1) Launch carla env `CUDA_VISIBLE_DEVICES=0 bash $CARLA_ROOT/CarlaUE4.sh -RenderOffScreen -quality-level=Epic -carla-streaming-port=0 -nosound -opengl -carla-rpc-port=2000`

2) Inside the root LAV repo, run
```bash
conda activate LAV-env
CUDA_VISIBLE_DEVICES=0 bash run_benchmark.sh assets/town05_routes_roach.xml 2000
```

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