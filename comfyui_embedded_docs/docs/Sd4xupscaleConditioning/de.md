# Sd4xupscaleConditioning

Dieser Node ist auf die Verbesserung der Auflösung von Bildern durch einen 4x-Upscale-Prozess spezialisiert, wobei Konditionierungselemente einbezogen werden, um die Ausgabe zu verfeinern. Er nutzt Diffusionstechniken, um Bilder hochzuskalieren, und ermöglicht die Anpassung des Skalierungsverhältnisses sowie eine Rausch-Augmentierung, um den Verbesserungsprozess fein abzustimmen.

## Eingaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `images` | Die Eingabebilder, die hochskaliert werden sollen. Dieser Parameter ist entscheidend, da er die Qualität und Auflösung der Ausgabebilder direkt beeinflusst. | `IMAGE` |
| `positive` | Positive Konditionierungselemente, die den Upscale-Prozess in Richtung gewünschter Attribute oder Merkmale in den Ausgabebildern lenken. | `CONDITIONING` |
| `negative` | Negative Konditionierungselemente, die der Upscale-Prozess vermeiden soll, wodurch die Ausgabe von unerwünschten Attributen oder Merkmalen weggeführt wird. | `CONDITIONING` |
| `scale_ratio` | Bestimmt den Faktor, um den die Bildauflösung erhöht wird. Ein höheres Skalierungsverhältnis führt zu einem größeren Ausgabebild und ermöglicht mehr Detail und Klarheit. | `FLOAT` |
| `noise_augmentation` | Steuert den Grad der Rausch-Augmentierung, die während des Upscale-Prozesses angewendet wird. Dies kann verwendet werden, um Variabilität einzuführen und die Robustheit der Ausgabebilder zu verbessern. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die verfeinerten positiven Konditionierungselemente, die aus dem Upscale-Prozess resultieren. | `CONDITIONING` |
| `negative` | Die verfeinerten negativen Konditionierungselemente, die aus dem Upscale-Prozess resultieren. | `CONDITIONING` |
| `latent` | Eine latente Repräsentation, die während des Upscale-Prozesses erzeugt wird und in der weiteren Verarbeitung oder beim Modelltraining verwendet werden kann. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/de.md)
