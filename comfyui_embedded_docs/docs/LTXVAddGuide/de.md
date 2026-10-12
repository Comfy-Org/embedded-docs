# LTXVAddGuide

Der LTXVAddGuide-Node kodiert Eingabebilder oder -videos über einen VAE-Encoder und fügt sie als Guide-Keyframes zu einer latenten Videosequenz hinzu. Er aktualisiert sowohl positives als auch negatives Conditioning und gibt das geänderte Latent zurück, mit Optionen zum Festlegen des Startframes, der Conditioning-Stärke, einer optionalen Attention-Maske und optionaler IC-LoRA-Parameter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positives Conditioning als Eingabe, das mit Keyframe-Guidance modifiziert werden soll. | CONDITIONING | Ja | - |
| `negative` | Negatives Conditioning als Eingabe, das mit Keyframe-Guidance modifiziert werden soll. | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren der Eingabebild-/Videoframes verwendet wird. | VAE | Ja | - |
| `latent` | Latente Eingabesequenz, die die Conditioning-Frames aufnimmt. | LATENT | Ja | - |
| `image` | Bild oder Video, auf das das latente Video konditioniert werden soll. Muss 8*n + 1 Frames haben. Wenn das Video nicht 8*n + 1 Frames hat, wird es auf die nächstgelegene Anzahl von 8*n + 1 Frames zugeschnitten. | IMAGE | Ja | - |
| `frame_idx` | Frame-Index, bei dem die Konditionierung beginnen soll. Bei Einzelbildern oder Videos mit 1–8 Frames ist jeder frame_idx-Wert zulässig. Bei Videos mit 9+ Frames muss frame_idx durch 8 teilbar sein; andernfalls wird es auf das nächstniedrigere Vielfache von 8 abgerundet. Negative Werte werden vom Ende des Videos an gezählt. Standard: 0. | INT | Ja | -9999 to 9999 |
| `strength` | Stärke des Conditioning-Einflusses, wobei 1.0 vollständiges Conditioning und 0.0 kein Conditioning anwendet. Standard: 1.0. | FLOAT | Ja | 0.0 to 10.0 |
| `attention_mask` | Optionale räumliche Maske im Pixelraum. Steuert den Conditioning-Einfluss pro Region über Self-Attention, multipliziert mit strength. | MASK | Nein | - |
| `iclora_parameters` | Optionale IC-LoRA-Parameter von einem Get IC-LoRA Parameters-Node. Werden verwendet, um die Guide-Verarbeitung anzupassen, wie es für bestimmte IC-LoRAs erforderlich ist (z. B. solche mit einem reference_downscale_factor > 1). Wenn sie verkettet werden, verwendet jeder LTXVAddGuide nur die mit ihm verbundenen Parameter. | IC_LORA_PARAMETERS | Nein | - |

**Hinweis:** Das Eingabebild/-video muss eine Frameanzahl nach dem Muster 8*n + 1 haben (z. B. 1, 9, 17, 25 Frames). Wenn die Eingabe über dieses Muster hinausgeht, wird sie automatisch auf die nächstgelegene gültige Frameanzahl zugeschnitten.

**Hinweis zu `iclora_parameters`:** Bei Verwendung von IC-LoRA-Parametern mit einem `reference_downscale_factor` größer als 1 müssen die räumlichen Dimensionen des Latents (Breite und Höhe) durch diesen Faktor teilbar sein. Der Node löst einen Fehler aus, wenn diese Bedingung nicht erfüllt ist.

**Hinweis:** Die kodierten Guide-Frames müssen an der ausgewählten Frame-Position in die Latent-Sequenz passen. Wenn die konditionierten Frames die Länge der Latent-Sequenz überschreiten, löst der Node einen Fehler aus.

**Hinweis:** Das Hinzufügen eines Guides zu einem Latent, das Audio- und Videokanäle kombiniert, wird nicht unterstützt und löst einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positives Conditioning, aktualisiert mit Keyframe-Guidance-Informationen. | CONDITIONING |
| `negative` | Negatives Conditioning, aktualisiert mit Keyframe-Guidance-Informationen. | CONDITIONING |
| `latent` | Latent-Sequenz mit eingebundenen Conditioning-Frames und aktualisierter Noise-Maske. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/de.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
