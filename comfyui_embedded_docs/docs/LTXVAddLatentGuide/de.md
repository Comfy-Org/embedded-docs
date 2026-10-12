# LTXVAddLatentGuide

Der Node LTXV Add Latent Guide heftet ein bereits kodiertes Latent als Guide an, für den Fall, dass der Guide aus einer früheren Stufe statt aus einem Bild stammt. Er hat dieselbe Wirkung wie LTXV Add Guide, jedoch ohne den VAE-Decode/Encode-Roundtrip. Ein Guide, der räumlich kleiner als das Ziel ist (eine IC-LoRA- oder Detailreferenz), wird auf ein dünn besetztes Raster dilatiert, und seine RoPE-Endpositionen werden um dasselbe Verhältnis erweitert, sodass er den Ziel-Canvas abdeckt, anstatt nur dessen obere linke Ecke zu adressieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positiver Conditioning-Eingang. | CONDITIONING | Ja | N/A |
| `negative` | Negativer Conditioning-Eingang. | CONDITIONING | Ja | N/A |
| `vae` | Das VAE-Modell, das verwendet wird, um die Downscale-Index-Formel für die Frame-Platzierung zu lesen. | VAE | Ja | N/A |
| `latent` | Ziel-Video-Latent, auf das der Guide angeheftet wird. | LATENT | Ja | N/A |
| `guiding_latent` | Guide-Latent. Seine räumliche Größe muss die räumliche Größe des Ziels auf beiden Achsen durch dieselbe ganze Zahl teilen; bei gleicher Größe wird es unverändert angeheftet, bei halber Größe wird es als x2-IC-LoRA-Referenz behandelt. | LATENT | Ja | N/A |
| `latent_idx` | Latent-Frame-Index, bei dem der Guide beginnt, gezählt in Latent-Frames statt in Pixel-Frames. Negative Werte platzieren den Guide auf Frames vor dem Anfang des Latents; sie werden nicht vom Ende des Latents aus rückwärts gezählt. Standard: 0. | INT | Ja | -9999 bis 9999 |
| `strength` | Auf 1.0 begrenzt. Ein dilatierter Guide markiert seine Padding-Positionen mit einer negativen Denoise-Maske, damit das Modell sie verwirft; oberhalb von 1.0 würden auch die beibehaltenen Positionen negativ werden und der gesamte Guide würde verworfen. Verstärken Sie stattdessen über 1.0 hinaus mit `attention_mask`. Standard: 1.0. | FLOAT | Ja | 0.0 bis 1.0, Schritt 0.01 |
| `attention_mask` | Optionale räumliche Maske im Pixelraum. Steuert den Conditioning-Einfluss pro Region über Self-Attention, multipliziert mit `strength`. | MASK | Nein | N/A |

### Hinweise

- Sowohl `latent` als auch `guiding_latent` müssen 5D-Video-Latents mit der Form (Batch, Kanäle, Frames, Höhe, Breite) sein.
- Der Guide muss in das Ziel-Latent passen: Die Frame-Anzahl des Guides plus `latent_idx` darf nicht über das Ende des Ziel-Latents hinauslaufen. Negative Werte für `latent_idx` sind erlaubt und platzieren den Guide vor dem Anfang des Latents.
- Die räumliche Größe des Guides muss die räumliche Größe des Ziels sowohl auf der Höhen- als auch auf der Breitenachse durch eine ganze Zahl teilen.
- Das Höhenverhältnis und das Breitenverhältnis müssen denselben Wert haben (ein quadratisches Verhältnis). Ein nicht quadratisches Verhältnis löst einen Fehler aus, da die Dilatation und die RoPE-Platzierung einen einzigen Downscale-Faktor für beide Achsen verwenden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positives Conditioning mit angehängtem Guide. | CONDITIONING |
| `negative` | Negatives Conditioning mit angehängtem Guide. | CONDITIONING |
| `latent` | Latent-Ausgabe mit angewendetem Guide, einschließlich der aktualisierten `noise_mask`. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/de.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
