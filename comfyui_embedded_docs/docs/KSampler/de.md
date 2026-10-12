# KSampler

Der KSampler funktioniert folgendermaßen: Er modifiziert die bereitgestellten ursprünglichen Latent-Bildinformationen auf Basis eines bestimmten Modells sowie sowohl positiver als auch negativer Bedingungen.
Zuerst fügt er den ursprünglichen Bilddaten gemäß dem festgelegten **seed** und der **Denoise-Stärke** Rauschen hinzu, dann werden das voreingestellte **Model** zusammen mit den **positive**- und **negative**-Führungsbedingungen eingegeben, um das Bild zu erzeugen.

## Eingaben

| Parametername | Beschreibung | Datentyp | Erforderlich | Standard | Bereich/Optionen |
| --- | --- | --- | --- | --- | --- |
| Model | Eingabemodell, das für den Denoising-Prozess verwendet wird | checkpoint | Ja | Keine | - |
| seed | Wird zur Erzeugung von Zufallsrauschen verwendet; die Verwendung desselben "seed" erzeugt identische Bilder | Int | Ja | 0 | 0 ~ 18446744073709551615 |
| steps | Anzahl der im Denoising-Prozess verwendeten Schritte; mehr Schritte bedeuten genauere Ergebnisse | Int | Ja | 20 | 1 ~ 10000 |
| cfg | Steuert, wie genau das erzeugte Bild mit den Eingabebedingungen übereinstimmt; 6–8 empfohlen | float | Ja | 8.0 | 0.0 ~ 100.0 |
| sampler_name | Wählt den Sampler für das Denoising; beeinflusst Generierungsgeschwindigkeit und Stil | UI Option | Ja | Keine | Mehrere Algorithmen |
| scheduler | Steuert, wie Rauschen entfernt wird; beeinflusst den Generierungsprozess | UI Option | Ja | Keine | Mehrere Scheduler |
| Positive | Positive Bedingungen, die das Denoising leiten; das, was im Bild erscheinen soll | conditioning | Ja | Keine | - |
| Negative | Negative Bedingungen, die das Denoising leiten; das, was nicht im Bild erscheinen soll | conditioning | Ja | Keine | - |
| Latent_Image | Latent-Bild, das für das Denoising verwendet wird | Latent | Ja | Keine | - |
| denoise | Bestimmt das Rauschentfernungsverhältnis; niedrigere Werte bedeuten eine geringere Verbindung zum Eingabebild | float | Nein | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | Ermöglicht das Ändern des Seeds nach jedem Prompt | UI Option | Nein | Keine | Random/Inc/Dec/Keep |

## Ausgabe

| Parameter | Funktion |
| --- | --- |
| Latent | Gibt das Latent nach dem Sampler-Denoising aus |

## Quellcode

[Aktualisiert am 15. Mai 2025]

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

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/de.md)
