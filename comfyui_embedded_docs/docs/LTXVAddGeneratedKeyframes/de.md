# LTXV Generierte Keyframes hinzufügen

Der Node LTXV Add Generated Keyframes hängt Detail-Keyframes an ein Video-Latent an. Jeder Keyframe ist ein Latent-Frame aus Tokens, der über einem einzelnen Pixel-Frame positioniert ist; er wird zusammen mit dem Video entrauscht und ist nicht Teil der dekodierten Ausgabe. Die Platzierung erfolgt als ein Slot pro `interval_frames` Pixel, wobei I2V-Frames, vorhandene Guides und bereits am Conditioning befindliche generierte Keyframes übersprungen werden; mit LTXV Separate Generated Keyframes lassen sie sich wieder extrahieren. Ein Checkpoint, der für generierte Keyframes trainiert wurde (einer, der `keyframes_abs_pos_embedding` trägt), ist erforderlich.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positives Conditioning, an das die Keyframes angehängt werden. | CONDITIONING | Ja | N/A |
| `negative` | Negatives Conditioning, an das die Keyframes angehängt werden. | CONDITIONING | Ja | N/A |
| `vae` | Wird nur verwendet, um die Latent-Skalierungsfaktoren zu lesen. | VAE | Ja | N/A |
| `latent` | Einfaches 5D-Video-Latent, neben dem Keyframes generiert werden. Fügen Sie sie vor Concat AV Latent hinzu. | LATENT | Ja | N/A |
| `interval_frames` | Pixel-Frame-Schrittweite für die automatische Platzierung. Standard 24 entspricht bei 24 fps etwa einem Keyframe pro Sekunde. Belegte Pixel werden übersprungen. Wird ignoriert, wenn `frame_indices` gesetzt ist. (Standard: 24) | INT | Nein | 1-1024 |
| `keyframes` | Optionaler Inhalt, mit dem die neuen Keyframes initialisiert werden. Verbinden Sie Keyframes aus einem früheren Separate (gleiche räumliche Größe) oder ein einfaches Video-Latent, um an jedem neuen Slot den nächstgelegenen Frame zu kopieren (z. B. nach temporalem Upscaling). Diese werden weiterhin entrauscht, nicht als Guides fixiert. Aufgezeichnete Indizes auf einem Keyframes-Latent werden ignoriert, sofern `frame_indices` nicht gesetzt ist. Hat nur eine Wirkung, wenn das Sampling unter Sigma 1 beginnt. | LATENT | Nein | N/A |
| `frame_indices` | Optionale Pixel-Frame-Indizes. Leer lassen, um anhand von `interval_frames` auf der aktuellen Arbeitsfläche zu platzieren. Wenn gesetzt, ist diese Liste die Platzierung (verbundene Keyframes werden in der Reihenfolge zugeordnet). Der letzte Frame ist erlaubt; Frame 0 nicht (er ist bereits ein eigenständiges Token). (Standard: leerer String) | STRING | Nein | Kommagetrennte Ganzzahlen; 1 bis zum letzten Pixel-Frame (Frame 0 ausgeschlossen) |

**Hinweis:** Das `latent` muss ein einfaches 5D-Video-Latent sein, wobei die generierten Keyframes vor Concat AV Latent hinzugefügt werden. Wenn `frame_indices` gesetzt ist, muss jeder aufgeführte Pixel-Frame eindeutig sein und darf nicht bereits einen Bild-Keyframe, einen Guide oder einen generierten Keyframe enthalten. Wenn `frame_indices` leer ist, werden belegte Pixel automatisch übersprungen; wenn kein freier Detail-Slot existiert, löst der Node einen Fehler aus. Beim Anhängen an vorhandene generierte Keyframes muss das Latent weiterhin dieselbe Anzahl Tokens pro Frame haben, und der vorhandene Block muss am letzten Latent-Frame enden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positives Conditioning mit angehängter Attention für generierte Keyframes. | CONDITIONING |
| `negative` | Negatives Conditioning mit angehängter Attention für generierte Keyframes. | CONDITIONING |
| `latent` | Video-Latent mit auf T angehängten generierten Keyframes. | LATENT |

## Hinweise

- Der Parameter `interval_frames` legt den Abstand automatisch platzierter Keyframes fest. Ein höherer Wert führt zu weniger Keyframes und größerem Abstand; ein niedrigerer Wert erzeugt mehr Keyframes.
- Der Eingang `keyframes` ermöglicht es, die neuen Keyframes mit vorhandenen Keyframes oder einem Video-Latent zu initialisieren. Wenn ein längeres einfaches Video-Latent bereitgestellt wird, wird an jedem neuen Slot der nächstgelegene Video-Frame kopiert. Diese Keyframes werden weiterhin entrauscht und nicht als Guides fixiert.
- Der Parameter `frame_indices` ermöglicht es, exakte Pixel-Frame-Indizes anzugeben, an denen Keyframes platziert werden sollen. Wenn er angegeben wird, wird `interval_frames` ignoriert. Die Liste muss eindeutige Ganzzahlen innerhalb des gültigen Pixelbereichs enthalten, und Frame 0 ist nicht erlaubt.
- Die Ausgaben `positive` und `negative` enthalten das Conditioning mit angehängter Attention für generierte Keyframes.
- Die Ausgabe `latent` enthält das Video-Latent mit auf T angehängten generierten Keyframes.
- Ein Checkpoint, der für generierte Keyframes trainiert wurde (einer, der `keyframes_abs_pos_embedding` trägt), ist erforderlich.
- Mit LTXV Separate Generated Keyframes lassen sich generierte Keyframes wieder extrahieren.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/de.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
