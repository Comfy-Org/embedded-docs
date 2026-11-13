# UltraTex Conditioning

Konditionieren Sie FLUX.2 Klein 9B mit dem UltraTex LoRA, um das Erscheinungsbild eines Referenzbildes als ein Bild pro Ansicht auf ein Mesh zu malen. Rendern Sie die Ansichten mit Render Mesh im Modus `world normal`, aus einer Create Camera Orbit mit 4 plus oben und unten, und backen Sie das Ergebnis mit Bake Texture From Views.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Textkonditionierung. UltraTex wurde mit einem leeren Prompt trainiert. | CONDITIONING | Ja | - |
| `vae` | VAE, die zum Kodieren der Normalen, der Ansichten und der Referenz verwendet wird. | VAE | Ja | - |
| `normals` | Render-Mesh-Bilder im Modus `world normal`: die 6 kanonischen Ansichten oder die 4 Seitenansichten. | IMAGE | Ja | - |
| `masks` | Render-Mesh-Masken derselben Ansichten, eine pro Ansicht. | MASK | Ja | - |
| `reference` | Das Objekt so, wie es aussehen soll, aus Sicht der Frontkamera. | IMAGE | Ja | - |
| `reference_mask` | Objektmaske der Referenz, weiß für das Objekt. Standard: vollständig weiß. | MASK | Nein | - |
| `extra_views` | Weitere Referenzen: das Objekt aus den anderen Ansichten, jede an ihre Ansicht gebunden, so wie die Referenz an die Front gebunden ist. Standard: `"off"`. | DYNAMIC_COMBO | Ja | `"off"`<br>`"on"` |

### Zusätzliche Ansichten "on" Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `right` | Das Objekt aus der rechten Ansicht. | IMAGE | Nein | - |
| `back` | Das Objekt aus der Rückansicht. | IMAGE | Nein | - |
| `left` | Das Objekt aus der linken Ansicht. | IMAGE | Nein | - |
| `top` | Das Objekt aus der Draufsicht. | IMAGE | Nein | - |
| `bottom` | Das Objekt aus der Untenansicht. | IMAGE | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Konditionierung, die das Ansichtsraster, die Referenz-Latents und die Token-Masken trägt, die UltraTex benötigt. | CONDITIONING |

Hinweis: `normals` muss entweder die 6 kanonischen Ansichten enthalten (Create Camera Orbit mit `count` 4 und `poles` oben und unten) oder die 4 Seitenansichten, und `masks` muss mit deren Ansichtsanzahl übereinstimmen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UltraTexConditioning/de.md)

---
**Source fingerprint (SHA-256):** `5b05f5151d4c12394ef893db69538adaef86e9cbdbb118a37c20919758520b6f`
