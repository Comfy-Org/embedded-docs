# Latent-Upscale-Modell laden

Der Node LatentUpscaleModelLoader lädt ein Modell, das auf das Hochskalieren latenter Repräsentationen spezialisiert ist, aus einer Datei, die im Ordner `latent_upscale_models` von ComfyUI gespeichert ist. Er erkennt die Modellarchitektur automatisch anhand des Dateiinhalts (Hunyuan Video 720p, Hunyuan Video 1080p oder ein Latent Upsampler) und konfiguriert das passende interne Modell, sodass das Ergebnis von anderen Nodes verwendet werden kann.Er erkennt außerdem Latent-Upscale-Modelle von MiniMax H3 und konfiguriert dafür den latenten Upscaler von MiniMax H3.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model_name` | Der Name der zu ladenden Latent-Upscale-Modell-Datei. Die verfügbaren Optionen werden dynamisch aus den Dateien befüllt, die im Verzeichnis `latent_upscale_models` von ComfyUI vorhanden sind. | COMBO | Ja | Alle Dateien im Ordner `latent_upscale_models` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geladene Latent-Upscale-Modell, konfiguriert und einsatzbereit. Je nach erkanntem Dateiinhalt handelt es sich um einen 720p-Hunyuan-Video-Upscaler, einen 1080p-Hunyuan-Video-Upscaler oder ein verpacktes Latent-Upsampler-Modell.Ein Latent-Upscale-Modell von MiniMax H3 wird als latenter Upscaler von MiniMax H3 geladen. | LATENT_UPSCALE_MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/de.md)

---
**Source fingerprint (SHA-256):** `3de8e009e6ce777815db462117cdebf57842cdc6dd43b6760490e5d9ef8ed138`
