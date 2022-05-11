## Setup
* To run CARLA and train the models, make sure you are using a machine with **at least** a mid-end GPU.
* Please follow [INSTALL.md](docs/INSTALL.md) to setup the environment.


## Evaluation
1) Launch carla env `CUDA_VISIBLE_DEVICES=0 bash /home/anthony/softwares/CARLA_0.9.10/CarlaUE4.sh -RenderOffScreen -quality-level=Epic -carla-streaming-port=0 -nosound -opengl -carla-rpc-port=2000`

2) Inside the root LAV repo, run
```bash
conda activate LAV-env
CUDA_VISIBLE_DEVICES=0 bash run_benchmark.sh assets/town05_routes_roach.yml 2000
```
