# TextEncodeBooguEdit

Dieser Node bereitet Conditioning für die Bildbearbeitung mit Boogu vor. Er verarbeitet Referenzbilder, um sowohl positive als auch negative Conditioning-Ausgaben zu erzeugen. Das Referenzbild wird zweimal verwendet: Vision-Tokens aus dem Bild werden nur zum positiven Conditioning hinzugefügt, um die Bearbeitungsanweisung zu verstärken, während ein VAE-Referenz-Latent sowohl zum positiven als auch zum negativen Conditioning hinzugefügt wird, sodass es sich unter CFG aufhebt und die Identität des Originalbilds bewahrt bleibt; der Tokenizer wählt automatisch den passenden System-Prompt basierend auf dem Vorhandensein von Bildern und leeren negativen Prompts aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | Das CLIP-Modell, das zur Textkodierung verwendet wird | CLIP | Ja | |
| `prompt` | Der Text-Prompt, der die gewünschte Bearbeitung beschreibt. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | |
| `negative_prompt` | Der Text-Prompt, der beschreibt, was bei der Bearbeitung vermieden werden soll. Kann leer gelassen werden, um negatives Conditioning wegzulassen. Erweiterter Parameter. | STRING | Ja | |
| `vae` | Das VAE-Modell, das verwendet wird, um Referenzbilder in den Latent-Raum zu kodieren. Erforderlich, um Referenz-Latents zu den Conditioning-Ausgaben hinzuzufügen. | VAE | Nein | |
| `images` | Referenzbild(er) zum Bearbeiten. Boogu konzentriert sich auf eine Referenz pro Sample; mehr sind erlaubt. | IMAGE | Nein | Bis zu 16 Bilder |

Referenz-Latents werden nur dann zu beiden Conditioning-Ausgaben hinzugefügt, wenn `vae` zusammen mit mindestens einem Referenz-`image` bereitgestellt wird. Wird `vae` weggelassen, erhält die positive Ausgabe weiterhin Vision-Tokens aus den Referenzbildern, aber keine der beiden Ausgaben enthält Referenz-Latents.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Conditioning, das sowohl den Text-Prompt mit Vision-Tokens als auch die Referenz-Latents enthält | CONDITIONING |
| `negative` | Conditioning, das den negativen Text-Prompt und die Referenz-Latents enthält | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/de.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
