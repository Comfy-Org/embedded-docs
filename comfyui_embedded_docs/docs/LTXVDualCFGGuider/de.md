# LTXV Dual CFG Guider

Dieser Node erstellt ein geführtes Sampling-Objekt (CFG-Guider) für LTXV-AV-Modelle. Er wendet eine separate Guidance-Skala auf den Videoteil und den Audioteil eines gepackten LTXV-AV-Latents an, sodass Sie den Einfluss der Konditionierung auf jede Modalität unabhängig steuern können. Wenn die beiden Skalen gleich sind oder das Latent keine getrennten Video- und Audiokomponenten enthält, wird stattdessen eine einzige Gesamtskala verwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, das beim Sampling verwendet werden soll. | MODEL | Ja | - |
| `positive` | Positive Konditionierung, zu der die Generierung hingeführt werden soll. | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierung, von der die Generierung weggeführt werden soll. | CONDITIONING | Ja | - |
| `video_cfg` | Guidance-Stärke, die auf die Videomodalität des Latents angewendet wird (Standard: 3.0). | FLOAT | Ja | 0.0 bis 100.0 |
| `audio_cfg` | Guidance-Stärke, die auf die Audiomodalität des Latents angewendet wird (Standard: 7.0). | FLOAT | Ja | 0.0 bis 100.0 |

Hinweis: Wenn `video_cfg` und `audio_cfg` gleich sind (oder im Wert sehr nahe beieinander liegen), verwendet der Guider diesen Wert als eine einzelne CFG-Skala für das gesamte Latent. Wenn das Latent kein gepacktes LTXV-AV-Latent ist, wird nur der Wert von `video_cfg` verwendet.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `guider` | Der konfigurierte CFG-Guider, der an einen Sampler-Node übergeben werden soll. | GUIDER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/de.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
