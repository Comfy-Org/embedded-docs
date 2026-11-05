# RelayVSRConditioning

RelayVSR Conditioning bereitet die Konditionierung und das leere Latent für ein RelayVSR-Video-Upscale vor. RelayVSR führt sein Ein-Schritt-Wan-2.2-Modell nur auf jedem 15. Frame des Clips sowie auf dem letzten Frame aus, sodass das Latent, das es ausgibt, nur diese Keyframes enthält. VSR Decode füllt anschließend die Frames dazwischen auf.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das RelayVSR-Diffusionsmodell, geladen mit Load Model: `relayvsr_x2_lightx2v_int8_convrot.safetensors` oder `relayvsr_x4_int8_convrot.safetensors`. | MODEL | Ja | N/A |
| `images` | Das Video in niedriger Qualität in seiner nativen Auflösung. Der Upscale-Faktor des Modells bestimmt, wie groß das Ergebnis wird. | IMAGE | Ja | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Konditionierung, die die ausgewählten Keyframes als Führungsinformation in niedriger Qualität enthält. | CONDITIONING |
| `latent` | Leeres Latent mit einem Frame pro Keyframe, bereit für den Sampler. | LATENT |

## Verwendung

Sampeln Sie das `latent` mit einem Schritt bei CFG 1: Es gibt keinen Prompt und keinen Text-Encoder im Graphen. Geben Sie die Ausgabe des Samplers, dieselben `images` und einen RelayVSR Flash VAE an VSR Decode weiter und halten Sie das Paar passend: das x2-Modell mit dem x2-Decoder, das x4-Modell mit dem x4-Decoder.

Es werden nur Keyframes gesampelt, daher wird aus einem Clip mit 150 Frames ein Latent mit 11 Frames. Der Sampler arbeitet an einem kleinen Bruchteil des Videos, und VSR Decode rekonstruiert den Rest.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/de.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
