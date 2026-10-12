# SeedVR2ProgressiveSampler

Sequenzieller Sampler für zeitliches Chunking für native SeedVR2-Workflows. Dieser Node verarbeitet lange Video-Latents, indem er sie in kleinere zeitliche Chunks aufteilt, jeden Chunk sequenziell sampelt und die Ergebnisse miteinander überblendet. Er dient als direkter Ersatz für den Standard-KSampler bei der Arbeit mit SeedVR2-Modellen auf Sequenzen, die andernfalls Out-of-Memory-Fehler verursachen würden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das Modell, das zum Denoising des Eingabe-Latents verwendet wird | MODEL | Ja | |
| `seed` | Der Zufallsseed, der zur Erzeugung des Rauschens verwendet wird (Standard: 0) | INT | Ja | 0 bis 0xffffffffffffffff |
| `steps` | Die Anzahl der Schritte, die im Denoising-Prozess verwendet werden (Standard: 20) | INT | Ja | 1 bis 10000 |
| `cfg` | Die Classifier-Free-Guidance-Skala balanciert Kreativität und Prompt-Treue aus. Höhere Werte führen zu Bildern, die dem Prompt stärker entsprechen; zu hohe Werte wirken sich jedoch negativ auf die Qualität aus (Standard: 1.0) | FLOAT | Ja | 0.0 bis 100.0 |
| `sampler_name` | Der Algorithmus, der beim Sampling verwendet wird; dies kann Qualität, Geschwindigkeit und Stil der generierten Ausgabe beeinflussen | COMBO | Ja | Mehrere Optionen verfügbar |
| `scheduler` | Der Scheduler steuert, wie Rauschen schrittweise entfernt wird, um das Bild zu formen | COMBO | Ja | Mehrere Optionen verfügbar |
| `positive` | Das Conditioning, das die Attribute beschreibt, die im Bild enthalten sein sollen | CONDITIONING | Ja | |
| `negative` | Das Conditioning, das die Attribute beschreibt, die aus dem Bild ausgeschlossen werden sollen | CONDITIONING | Ja | |
| `latent` | Das zu entrauschende Latent-Bild | LATENT | Ja | |
| `denoise` | Der Grad des angewendeten Denoisings; niedrigere Werte erhalten die Struktur des Ausgangsbilds bei und ermöglichen Image-to-Image-Sampling (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `frames_per_chunk` | Pixel-Frames pro zeitlichem Chunk. Muss ein 4n+1-Wert sein (1, 5, 9, 13, 17, 21, ...), um den SeedVR2-Einschränkungen zu entsprechen (Standard: 21) | INT | Ja | 1 bis 16384 (Schrittweite 4) |
| `temporal_overlap` | Latent-Frames, die zwischen benachbarten Chunks überblendet werden, um die Naht zu verbergen; 0 bedeutet keine Überblendung (Standard: 0) | INT | Ja | 0 bis 16384 |
| `chunking_mode` | manual = verwendet `frames_per_chunk` exakt; auto = verkleinert den Chunk, bis er in den VRAM passt (Standard: "manual") | COMBO | Ja | "manual"<br>"auto" |

**Hinweis zu `frames_per_chunk`:** Dieser Parameter muss eine Pixel-Frame-Anzahl von 4n+1 sein (1, 5, 9, 13, 17, 21, ...). Der Node löst einen Fehler aus, wenn ein ungültiger Wert angegeben wird.

**Hinweis zu `temporal_overlap`:** Der Überlappungswert wird automatisch auf höchstens eins weniger als die Latent-Chunk-Größe begrenzt, um eine gültige Chunk-Verarbeitung sicherzustellen.

**Hinweis zu `chunking_mode`:** Wenn auf "auto" gesetzt, versucht der Node automatisch kleinere Chunk-Größen, falls der aktuelle Chunk einen Out-of-Memory-Fehler verursacht. Wenn alle Versuche fehlschlagen, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `latent` | Die entrauschte Latent-Ausgabe, die aus allen zeitlichen Chunks wieder zu einem einzelnen zusammengeführten SeedVR2-Latent-Tensor zusammengesetzt wird | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2ProgressiveSampler/de.md)

---
**Source fingerprint (SHA-256):** `a4574c3e619954b5569551b5b2ba112ecbff918dcebb5ba718a14e77701144a9`
