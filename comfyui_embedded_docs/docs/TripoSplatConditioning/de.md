# TripoSplatConditioning

Dieser Node kodiert ein Eingabebild mit dem DINOv3-Bildencoder und dem Flux2-VAE, um positive und negative Conditioning-Daten für das TripoSplat-Modell zu erzeugen. Außerdem wird ein Rauschziel fester Größe (Latent plus Kameradaten) erstellt, das als Ausgangspunkt für den KSampler dient.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ Bildencoder | CLIP_VISION | Ja | - |
| `vae` | Flux2 VAE | VAE | Ja | - |
| `image` | Das zu kodierende Eingabebild | IMAGE | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positive Conditioning-Daten, die die DINOv3-Merkmalssequenz und das als Referenz-Latent mitgeführte Flux2-VAE-Latent enthalten | CONDITIONING |
| `negative` | Negative Conditioning-Daten, die nullgefüllte DINOv3-Merkmale und ein nullgefülltes Flux2-VAE-Referenz-Latent enthalten | CONDITIONING |
| `latent` | Das Rauschziel fester Größe (Latent + Kamera) für den KSampler. Das Latent ist eine Shape-Code-Sequenz konstanter Form (8192 x 16), gepaart mit einem einzelnen Kamera-Token (1 x 5) | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/de.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
