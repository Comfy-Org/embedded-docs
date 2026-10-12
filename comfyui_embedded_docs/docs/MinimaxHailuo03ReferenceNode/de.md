# MiniMax H3 Referenz zu Video

Dieser Node generiert ein Video mithilfe der MiniMax H3-Modelle, konditioniert auf Referenzbilder, -videos und -audio. Referenzen werden im Prompt über ihre Verbindungsreihenfolge angesprochen: "Image 1", "Image 2", "Video 1", "Audio 1" und so weiter. Zwei Modelle sind verfügbar: "MiniMax H3" und "MiniMax H3 Max".

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell für die Videogenerierung (Standard: "MiniMax H3"). Die Auswahl von "MiniMax H3" stellt die unten aufgeführten Generierungs- und Referenzeingaben für MiniMax H3 bereit. Die Auswahl von "MiniMax H3 Max" stellt die unten aufgeführten Generierungs- und Referenzeingaben für MiniMax H3 Max bereit. | DYNAMIC_COMBO | Ja | "MiniMax H3"<br>"MiniMax H3 Max" |
| `seed` | Zufälliger Seed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 4294967295 |
| `watermark` | Ob dem Video ein AIGC-Wasserzeichen hinzugefügt werden soll (Standard: false). Wird nur vom Modell MiniMax H3 unterstützt. | BOOLEAN | Nein | true<br>false |

### MiniMax H3 Eingaben

Diese Eingaben sind verfügbar, wenn "MiniMax H3" als Modell ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Referenzmedien können in ihrer Reihenfolge referenziert werden, zum Beispiel "Image 1", "Image 2", "Video 1" oder "Audio 1". | STRING | Ja | Mindestens 1 Zeichen |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "768P"<br>"2K" |
| `ratio` | Seitenverhältnis des Ausgabevideos (Standard: "adaptive"). | COMBO | Ja | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 4 bis 15 |

### MiniMax H3 Max Eingaben

Diese Eingaben sind verfügbar, wenn "MiniMax H3 Max" als Modell ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Referenzmedien können in ihrer Reihenfolge referenziert werden, zum Beispiel "Image 1", "Image 2", "Video 1" oder "Audio 1". | STRING | Ja | 1 bis 50000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "480P"<br>"768P" |
| `ratio` | Seitenverhältnis des Ausgabevideos (Standard: "adaptive"). | COMBO | Ja | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 5 bis 15 |
| `prompt_expansion_mode` | Wie viel Aufwand in die Umformulierung des Prompts vor der Generierung gesteckt wird (Standard: "balanced"). | COMBO | Ja | "balanced"<br>"quality" |
| `reference_detail` | Detailstufe, in der Referenzbilder übermittelt werden. "high" übermittelt sie in der größten vom Modell verwendeten Größe (bis zu einer kurzen Seite von 2048 Pixeln); "standard" verkleinert sie auf höchstens 2048x1024, um die Referenzkosten zu senken (Standard: "standard"). | COMBO | Ja | "high"<br>"standard" |

### Referenzeingaben

Diese Referenzeingaben werden von beiden Modellen gemeinsam genutzt. Jede ist ein erweiterbarer Slot.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie bis zu 9 Elemente (`image_1`...`image_9`). Referenzbilder für Motiv oder Stil, im Prompt als "Image 1".."Image 9" in Verbindungsreihenfolge referenziert. Bis zu 9 Bilder. | IMAGE | Nein | 0 bis 9 Bilder |
| `reference_videos` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Elemente (`video_1`...`video_3`). Referenzvideos für Bewegung oder Szene, im Prompt als "Video 1".."Video 3" in Verbindungsreihenfolge referenziert. Bis zu 3 Videos, jeweils 2-15 Sekunden, insgesamt 15 Sekunden. | VIDEO | Nein | 0 bis 3 Videos |
| `reference_audios` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Elemente (`audio_1`...`audio_3`). Audio-Referenzen, im Prompt als "Audio 1".."Audio 3" in Verbindungsreihenfolge referenziert. Bis zu 3 Clips, jeweils 2-15 Sekunden, insgesamt 15 Sekunden. Kann nicht ohne ein Referenzbild oder -video verwendet werden. | AUDIO | Nein | 0 bis 3 Clips |

### Parametereinschränkungen

- Mindestens ein Referenzbild oder ein Referenzvideo ist erforderlich. Nur Referenzaudio wird nicht akzeptiert.
- Jedes Referenzbild muss ein Seitenverhältnis zwischen etwa 0,4 und 2,5 (2:5 bis 5:2) sowie eine Mindestbreite und -höhe von 256 Pixeln haben.
- Jedes Referenzvideo muss zwischen 2 und 15 Sekunden lang sein und eine Bildrate zwischen 23,976 und 60 FPS aufweisen. Die Gesamtdauer aller Referenzvideos darf 15 Sekunden nicht überschreiten.
- Jeder Referenzaudioclip muss zwischen 2 und 15 Sekunden lang sein. Die Gesamtdauer aller Referenzaudioclips darf 15 Sekunden nicht überschreiten.
- Wenn "MiniMax H3 Max" ausgewählt ist, muss die Einstellung `watermark` deaktiviert sein.
- Wenn "MiniMax H3 Max" ausgewählt ist, darf die Gesamtzahl der Referenzdateien (Bilder, Videos und Audio zusammen) 12 nicht überschreiten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/de.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
