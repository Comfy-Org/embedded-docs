# Text Encode MOSS-Image Edit

Kodiert eine Bearbeitungsanweisung zusammen mit Referenzbildern in Conditioning für ein MOSS-Image-Edit-LoRA. Verbinden Sie die Ausgabe als positive Conditioning und führen Sie eine zweite Instanz mit denselben Referenzen für die negative aus. Die Referenzen werden in der Größe verwendet, in der sie ankommen, daher sollten Sie sie vor dem Verbinden skalieren. Dieser Node ist in ComfyUI als experimentell gekennzeichnet. Ohne VAE gelangen die Bilder nur zum Text-Encoder.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das die Anweisung tokenisiert und kodiert. | CLIP | Ja | - |
| `prompt` | Die Anweisung, die die Bearbeitung beschreibt. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | Beliebiger Text |
| `vae` | Das VAE, das verwendet wird, um die Referenzbilder in Referenz-Latents zu kodieren. Optional: ohne VAE gelangen die Bilder nur zum Text-Encoder.| VAE | Nein | - |
| `edit_format` | Das Layout, mit dem das Edit-LoRA trainiert wurde. Es wählt die Referenz-Latents-Methode aus und ob der Text-Encoder auch die Referenzen sieht. | COMBO | Ja | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzbilder (`image_1`, `image_2`, ...). Jedes Bild wird in der Größe verwendet, in der es ankommt, sein Alphakanal wird verworfen und es wird per VAE in ein Referenz-Latent kodiert. Wenn ein VAE verbunden ist, wird der Alphakanal verworfen und jedes Bild in ein Referenz-Latent kodiert; ohne VAE gelangen die Bilder nur zum Text-Encoder.| IMAGE | Ja | 1 oder mehr Bilder |
| `image_strength` | Skaliert, wie stark das Modell auf die vom Text-Encoder gesehenen Bilder achtet (ai-toolkit-Formate oder ohne VAE): 0 ignoriert sie, 1 unverändert, über 1 betont sie. Erweitert. Standard: 1.0. | FLOAT | Ja | 0.0 to 100.0 (step 0.05) |

**Hinweis:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die kodierte Anweisung mit den angehängten Referenz-Latents und der passenden Referenz-Latents-Methode. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/de.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
