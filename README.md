## Setup
* To run CARLA and train the models, make sure you are using a machine with **at least** a mid-end GPU.
* Please follow [INSTALL.md](docs/INSTALL.md) to setup the environment.


## Evaluation
1) Launch carla env `CUDA_VISIBLE_DEVICES=0 bash /home/anthony/softwares/CARLA_0.9.10.1/CarlaUE4.sh -quality-level=Epic -carla-rpc-port=2000`

2) Inside the root LAV repo, run
```bash
conda activate LAV-env
CUDA_VISIBLE_DEVICES=0 bash run_benchmark.sh assets/routes_lav_valid.xml 2000
```
