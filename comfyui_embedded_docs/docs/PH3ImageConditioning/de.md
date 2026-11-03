# p-h3-image Conditioning

Dieser Node wandelt einen Prompt in Conditioning und einen leeren Latent für ein einzelnes Standbild mit p-h3-image um. Ohne Bilder handelt es sich um Text-zu-Bild; wenn Bilder verbunden sind, ist `image_1` das Bild, das bearbeitet wird, und die anderen Slots dienen als Referenzen, die der Prompt mit `<Picture 1>`, `<Picture 2>` usw. adressiert. Der Sampler benötigt ein Modell, das mit dem MiniMax H3 Sigma-Shift-Node gepatcht wurde, wobei beide Shift-Werte auf 1.0 stehen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das p-h3-image CLIP-Modell, mit dem der Prompt einschließlich etwaiger Referenzbilder tokenisiert und das Conditioning kodiert wird. | CLIP | Ja | - |
| `prompt` | Was generiert werden soll oder wie `image_1` bearbeitet werden soll. Wenn Bilder verbunden sind, wird einer kurzen Anweisung `Edit <Picture 1>. ` vorangestellt. Eine Anweisung, die bereits mit `Edit <Picture` beginnt, oder eine Bearbeitungsanweisung, die von einem Prompt-Upsampler erzeugt wurde, wird exakt so verwendet, wie sie geschrieben ist. | STRING | Ja | - |
| `width` | Ausgabebreite in Pixeln, gerundet auf ein Vielfaches von 32. 0 verwendet die Breite von `image_1` nach der Skalierung oder 2912, wenn kein Bild verbunden ist (Standard: 0). | INT | Ja | 0 bis MAX_RESOLUTION |
| `height` | Ausgabehöhe in Pixeln, gerundet auf ein Vielfaches von 32. 0 verwendet die Höhe von `image_1` nach der Skalierung oder 2912, wenn kein Bild verbunden ist (Standard: 0). | INT | Ja | 0 bis MAX_RESOLUTION |
| `vae` | Das p-h3-image VAE. Erforderlich, sobald ein Bild-Slot verbunden ist, da die Referenz-Latents damit kodiert werden. | VAE | Nein | - |
| `images` | Erweiterbare Gruppe von bis zu 9 Bildern, `image_1` bis `image_9`. `image_1` ist das Bild, das bearbeitet wird, die übrigen Slots sind Referenzen. | AUTOGROW | Nein | 0 bis 9 Bilder |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Conditioning für den p-h3-image Sampler. Wenn Bilder verbunden sind, trägt es außerdem die gepackten Referenz-Latents. | CONDITIONING |
| `latent` | Leerer Latent für ein einzelnes Standbild, einschließlich der beiden Audio-Latents, die das Modell erwartet. | LATENT |

**Hinweis:** Bilder erfordern die Eingabe `vae`. Wird der Node mit einem verbundenen Bild und ohne VAE ausgeführt, tritt ein Fehler auf.

**Hinweis:** Das Conditioning umfasst ein einzelnes Standbild. Für Video oder Audio verwenden Sie stattdessen die MiniMax H3 Video-Nodes.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/de.md)

---
**Source fingerprint (SHA-256):** `f1f5e5b2d3ff9bc2f3b81f3d0dd722e725c7930c6f95bf44ad83bc64357d2fb7`
