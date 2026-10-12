# KSampler

Il KSampler funziona così: modifica le informazioni originali dell'immagine latente fornite in base a un modello specifico e a condizioni sia positive sia negative.
Innanzitutto, aggiunge rumore ai dati originali dell'immagine in base al **seed** e alla **forza di denoising** impostati, quindi inserisce il **Model** preimpostato combinato con le condizioni di guida **positive** e **negative** per generare l'immagine.

## Input

| Nome parametro | Descrizione | Tipo di dati | Obbligatorio | Predefinito | Intervallo/Opzioni |
| --- | --- | --- | --- | --- | --- |
| Model | Modello di input utilizzato per il processo di denoising | checkpoint | Sì | Nessuno | - |
| seed | Usato per generare rumore casuale; usando lo stesso "seed" si generano immagini identiche | Int | Sì | 0 | 0 ~ 18446744073709551615 |
| steps | Numero di passaggi da usare nel processo di denoising; più passaggi significano risultati più accurati | Int | Sì | 20 | 1 ~ 10000 |
| cfg | Controlla quanto l'immagine generata corrisponde alle condizioni di input; consigliato 6-8 | float | Sì | 8.0 | 0.0 ~ 100.0 |
| sampler_name | Sceglie il sampler per il denoising; influisce sulla velocità e sullo stile di generazione | UI Option | Sì | Nessuno | Molteplici algoritmi |
| scheduler | Controlla come viene rimosso il rumore; influisce sul processo di generazione | UI Option | Sì | Nessuno | Molteplici scheduler |
| Positive | Condizioni positive che guidano il denoising, ciò che si desidera far apparire nell'immagine | conditioning | Sì | Nessuno | - |
| Negative | Condizioni negative che guidano il denoising, ciò che non si desidera nell'immagine | conditioning | Sì | Nessuno | - |
| Latent_Image | Immagine latente usata per il denoising | Latent | Sì | Nessuno | - |
| denoise | Determina la percentuale di rimozione del rumore; valori più bassi significano meno connessione all'immagine di input | float | No | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | Fornisce la possibilità di cambiare seed dopo ogni prompt | UI Option | No | Nessuno | Random/Inc/Dec/Keep |

## Output

| Parametro | Funzione |
| -------------- | ------------------------------------------ |
| Latent         | Restituisce il latente dopo il denoising del sampler |

## Codice sorgente

[Aggiornato al 15 maggio 2025]

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

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/it.md)
