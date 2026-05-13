> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/pt-BR.md)

O KSampler funciona da seguinte forma: ele modifica as informações da imagem latente original fornecidas com base em um modelo específico e em condições positivas e negativas.
Primeiro, ele adiciona ruído aos dados da imagem original de acordo com a **semente** e a **força de redução de ruído** definidas, então insere o **Modelo** pré-definido combinado com as condições de orientação **positiva** e **negativa** para gerar a imagem.

## Entradas

| Nome do Parâmetro    | Tipo de Dado   | Obrigatório | Padrão | Faixa/Opções             | Descrição                                                                                     |
| -------------------- | -------------- | ----------- | ------ | ------------------------ | --------------------------------------------------------------------------------------------- |
| Model                | checkpoint     | Sim         | Nenhum | -                        | Modelo de entrada usado para o processo de redução de ruído                                   |
| seed                 | Int            | Sim         | 0      | 0 ~ 18446744073709551615 | Usado para gerar ruído aleatório; usar a mesma "semente" gera imagens idênticas               |
| steps                | Int            | Sim         | 20     | 1 ~ 10000                | Número de etapas no processo de redução de ruído; mais etapas significam resultados mais precisos |
| cfg                  | float          | Sim         | 8.0    | 0.0 ~ 100.0              | Controla o quão fielmente a imagem gerada corresponde às condições de entrada; recomenda-se 6-8 |
| sampler_name         | Opção de UI    | Sim         | Nenhum | Múltiplos algoritmos     | Escolhe o amostrador para redução de ruído; afeta a velocidade e o estilo da geração           |
| scheduler            | Opção de UI    | Sim         | Nenhum | Múltiplos agendadores    | Controla como o ruído é removido; afeta o processo de geração                                 |
| Positive             | conditioning   | Sim         | Nenhum | -                        | Condições positivas que guiam a redução de ruído; o que você deseja que apareça na imagem      |
| Negative             | conditioning   | Sim         | Nenhum | -                        | Condições negativas que guiam a redução de ruído; o que você não deseja na imagem              |
| Latent_Image         | Latent         | Sim         | Nenhum | -                        | Imagem latente usada para a redução de ruído                                                  |
| denoise              | float          | Não         | 1.0    | 0.0 ~ 1.0                | Determina a taxa de remoção de ruído; valores mais baixos significam menos conexão com a imagem de entrada |
| control_after_generate | Opção de UI  | Não         | Nenhum | Aleatório/Aum/Dim/Manter | Permite alterar a semente após cada prompt                                                    |

## Saída

| Parâmetro | Função                                              |
| --------- | --------------------------------------------------- |
| Latent    | Gera o latente após a redução de ruído pelo amostrador |

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
                "model": ("MODEL", {"tooltip": "O modelo usado para reduzir o ruído do latente de entrada."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "A semente aleatória usada para criar o ruído."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "O número de etapas usadas no processo de redução de ruído."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "A escala de Orientação Livre de Classificador equilibra criatividade e aderência ao prompt. Valores mais altos resultam em imagens mais próximas do prompt, no entanto, valores muito altos impactarão negativamente a qualidade."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "O algoritmo usado durante a amostragem; isso pode afetar a qualidade, velocidade e estilo da saída gerada."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "O agendador controla como o ruído é gradualmente removido para formar a imagem."}),
                "positive": ("CONDITIONING", {"tooltip": "O condicionamento que descreve os atributos que você deseja incluir na imagem."}),
                "negative": ("CONDITIONING", {"tooltip": "O condicionamento que descreve os atributos que você deseja excluir da imagem."}),
                "latent_image": ("LATENT", {"tooltip": "A imagem latente para reduzir o ruído."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "A quantidade de redução de ruído aplicada; valores mais baixos manterão a estrutura da imagem inicial, permitindo a amostragem imagem para imagem."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("O latente com ruído reduzido.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "Usa o modelo, condicionamento positivo e negativo fornecidos para reduzir o ruído da imagem latente."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```