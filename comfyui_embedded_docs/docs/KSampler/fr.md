# KSampler

Le KSampler fonctionne de la manière suivante : il modifie les informations de l'image latente originale fournie en fonction d'un modèle spécifique et de conditions positives et négatives.
Tout d'abord, il ajoute du bruit aux données de l'image originale selon la **graine (seed)** et la **force de débruitage (denoise strength)** définies, puis il utilise le **Modèle (Model)** prédéfini combiné aux conditions de guidage **positives** et **négatives** pour générer l'image.

## Entrées

| Nom du paramètre | Description | Type de données | Requis | Valeur par défaut | Plage/Options |
| --- | --- | --- | --- | --- | --- |
| Model | Modèle d'entrée utilisé pour le processus de débruitage | checkpoint | Oui | Aucun | - |
| seed | Utilisé pour générer un bruit aléatoire ; l'utilisation de la même "seed" génère des images identiques | Int | Oui | 0 | 0 ~ 18446744073709551615 |
| steps | Nombre d'étapes à utiliser dans le processus de débruitage ; plus d'étapes donnent des résultats plus précis | Int | Oui | 20 | 1 ~ 10000 |
| cfg | Contrôle la fidélité de l'image générée aux conditions d'entrée ; 6-8 recommandé | float | Oui | 8.0 | 0.0 ~ 100.0 |
| sampler_name | Choisir l'échantillonneur pour le débruitage ; affecte la vitesse et le style de génération | Option d'interface | Oui | Aucun | Plusieurs algorithmes |
| scheduler | Contrôle la suppression du bruit ; affecte le processus de génération | Option d'interface | Oui | Aucun | Plusieurs planificateurs |
| Positive | Conditions positives guidant le débruitage ; ce que vous voulez voir apparaître dans l'image | conditioning | Oui | Aucun | - |
| Negative | Conditions négatives guidant le débruitage ; ce que vous ne voulez pas dans l'image | conditioning | Oui | Aucun | - |
| Latent_Image | Image latente utilisée pour le débruitage | Latent | Oui | Aucun | - |
| denoise | Détermine le taux de suppression du bruit ; des valeurs plus faibles signifient moins de lien avec l'image d'entrée | float | Non | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | Permet de modifier la graine après chaque invite | Option d'interface | Non | Aucun | Aléatoire/Croissant/Décroissant/Conserver |

## Sortie

| Paramètre | Fonction                                   |
| --------------- | ------------------------------------------ |
| Latent          | Produit le latent après le débruitage de l'échantillonneur |

## Code source

[Mis à jour le 15 mai 2025]

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

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/fr.md)
