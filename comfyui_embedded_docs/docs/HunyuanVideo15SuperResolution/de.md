# Hunyuan Video 1.5 Super Resolution

Der Node HunyuanVideo15SuperResolution bereitet Conditioning-Daten für einen Video-Super-Resolution-Prozess vor. Er nimmt eine latente Repräsentation eines Videos und optional ein Startbild entgegen und verpackt sie zusammen mit Rausch-Augmentierung und CLIP-Vision-Daten in ein Format, das von einem Modell verwendet werden kann, um eine Ausgabe mit höherer Auflösung zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Conditioning-Eingabe, die mit Latent- und Augmentierungsdaten modifiziert werden soll. | CONDITIONING | Ja | N/A |
| `negative` | Die negative Conditioning-Eingabe, die mit Latent- und Augmentierungsdaten modifiziert werden soll. | CONDITIONING | Ja | N/A |
| `vae` | Die VAE, die zum Kodieren des optionalen `start_image` verwendet wird. Erforderlich, wenn `start_image` angegeben wird. | VAE | Nein | N/A |
| `start_image` | Ein optionales Startbild zur Steuerung der Super-Resolution. Wenn angegeben, wird es hochskaliert und in das Conditioning-Latent kodiert. | IMAGE | Nein | N/A |
| `clip_vision_output` | Optionale CLIP-Vision-Einbettungen, die dem Conditioning hinzugefügt werden. | CLIP_VISION_OUTPUT | Nein | N/A |
| `latent` | Die eingegebene latente Video-Repräsentation, die in das Conditioning aufgenommen wird. | LATENT | Ja | N/A |
| `noise_augmentation` | Die Stärke der Rausch-Augmentierung, die auf das Conditioning angewendet wird (Standard: 0.70). Dies ist ein erweiterter Parameter; ein Wert wird immer durch den Standardwert vorgegeben. | FLOAT | Ja | 0.0 - 1.0 (step 0.01) |

**Hinweis:** Wenn Sie ein `start_image` angeben, müssen Sie auch ein `vae` verbinden, damit es kodiert werden kann. Das `start_image` wird automatisch auf das 16-Fache der räumlichen Dimensionen (Breite und Höhe) des Eingabe-`latent` hochskaliert, dann kodiert und in das Conditioning-Latent eingesetzt. Für die Kodierung werden nur die RGB-Kanäle des `start_image` verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Das modifizierte positive Conditioning, das nun das verkettete Latent, die Rausch-Augmentierung und optionale CLIP-Vision-Daten enthält. | CONDITIONING |
| `negative` | Das modifizierte negative Conditioning, das nun das verkettete Latent, die Rausch-Augmentierung und optionale CLIP-Vision-Daten enthält. | CONDITIONING |
| `latent` | Das Eingabe-Latent wird unverändert weitergegeben. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/de.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
