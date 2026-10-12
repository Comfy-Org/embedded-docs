# GeminiVideoOmniV2

Google Gemini Omni (Video) erzeugt aus einem Text-Prompt ein Video mit Audio unter Verwendung der Gemini Omni Flash-Modelle von Google. Optional können Sie Referenzbilder und/oder -videos anhängen, um das Ergebnis zu steuern oder vorhandenes Material zu bearbeiten. Beschreiben Sie die gewünschte Länge (3–10 Sekunden) direkt im Prompt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Gemini-Videomodell, das zur Generierung des Videos verwendet wird. | DYNAMIC_COMBO | Ja | "Omni Flash 1.1"<br>"Omni Flash" |

### Omni Flash 1.1 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreiben Sie das zu generierende Video oder die auf ein angehängtes Video anzuwendende Bearbeitung. Geben Sie die Länge direkt im Prompt an, z. B. „einen 6-sekündigen Clip“ oder für die Aufgabe 'extend' „um 5 Sekunden verlängern“; die generierte Länge kann 3–10 Sekunden betragen und ist standardmäßig 10. Die Ausgabe enthält Audio. (Standard: "") | STRING | Ja | - |
| `resolution` | Ausgabeauflösung. (Standard: "720p") | COMBO | Ja | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Ausgabe-Seitenverhältnis: 16:9 (Querformat) oder 9:16 (Hochformat). Die Aufgaben 'edit' und 'extend' behalten stattdessen das Seitenverhältnis des Eingabevideos bei. (Standard: "16:9") | COMBO | Ja | "16:9"<br>"9:16" |
| `task_type` | Was mit dem Prompt und den angehängten Medien geschehen soll. Bei 'auto' entscheidet das Modell. 'text_to_video' generiert allein aus dem Prompt und lehnt angehängte Medien ab. 'image_to_video' animiert ein Bild oder interpoliert von einem Startframe zu einem Endframe, wenn zwei angehängt sind. 'reference_to_video' behandelt die angehängten Medien als Motivreferenzen. 'edit' überarbeitet genau ein angehängtes Video, und 'extend' fügt neues Material daran an, sodass die Ausgabe mit dem Eingabevideo beginnt. (Standard: "auto") | COMBO | Ja | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Omni Flash Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreiben Sie das zu generierende Video oder die auf ein angehängtes Video anzuwendende Bearbeitung. Geben Sie die Länge direkt im Prompt an, z. B. „einen 6-sekündigen Clip“; die Länge kann 3–10 Sekunden betragen. Die Ausgabe ist 720p, 24 FPS, mit Audio. (Standard: "") | STRING | Ja | - |
| `aspect_ratio` | Ausgabe-Seitenverhältnis: 16:9 (Querformat) oder 9:16 (Hochformat). Die Aufgabe 'edit' behält stattdessen das Seitenverhältnis des Eingabevideos bei. (Standard: "16:9") | COMBO | Ja | "16:9"<br>"9:16" |
| `task_type` | Was mit dem Prompt und den angehängten Medien geschehen soll. Bei 'auto' entscheidet das Modell. 'text_to_video' generiert allein aus dem Prompt und lehnt angehängte Medien ab. 'image_to_video' animiert ein Bild oder interpoliert von einem Startframe zu einem Endframe, wenn zwei angehängt sind. 'reference_to_video' behandelt die angehängten Medien als Motivreferenzen. 'edit' überarbeitet genau ein angehängtes Video. (Standard: "auto") | COMBO | Ja | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Steuert die Zufälligkeit. Niedrigere Werte sind fokussierter/deterministischer, höhere Werte variabler. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 2.0 (Schritt 0.01) |
| `top_p` | Nucleus-Sampling: Auswahl aus dem kleinsten Token-Set, dessen kumulierte Wahrscheinlichkeit top_p erreicht. (Standard: 0.95) | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.01) |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Erweiterbarer Slot: Verbinden Sie bis zu 14 Bilder (`image_1`...`image_14`). Optionale Referenzbilder, um das Video zu steuern oder zu animieren. Bei der Aufgabe 'image_to_video' ist das erste das Startframe und ein optionales zweites das Endframe. | IMAGE | Nein | 0 bis 14 Bilder |
| `videos` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Videos (`video_1`...`video_3`). Optionale Referenzvideos zur Steuerung oder Bearbeitung. Jeweils bis zu 10 Sekunden lang. | VIDEO | Nein | 0 bis 3 Videos |

**Hinweise:**
- Der `prompt` darf nicht leer sein; der Node löst einen Fehler aus, wenn er leer ist.
- Die Aufgabe `text_to_video` generiert allein aus dem Prompt – das Anhängen von Bildern oder Videos löst einen Fehler aus.
- Die Aufgabe `image_to_video` akzeptiert nur Bilder (keine Videos) und erfordert genau 1 oder 2 Bilder: Das erste ist das Startframe und das optionale zweite das Endframe.
- Die Aufgabe `edit` (beide Modelle) und die Aufgabe `extend` (nur Omni Flash 1.1) erfordern genau ein Eingabevideo und behalten das Seitenverhältnis dieses Eingabevideos bei, wodurch `aspect_ratio` überschrieben wird.
- Es können höchstens 14 Bilder und 3 Videos angehängt werden, und jedes angehängte Video muss 10 Sekunden oder kürzer sein.
- Omni Flash gibt immer 720p-Video mit 24 FPS und Audio aus; die Auflösungsauswahl ist nur bei Omni Flash 1.1 verfügbar.
- Die Steuerelemente `temperature` und `top_p` sind nur beim Modell Omni Flash verfügbar; Omni Flash 1.1 verwendet feste Generierungseinstellungen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` (erste Ausgabe) | Das generierte Video mit Audio. Für Omni Flash: 720p, 24 FPS. Für Omni Flash 1.1: die im Eingabeparameter `resolution` ausgewählte Auflösung. | VIDEO |
| `text` (zweite Ausgabe) | Der vom Modell zusammen mit dem Video generierte Textinhalt (kann leer sein). | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/de.md)

---
**Source fingerprint (SHA-256):** `7a0dda4bcd662c9df3c680297ec9de7886d35e618de8b3ce0cd95b9afd13a892`
