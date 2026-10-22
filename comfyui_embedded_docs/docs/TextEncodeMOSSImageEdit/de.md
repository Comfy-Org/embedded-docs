# Text Encode MOSS-Image Edit

Kodiert eine Bearbeitungsanweisung zusammen mit Referenzbildern in Conditioning für ein MOSS-Image-Edit-LoRA. Verbinden Sie die Ausgabe als positive Conditioning und führen Sie eine zweite Instanz mit denselben Referenzen für die negative aus. Die Referenzen werden in der Größe verwendet, in der sie ankommen, daher sollten Sie sie vor dem Verbinden skalieren. Dieser Node ist in ComfyUI als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das die Anweisung tokenisiert und kodiert. | CLIP | Ja | - |
| `prompt` | Die Anweisung, die die Bearbeitung beschreibt. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | Beliebiger Text |
| `vae` | Das VAE, das verwendet wird, um die Referenzbilder in Referenz-Latents zu kodieren. | VAE | Ja | - |
| `edit_format` | Das Layout, mit dem das Edit-LoRA trainiert wurde. Es wählt die Referenz-Latents-Methode aus und ob der Text-Encoder auch die Referenzen sieht. | COMBO | Ja | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzbilder (`image_1`, `image_2`, ...). Jedes Bild wird in der Größe verwendet, in der es ankommt, sein Alphakanal wird verworfen und es wird per VAE in ein Referenz-Latent kodiert. | IMAGE | Ja | 1 oder mehr Bilder |

**Hinweis:** Bei `"ai-toolkit"` und `"ai-toolkit (kv_cache off)"` sieht der Text-Encoder auch jede Referenz, herunterskaliert auf maximal 384x384 Pixel und im Prompt mit einem `Picture N:`-Marker versehen, sodass die Anweisung sie anhand ihrer Nummer referenzieren kann. Bei `"Moss-Image-Edit"` erreichen die Referenzen das Modell nur als Referenz-Latents und der Text-Encoder sieht die Anweisung allein. `"ai-toolkit (kv_cache off)"` sorgt zusätzlich dafür, dass die Referenzen weiterhin auf das gerade generierte Bild achten, sodass sie bei jedem Sampling-Schritt neu berechnet werden.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die kodierte Anweisung mit den angehängten Referenz-Latents und der passenden Referenz-Latents-Methode. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/de.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
