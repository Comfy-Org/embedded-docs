# MiniMax H3 Image Conditioning

Wandelt einen Prompt mit MiniMax H3 Image in eine Konditionierung und ein leeres Latent für ein Standbild um. Ohne Bilder handelt es sich um Text-zu-Bild; bei verbundenen Bildern werden diese bearbeitet, und der Prompt verweist auf sie als `<Picture 1>`, `<Picture 2>` und so weiter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell MiniMax H3 Image, das den Prompt mit etwaigen Referenzbildern tokenisiert und die Konditionierung kodiert. | CLIP | Ja | - |
| `vae` | Die VAE von MiniMax H3 Image. Damit werden die Bilder außerdem als Referenz-Latents verankert; ohne sie konditionieren sie nur den Textencoder. | VAE | Nein | - |
| `prompt` | Was generiert oder wie die Referenzbilder bearbeitet werden sollen. | STRING | Ja | Mehrzeiliger Text |
| `width` | Ausgabebreite in Pixeln. 0 verwendet die Breite von `image_1` nach dessen Referenzskalierung oder 2048 ohne Bilder. Standard: 0. | INT | Ja | 0 bis MAX_RESOLUTION (Schritt 32) |
| `height` | Ausgabehöhe in Pixeln. 0 verwendet die Höhe von `image_1` nach dessen Referenzskalierung oder 2048 ohne Bilder. Standard: 0. | INT | Ja | 0 bis MAX_RESOLUTION (Schritt 32) |
| `images` | Erweiterbare Gruppe von Referenzbildern, beginnend mit `image_1`; `image_1` ist das zu bearbeitende Bild. Der Prompt spricht sie als `<Picture n>` an. | AUTOGROW | Nein | 0 bis 100 Bilder |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Konditionierung für den MiniMax H3 Image Sampler, mit angehängten Referenz-Latents, wenn Bilder verbunden sind. | CONDITIONING |
| `latent` | Leeres Latent für ein Bild, 24 Kanäle bei einem Sechzehntel der Ausgabegröße. | LATENT |

Hinweis: Das Modell ist auf eine Fläche von 2048x2048 Pixeln abgestimmt, daher `width` und `height` auf 0 lassen, es sei denn, eine andere Leinwand wird benötigt.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageConditioning/de.md)

---
**Source fingerprint (SHA-256):** `b0927bbc44ac82e8a23b1edb5470c0cc8945844c326a352d75495ed801d11b1d`
