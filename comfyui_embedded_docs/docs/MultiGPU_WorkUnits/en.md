# COMFYUI MultiGPU CFG Split Node

## Overview:

The MultiGPU CFG Split Node allows diffusion processing to occur using multiple GPUs installed in the same system. Performance results are workflow dependent, but speedups of up to 1.95x have been measured in common workflows.

## Key Details:

Mixing different GPU types is not supported, the installed GPUs must be the same (ie 2x 5090, or 2x 5080, etc.)

ComfyUI will automatically detect multiple installed GPUs at startup.

## Supported GPUs:

Any homogeneous dual GPU setups with Ampere+ architecture (e.g 2 x 3090 or 2 x RTX6000 Pro)

## Supported Models:

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein \- Base Versions  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Yes | N/A | The model to prepare for MultiGPU CFG splitting before sampling. |
| `max_gpus` | INT | Yes | Minimum: 1<br>Step: 1<br>Default: 2 | The maximum number of identical GPUs to use for splitting the workload. Set this to the number of matching GPUs installed in your system. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `MODEL` | MODEL | The model prepared for MultiGPU CFG splitting, ready for accelerated sampling. |

## Node:

![image1.png](./asset/image1.png)  
The max\_gpus field should be set to the maximum number of identical GPUs installed in the system. 

**Node placement:**  The MultiGPU CFG Split needs to be placed between the Model Load node and Sampling node. If other nodes are connected to the model output of the model loader node, the MultiGPU CFG should be the last node in the chain before the Sampling node.

![image2.png](./asset/image2.png)

**Workflow Requirements:** The node works by splitting the diffusion workflow at the CFG level, due to this, the CFG in the workflow must be greater than CFG=1. Distilled workflows which require a CFG \=1 will not show a performance benefit when using the MultiGPU CFG Split node to run on multiple GPUs. 

## Verifying Multi-GPU Utilization

When running a workflow with MultiGPU CFG Split enabled, you can look at the Windows Task Manager and select the performance category  
![image3.png](./asset/image3.webp)  
![image4.png](./asset/image4.web)  
You should see activity on both installed GPUs while the sampler is running in the workflow. 

## Known Issues:

TBD

## Sample Multi-GPU Workflow: (Wan 2.2 FP8)

[https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive\_link](https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive_link)  

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
