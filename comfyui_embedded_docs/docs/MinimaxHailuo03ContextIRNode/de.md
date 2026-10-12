# MiniMax H3 Context IR (Prompt-Verbesserer)

## Überblick

Dieser Node verwendet MiniMax H3 Context IR, um Ihre Textbeschreibung und alle angehängten Medien zu analysieren und dann einen stärkeren, strukturierten Video-Prompt zu erzeugen. Der zurückgegebene Prompt ist so konzipiert, dass er mit dem Prompt-Eingang eines MiniMax H3-Video-Nodes verbunden werden kann; wenn Sie dort Medien anhängen, hängen Sie dieselben Medien in derselben Reihenfolge an, denn der verbesserte Prompt verweist anhand der Position auf die Medien.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `model` | Modell, das für die Prompt-Verbesserung verwendet wird. | DYNAMIC_COMBO | Ja | `"MiniMax H3"` |
| `first_frame` | Erstes Einzelbild des Videos, das Sie generieren möchten. Kann nicht mit Referenzmedien kombiniert werden. | IMAGE | Nein | Einzelbild |
| `last_frame` | Letztes Einzelbild des Videos, das Sie generieren möchten. Kann nicht mit Referenzmedien kombiniert werden. | IMAGE | Nein | Einzelbild |

### MiniMax H3 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `prompt` | Beschreibung des Videos, das Sie generieren möchten. Darf nicht leer sein. (Standard: `""`) | STRING | Ja | Beliebiger Text (darf nicht leer sein) |
| `duration` | Dauer des Videos, das Sie generieren möchten, in Sekunden (4-15). (Standard: 5) | INT | Ja | 4 bis 15 |
| `ratio` | Seitenverhältnis des Videos, das Sie generieren möchten. `"adaptive"` erfordert mindestens eine Bild-, Video- oder Audio-Eingabe. (Standard: `"adaptive"`) | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `reference_images` | Referenzbilder für Motiv oder Stil, im Prompt als "Image 1".."Image 9" in Verbindungsreihenfolge bezeichnet. Bis zu 9 Bilder. Erweiterbarer Slot: `image_1`...`image_9` verbinden. | IMAGE | Nein | 0 bis 9 Bilder |
| `reference_videos` | Referenzvideos für Bewegung oder Szene, im Prompt als "Video 1".."Video 3" in Verbindungsreihenfolge bezeichnet. Bis zu 3 Videos, jeweils 2-15 Sekunden, insgesamt 15 Sekunden. Erweiterbarer Slot: `video_1`...`video_3` verbinden. | VIDEO | Nein | 0 bis 3 Videos |
| `reference_audios` | Audio-Referenzen, im Prompt als "Audio 1".."Audio 3" in Verbindungsreihenfolge bezeichnet. Bis zu 3 Clips, jeweils 2-15 Sekunden, insgesamt 15 Sekunden. Können nicht ohne ein Referenzbild oder -video verwendet werden. Erweiterbarer Slot: `audio_1`...`audio_3` verbinden. | AUDIO | Nein | 0 bis 3 Clips |

### Parametereinschränkungen

- Die Eingaben `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` und `reference_audios` sind Teil der Optionsgruppe `model` und erscheinen, wenn "MiniMax H3" ausgewählt ist.
- `first_frame` und `last_frame` können nicht mit Referenzmedien kombiniert werden.
- `reference_audios` kann nicht verwendet werden, es sei denn, mindestens ein `reference_image` oder `reference_video` ist ebenfalls verbunden.
- Wenn keine Frames und keine Referenzmedien verbunden sind, kann `ratio` nicht auf `"adaptive"` gesetzt werden.
- Referenzvideos müssen jeweils etwa 2-15 Sekunden lang sein, bei einer Gesamtdauer von höchstens 15 Sekunden. Ihre Bildrate muss zwischen 23,9 und 60,5 FPS liegen.
- Referenzaudios müssen jeweils etwa 2-15 Sekunden lang sein, bei einer Gesamtdauer von höchstens 15 Sekunden.
- `first_frame`, `last_frame` und jedes Referenzbild müssen mindestens 256x256 Pixel groß sein und ein Seitenverhältnis zwischen 0,4 und 2,5 aufweisen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `STRING` | Der verbesserte, strukturierte Video-Prompt, der von MiniMax H3 Context IR generiert wurde. Er kann mit dem Prompt-Eingang eines MiniMax H3-Video-Generierungs-Nodes verbunden werden. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/de.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
