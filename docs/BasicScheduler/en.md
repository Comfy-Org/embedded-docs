
The BasicScheduler node is designed to compute a sequence of sigma values for diffusion models based on the provided scheduler, model, and denoising parameters. It dynamically adjusts the total number of steps based on the denoise factor to fine-tune the diffusion process.

## Input types

| Parameter | Comfy dtype | Description |
|-----------|-------------|-------------|
| `model`   | `MODEL`     | The model parameter specifies the diffusion model for which the sigma values are to be calculated. It plays a crucial role in determining the appropriate sigma values for the diffusion process. |
| `scheduler` | `COMBO[STRING]` | The scheduler parameter determines the scheduling algorithm to be used for calculating the sigma values. It directly influences the progression and characteristics of the diffusion process. |
| `steps`    | `INT`       | The steps parameter indicates the total number of steps in the diffusion process. It affects the granularity and duration of the process. |
| `denoise`  | `FLOAT`     | The denoise parameter allows for adjusting the effective number of steps by scaling the total steps, enabling finer control over the diffusion process. |

## Output types

| Parameter | Comfy dtype | Description |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | The sigmas output represents the computed sequence of sigma values for the diffusion process, essential for controlling the noise level at each step. |