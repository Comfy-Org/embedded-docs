# Trellis2 VAE-Strukturdekodierung

Dieser Node konvertiert latente Trellis-Struktur-Samples in ein 3D-Voxelgitter unter Verwendung des Struktur-Decoders eines VAE. Er liest nur die ersten 8 Kanäle des Latents, rekonstruiert die Voxel-Belegung und passt die Ausgabeauflösung nach Bedarf auf entweder 32 oder 64 an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `samples` | Die latente Repräsentation der zu dekodierenden Struktur. Nur die ersten 8 Kanäle des Latents werden zur Dekodierung verwendet. | LATENT | Ja | - |
| `vae` | Der VAE, dessen Struktur-Decoder das Latent in ein Voxelgitter umwandelt. Die Dekodierung erfolgt in Batches. | VAE | Ja | - |
| `resolution` | Die Zielauflösung (räumlich) des Ausgabe-Voxelgitters (Standard: "32"). Wenn das dekodierte Gitter eine andere Auflösung hat, wird es entsprechend heruntergesampelt. | COMBO | Ja | "32"<br>"64" |

Hinweis: Wenn die Auflösung des dekodierten Voxelgitters von der ausgewählten `resolution` abweicht, wird das Gitter mittels 3D-Max-Pooling auf die angeforderte Größe heruntergesampelt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `voxel` | Ein binäres Voxel-Belegungsgitter als Float-Tensor mit der Form [batch, depth, height, width]. Werte sind 1.0 für belegte Voxel und 0.0 für leere Voxel. | VOXEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/de.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
