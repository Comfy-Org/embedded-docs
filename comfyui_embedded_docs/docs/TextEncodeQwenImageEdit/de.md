# TextEncodeQwenImageEdit

Der TextEncodeQwenImageEdit-Node wandelt Text-Prompts und optionale Bilder in Conditioning-Daten für die Bilderzeugung oder Bildbearbeitung um. Er verwendet ein CLIP-Modell, um die Eingabe zu tokenisieren, und kann optional Referenzbilder mit einem VAE kodieren, um Referenz-Latents zu erzeugen. Wenn ein Bild bereitgestellt wird, wird es automatisch skaliert, um einen konsistenten Verarbeitungsmaßstab beizubehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das für die Text- und Bild-Tokenisierung verwendet wird | CLIP | Ja | - |
| `prompt` | Text-Prompt für die Conditioning-Generierung, unterstützt mehrzeilige Eingabe und dynamische Prompts | STRING | Ja | - |
| `vae` | Optionales VAE-Modell zum Kodieren von Referenzbildern in Latents | VAE | Nein | - |
| `image` | Optionales Eingabebild für Referenz- oder Bearbeitungszwecke | IMAGE | Nein | - |

**Hinweis:** Wenn ein Bild bereitgestellt wird, wird es so skaliert, dass seine Gesamtpixelzahl nahe bei 1,048,576 (1024 × 1024) bleibt, und es werden nur seine RGB-Kanäle verwendet. Das skalierte Bild wird zusammen mit dem Prompt an den CLIP-Tokenizer übergeben. Wenn sowohl `image` als auch `vae` bereitgestellt werden, kodiert der Node das Bild außerdem in Referenz-Latents und hängt sie an die Conditioning-Ausgabe an.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Conditioning-Daten, die Text-Tokens und optionale Referenz-Latents für die Bilderzeugung enthalten | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/de.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
