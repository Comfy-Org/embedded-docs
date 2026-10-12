# Text kodieren Qwen Image 2.1

Der Node TextEncodeQwenImage21 kodiert einen Prompt und einen Negativ-Prompt für das Modell Qwen-Image 2.1 und hängt optional Referenzbilder an. Referenzbilder werden vom Textencoder gesehen und, wenn ein VAE verbunden ist, zusätzlich als Latents kodiert, die in die Sequenz eingefügt werden. Dadurch trägt die Konditionierung sowohl die Textanweisung als auch die visuelle Referenz. Der Node gibt die positive und die negative Konditionierung zusammen mit einem leeren Latent zurück, das auf die Größe des ersten Referenzbilds dimensioniert und bereit für das Sampling ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Der Textencoder von Qwen-Image 2.1, der zum Tokenisieren und Kodieren der Prompts verwendet wird. | CLIP | Ja | - |
| `prompt` | Text-Prompt, der das zu generierende Bild oder die anzuwendende Bearbeitung beschreibt. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | Beliebiger Text |
| `negative_prompt` | Text-Prompt, der beschreibt, was das Ergebnis vermeiden soll. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | Beliebiger Text |
| `vae` | VAE, der zum Kodieren der Referenzbilder in Referenz-Latents verwendet wird. Wenn er weggelassen wird, beeinflussen die Referenzbilder das Ergebnis nur über den Textencoder. | VAE | Nein | - |
| `resolution` | Referenzbilder werden auf etwa `resolution` x `resolution` Pixel skaliert, auf Vielfache von 32, wobei das Seitenverhältnis erhalten bleibt. 0 behält die jeweilige Größe jeder Referenz bei, auf ein Vielfaches von 32 gerundet (Standard: 1024). | INT | Ja | 0 bis 4096 (Schrittweite 32) |
| `images` | Referenzbilder, die vom Textencoder gesehen und als VAE-Latents in die Sequenz eingefügt werden. Erweiterbarer Slot: Verbinden Sie bis zu 16 Bilder (`image_1` ... `image_16`). | IMAGE | Nein | 0 bis 16 Bilder |

Die Ausgabe des leeren Latents wird auf die Größe des ersten verbundenen Referenzbilds dimensioniert oder auf `resolution`, wenn kein Referenzbild verbunden ist. Verwenden Sie für das Sampling das Latent, das dieser Node zurückgibt: Jede andere Größe verschiebt die Bearbeitung. Wenn ein VAE verbunden ist, werden dieselben Referenz-Latents sowohl an die positive als auch an die negative Konditionierung angehängt, sodass ein einzelner Sampler-Schritt beide entrauschen kann.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Kodierte Konditionierung für den Prompt, die die Referenz-Latents trägt, wenn ein VAE verbunden ist. | CONDITIONING |
| `negative` | Kodierte Konditionierung für den Negativ-Prompt, mit denselben Referenz-Latents. | CONDITIONING |
| `latent` | Leeres Latent in der Größe des ersten Referenzbilds oder 1024 x 1024, wenn kein Referenzbild verbunden ist. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImage21/de.md)

---
**Source fingerprint (SHA-256):** `3870f04597d12b593498c12ca139428af2d717b65aa40c889de9373ae9eb475e`
