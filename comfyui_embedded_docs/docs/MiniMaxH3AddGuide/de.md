# MiniMaxH3AddGuide

Dieser Node verankert ein Bild, einen kurzen Clip, Audio oder einen Clip mit seinem Soundtrack an einem beliebigen Frame eines MiniMax H3-Videos. Er fügt dem Conditioning am gewählten Frame-Index ein Guide-Keyframe hinzu, und Sie können mehrere dieser Nodes verketten, um mehrere Frames im selben Video zu verankern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Das Conditioning, dem das Guide-Keyframe hinzugefügt wird. | CONDITIONING | Ja | - |
| `vae` | Video-VAE, erforderlich, wenn ein Bild verbunden ist. | VAE | Nein | - |
| `audio_vae` | Audio-VAE, erforderlich, wenn Audio verbunden ist. | VAE | Nein | - |
| `latent` | Das MiniMax H3 Audio-Video-Latent, das das Zielvideo definiert. Muss ein MiniMax H3 AV-Latent sein (verschachtelt, mit zwei 5D-Tensoren, wobei der Video-Tensor 24 Kanäle hat). | LATENT | Ja | - |
| `image` | Bild- oder Video-Frames, die verankert werden sollen. Multi-Frame-Batches werden als Clip verankert und auf die gültigen Clip-Längen des Modells zugeschnitten: 5, 22, 39... (17k + 5) Frames. Batches mit weniger als 5 Frames verwenden nur das erste Bild. | IMAGE | Nein | - |
| `audio` | Soundtrack, der ab demselben Frame-Index verankert wird, zugeschnitten auf die verbleibende Dauer des Videos. | AUDIO | Nein | - |
| `frame_idx` | Frame-Index, an dem das Bild oder der erste Frame des Clips verankert wird. Negative Werte werden vom Ende des Videos an gezählt. (Standard: 0) | INT | Ja | -9999 bis 9999 |

**Einschränkungen:**
- Mindestens eines von `image` oder `audio` muss angegeben werden; andernfalls löst der Node einen Fehler aus.
- `vae` ist erforderlich, wenn `image` verbunden ist.
- `audio_vae` ist erforderlich, wenn `audio` verbunden ist.
- `image`-Batches mit weniger als 5 Frames verwenden nur das erste Bild; Batches mit 5 oder mehr Frames werden auf eine gültige Clip-Länge zugeschnitten (5, 22, 39 usw.).
- `frame_idx` muss den Guide innerhalb des Frame-Bereichs des Videos platzieren, und ein Multi-Frame-Clip muss vollständig in das Video passen; andernfalls löst der Node einen Fehler aus.
- Wenn Audio verbunden ist, darf der Frame-Index nicht nach dem Ende der Audiospur des Videos liegen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Das Conditioning mit dem hinzugefügten Guide-Keyframe, das den aufgelösten Frame-Index und, sofern angegeben, die kodierten Bild- oder Audio-Latents enthält. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/de.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
