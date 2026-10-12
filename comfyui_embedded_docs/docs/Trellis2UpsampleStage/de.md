# Trellis2-Upsample-Stufe

Dieser Node skaliert ein Shape-Latent mit 512-Auflösung in hochauflösende Sparse-Koordinaten hoch und bereitet den zweiten Sampling-Durchlauf der Shape-Stufe bei der Zielauflösung vor. Er hängt Metadaten pro Stufe an das Conditioning an, damit das Modell sie während der Generierung nutzen kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Das positive Conditioning, an das die Shape-Metadaten der Upsampling-Stufe angehängt werden. | CONDITIONING | Ja | |
| `negative` | Das negative Conditioning, an das die Shape-Metadaten der Upsampling-Stufe angehängt werden. | CONDITIONING | Ja | |
| `shape_latent` | Das Shape-Latent mit 512-Auflösung aus dem ersten KSampler der Shape-Stufe. | LATENT | Ja | |
| `vae` | Der Trellis2-VAE, der verwendet wird, um das Shape-Latent in hochauflösende Sparse-Koordinaten zu dekodieren. | VAE | Ja | |
| `target_resolution` | Voxel-Auflösung der hochskalierten Shape. Höher = mehr Details, mehr VRAM. Standard: 1024. | INT | Ja | 1024 - 2048 (step 128) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positives Conditioning mit angehängten Shape-Metadaten der Upsampling-Stufe. | CONDITIONING |
| `negative` | Negatives Conditioning mit angehängten Shape-Metadaten der Upsampling-Stufe. | CONDITIONING |
| `latent` | Mit Nullen gefülltes Latent, das für den zweiten Sampling-Durchlauf der Shape-Stufe bei der Zielauflösung vorbereitet wurde und die hochskalierten Koordinaten, Koordinatenanzahlen pro Sample sowie Metadaten zur Koordinatenauflösung enthält. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/de.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
