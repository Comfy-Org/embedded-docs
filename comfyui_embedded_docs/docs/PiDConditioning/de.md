# PiDConditioning

Fügt einem CONDITIONING einen Latent- und einen degrade_sigma-Wert hinzu, damit es für die PiD-Dekodierung oder -Hochskalierung verwendet werden kann. Dadurch können Sie steuern, wie stark das Latent vor der Verarbeitung degradiert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Die Conditioning-Daten, an die das Latent und das Degrade-Sigma angehängt werden. | CONDITIONING | Ja | - |
| `latent` | Das Latent (von VAEEncode oder einem KSampler), das an das Conditioning angehängt werden soll. | LATENT | Ja | - |
| `latent_format` | Das Format des Latents. Flux1-Latents (16 Kanäle) und Flux2-Latents (128 Kanäle) werden unter `"flux"` automatisch anhand der Kanaldimension erkannt. Für SD3 (16 Kanäle), SDXL (4 Kanäle) oder QwenImage (16 Kanäle) manuell auswählen (Standard: `"flux"`). | COMBO | Ja | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | Der Grad der anzuwendenden Degradierung. 0 bedeutet ein sauberes Latent. Erhöhen Sie diesen Wert, um beschädigte Latent-Ausgaben zu entrauschen (Standard: 0.0). | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |

Hinweis: Wenn `latent_format` auf `"flux"` gesetzt ist, erkennt der Node den Latent-Typ automatisch anhand der Kanaldimension: 128 Kanäle werden als Flux2-Latents behandelt, während 16 Kanäle als Flux1-Latents behandelt werden.

Hinweis: Ein nicht unterstützter `latent_format`-Wert löst einen Fehler aus, aber alle verfügbaren Optionen werden vom Node verarbeitet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `CONDITIONING` | Die ursprünglichen Conditioning-Daten mit angehängtem Latent und angehängtem Degrade-Sigma-Wert. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/de.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
