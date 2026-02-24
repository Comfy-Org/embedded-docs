> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/pt-BR.md)

O KSampler funciona da seguinte forma: ele modifica as informações latentes da imagem original fornecida com base em um modelo específico e em condições positivas e negativas.
Primeiro, ele adiciona ruído aos dados da imagem original de acordo com a **seed** e a **força de denoise** definidas, em seguida, insere o **Modelo** predefinido combinado com as condições de orientação **positivas** e **negativas** para gerar a imagem.

## Entradas

| Nome do Parâmetro      | Tipo de Dado | Obrigatório | Padrão  | Intervalo/Opções         | Descrição                                                                        |
| ---------------------- | ------------ | ----------- | ------- | ------------------------ | -------------------------------------------------------------------------------- |
| Model                  | checkpoint   | Sim         | Nenhum  | -                        | Modelo de entrada usado para o processo de remoção de ruído                      |
| seed                   | Int          | Sim         | 0       | 0 ~ 18446744073709551615 | Usado para gerar ruído aleatório; usar a mesma "seed" gera imagens idênticas     |
| steps                  | Int          | Sim         | 20      | 1 ~ 10000                | Número de etapas a usar no processo de remoção de ruído; mais etapas significam resultados mais precisos |
| cfg                    | float        | Sim         | 8.0     | 0.0 ~ 100.0              | Controla o quão de perto a imagem gerada corresponde às condições de entrada; 6-8 é recomendado |
| sampler_name           | UI Option    | Sim         | Nenhum  | Múltiplos algoritmos     | Escolhe o amostrador para remoção de ruído; afeta a velocidade e o estilo da geração |
| scheduler              | UI Option    | Sim         | Nenhum  | Múltiplos schedulers     | Controla como o ruído é removido; afeta o processo de geração                    |
| Positive               | conditioning | Sim         | Nenhum  | -                        | Condições positivas que orientam a remoção de ruído; o que você quer que apareça na imagem |
| Negative               | conditioning | Sim         | Nenhum  | -                        | Condições negativas que orientam a remoção de ruído; o que você não quer na imagem |
| Latent_Image           | Latent       | Sim         | Nenhum  | -                        | Imagem latente usada para a remoção de ruído                                     |
| denoise                | float        | Não         | 1.0     | 0.0 ~ 1.0                | Determina a proporção de remoção de ruído; valores mais baixos significam menos conexão com a imagem de entrada |
| control_after_generate | UI Option    | Não         | Nenhum  | Random/Inc/Dec/Keep      | Fornece a capacidade de alterar a seed após cada prompt                          |

## Saída

| Parâmetro | Função                                   |
| --------- | ---------------------------------------- |
| Latent    | Saída do latente após a remoção de ruído do amostrador |

## Código Fonte

[Atualizado em 15 de maio de 2025]

```Python

def common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=1.0, disable_noise=False, start_step=None, last_step=None, force_full_denoise=False):
    latent_image = latent["samples"]
    latent_image = comfy.sample.fix_empty_latent_channels(model, latent_image)

    if disable_noise:
        noise = torch.zeros(latent_image.size(), dtype=latent_image.dtype, layout=latent_image.layout, device="cpu")
    else:
        batch_inds = latent["batch_index"] if "batch_index" in latent else None
        noise = comfy.sample.prepare_noise(latent_image, seed, batch_inds)

    noise_mask = None
    if "noise_mask" in latent:
        noise_mask = latent["noise_mask"]

    callback = latent_preview.prepare_callback(model, steps)
    disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
    samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative, latent_image,
                                  denoise=denoise, disable_noise=disable_noise, start_step=start_step, last_step=last_step,
                                  force_full_denoise=force_full_denoise, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)
    out = latent.copy()
    out["samples"] = samples
    return (out, )
class KSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {"tooltip": "The model used for denoising the input latent."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "The random seed used for creating the noise."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "The number of steps used in the denoising process."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "The algorithm used when sampling, this can affect the quality, speed, and style of the generated output."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "The scheduler controls how noise is gradually removed to form the image."}),
                "positive": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to include in the image."}),
                "negative": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to exclude from the image."}),
                "latent_image": ("LATENT", {"tooltip": "The latent image to denoise."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("The denoised latent.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "Uses the provided model, positive and negative conditioning to denoise the latent image."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```
