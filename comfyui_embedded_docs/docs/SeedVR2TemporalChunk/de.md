# SeedVR2TemporalChunk

Dieser Node zerlegt einen SeedVR2-Video-Latent in kleinere zeitliche Chunks, die jeweils einzeln innerhalb des verfügbaren VRAM verarbeitet werden können. Er berechnet automatisch die optimale Chunk-Größe basierend auf Ihrem GPU-Speicher oder lässt Sie die Chunk-Größe manuell festlegen und gibt die Chunks in Reihenfolge zur Verarbeitung aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `latent` | Der VAE-kodierte SeedVR2-Latent, der aufgeteilt werden soll. Muss ein 5-D-Tensor (B, C, T, H, W) mit der erwarteten SeedVR2-Latent-Kanalanzahl sein. | LATENT | Ja | - |
| `temporal_overlap` | Latent-Frames, die zwischen benachbarten Chunks geteilt und beim Zusammenführen überblendet werden; 0 bedeutet keine Überlappung (Standard: 0). Die effektive Überlappung ist auf eins weniger als die Anzahl der Latent-Frames des Chunks begrenzt. | INT | Nein | 0 to 16384 |
| `chunking_mode` | `manual` verwendet `frames_per_chunk` exakt; `auto` prognostiziert den größten Chunk, der in den freien VRAM passt. | COMBO | Ja | `"auto"`<br>`"manual"` |

Wenn `chunking_mode` auf `"manual"` gesetzt ist, wird ein zusätzlicher Parameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `frames_per_chunk` | Pixel-Frames pro zeitlichem Chunk (4n+1: 1, 5, 9, 13, 17, 21, ...); die UI erhöht in Schritten von 4 (Standard: 21). | INT | Ja | 1 to 16384 |

Hinweis: Der Parameter `frames_per_chunk` erscheint nur, wenn `chunking_mode` auf `"manual"` gesetzt ist. Der Wert muss die Formel `(frames_per_chunk - 1) % 4 == 0` erfüllen, das heißt, er muss einer der folgenden Werte sein: 1, 5, 9, 13, 17, 21 usw. Der eingegebene Latent muss 5-dimensional sein und die erwartete SeedVR2-Latent-Kanalanzahl enthalten; andernfalls löst der Node einen Fehler aus. Wenn die Gesamtzahl der Pixel-Frames im Latent gleich oder kleiner als die gewählte Chunk-Größe (oder die automatisch berechnete Größe) ist, gibt der Node den ursprünglichen Latent als einzelnen Chunk ohne Überlappung zurück.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `latents` | Die zeitlichen Chunks in sequenzieller Reihenfolge. Jeder Chunk ist ein LATENT mit derselben Batch-, Kanal-, Höhen- und Breitendimension, aber einer reduzierten zeitlichen Dimension. | LATENT |
| `temporal_overlap` | Die effektive Überlappung der Latent-Frames zwischen benachbarten Chunks, für Merge SeedVR2 Latents. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/de.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
