# InstructPixToPixConditioning

Der InstructPixToPixConditioning-Node bereitet Konditionierungsdaten für die InstructPix2Pix-Bildbearbeitung vor, indem er positive und negative Text-Prompts mit Bilddaten kombiniert. Er kodiert das Eingabebild durch ein VAE in eine latente Repräsentation und hängt dieses Latent sowohl an die positive als auch an die negative Konditionierung an, während er außerdem ein dazu passendes leeres Latent zurückgibt. Bildabmessungen werden automatisch auf Vielfache von 8 Pixeln zugeschnitten, damit das VAE sie verarbeiten kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierungsdaten, die Text-Prompts und Einstellungen für gewünschte Bildeigenschaften enthalten | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierungsdaten, die Text-Prompts und Einstellungen für unerwünschte Bildeigenschaften enthalten | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren von Eingabebildern in latente Repräsentationen verwendet wird | VAE | Ja | - |
| `pixels` | Eingabebild, das verarbeitet und in den latenten Raum kodiert werden soll | IMAGE | Ja | - |

**Hinweis:** Die Abmessungen des Eingabebildes werden automatisch durch mittiges Zuschneiden auf Vielfache von 8 Pixeln sowohl in der Breite als auch in der Höhe angepasst, um die Kompatibilität mit dem VAE-Kodierungsprozess sicherzustellen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Konditionierungsdaten, wobei das kodierte Bild-Latent als `concat_latent_image` angehängt ist | CONDITIONING |
| `negative` | Negative Konditionierungsdaten, wobei das kodierte Bild-Latent als `concat_latent_image` angehängt ist | CONDITIONING |
| `latent` | Latenter Tensor aus Nullen mit denselben Abmessungen wie das kodierte Bild | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/de.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
