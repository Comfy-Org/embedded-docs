# Google Gemini Omni (Video)

Google Gemini Omni (Video) erzeugt anhand eines Text-Prompts ein Video mit Audio mithilfe der Gemini Omni Flash-Modelle von Google. Optional können Referenzbilder und/oder -videos angehängt werden, um das Ergebnis zu steuern oder vorhandenes Filmmaterial zu bearbeiten. Beschreiben Sie die gewünschte Länge direkt im Prompt: 3 bis 10 Sekunden für Omni Flash und Omni Flash 1.1, 3 bis 15 Sekunden für Omni Flash 1.2.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `Modell` | Das Gemini-Videomodell, das zur Erzeugung des Videos verwendet wird. | DYNAMIC_COMBO | Ja | "Omni Flash 1.2"<br>"Omni Flash 1.1"<br>"Omni Flash" |

### Omni Flash 1.2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Beschreiben Sie das zu erzeugende Video oder die auf ein angehängtes Video anzuwendende Bearbeitung. Geben Sie die Länge direkt im Prompt an, z. B. „ein 6-Sekunden-Clip" oder, für die Aufgabe 'extend', „um 5 Sekunden verlängern"; die erzeugte Länge kann 3 bis 15 Sekunden betragen, und 'extend' fügt höchstens 10 Sekunden hinzu. Die Ausgabe enthält Audio. (Standard: "") | STRING | Ja | - |
| `resolution` | Ausgabeauflösung. (Standard: "720p") | COMBO | Ja | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Ausgabe-Seitenverhältnis: 16:9 (Querformat) oder 9:16 (Hochformat). Die Aufgaben 'edit' und 'extend' behalten stattdessen das Seitenverhältnis des Eingabevideos bei. (Standard: "16:9") | COMBO | Ja | "16:9"<br>"9:16" |
| `task_type` | Was mit dem Prompt und den angehängten Medien geschehen soll. Bei 'auto' entscheidet das Modell. 'text_to_video' erzeugt ausschließlich aus dem Prompt und lehnt angehängte Medien ab. 'image_to_video' animiert ein Bild oder interpoliert zwischen einem Startbild und einem Endbild, wenn zwei angehängt sind. 'reference_to_video' behandelt die angehängten Medien als Motivreferenzen. 'edit' schreibt genau ein angehängtes Video neu, und 'extend' hängt neues Filmmaterial daran an, sodass die Ausgabe mit dem Eingabevideo beginnt. (Standard: "auto") | COMBO | Ja | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Omni Flash 1.1 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Beschreiben Sie das zu erzeugende Video oder die auf ein angehängtes Video anzuwendende Bearbeitung. Geben Sie die Länge direkt im Prompt an, z. B. „ein 6-Sekunden-Clip" oder, für die Aufgabe 'extend', „um 5 Sekunden verlängern"; die erzeugte Länge kann 3 bis 10 Sekunden betragen und ist standardmäßig 10. Die Ausgabe enthält Audio. (Standard: "") | STRING | Ja | - |
| `resolution` | Ausgabeauflösung. (Standard: "720p") | COMBO | Ja | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Ausgabe-Seitenverhältnis: 16:9 (Querformat) oder 9:16 (Hochformat). Die Aufgaben 'edit' und 'extend' behalten stattdessen das Seitenverhältnis des Eingabevideos bei. (Standard: "16:9") | COMBO | Ja | "16:9"<br>"9:16" |
| `task_type` | Was mit dem Prompt und den angehängten Medien geschehen soll. Bei 'auto' entscheidet das Modell. 'text_to_video' erzeugt ausschließlich aus dem Prompt und lehnt angehängte Medien ab. 'image_to_video' animiert ein Bild oder interpoliert zwischen einem Startbild und einem Endbild, wenn zwei angehängt sind. 'reference_to_video' behandelt die angehängten Medien als Motivreferenzen. 'edit' schreibt genau ein angehängtes Video neu, und 'extend' hängt neues Filmmaterial daran an, sodass die Ausgabe mit dem Eingabevideo beginnt. (Standard: "auto") | COMBO | Ja | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Omni Flash Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Beschreiben Sie das zu erzeugende Video oder die auf ein angehängtes Video anzuwendende Bearbeitung. Geben Sie die Länge direkt im Prompt an, z. B. „ein 6-Sekunden-Clip"; die Länge kann 3 bis 10 Sekunden betragen. Die Ausgabe ist 720p, 24 FPS, mit Audio. (Standard: "") | STRING | Ja | - |
| `aspect_ratio` | Ausgabe-Seitenverhältnis: 16:9 (Querformat) oder 9:16 (Hochformat). Die Aufgabe 'edit' behält stattdessen das Seitenverhältnis des Eingabevideos bei. (Standard: "16:9") | COMBO | Ja | "16:9"<br>"9:16" |
| `task_type` | Was mit dem Prompt und den angehängten Medien geschehen soll. Bei 'auto' entscheidet das Modell. 'text_to_video' erzeugt ausschließlich aus dem Prompt und lehnt angehängte Medien ab. 'image_to_video' animiert ein Bild oder interpoliert zwischen einem Startbild und einem Endbild, wenn zwei angehängt sind. 'reference_to_video' behandelt die angehängten Medien als Motivreferenzen. 'edit' schreibt genau ein angehängtes Video neu. (Standard: "auto") | COMBO | Ja | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Steuert die Zufälligkeit. Niedrigere Werte sind fokussierter/deterministischer, höhere Werte vielfältiger. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 2.0 (Schritt 0.01) |
| `top_p` | Nucleus-Sampling: Auswahl aus dem kleinsten Token-Set, dessen kumulierte Wahrscheinlichkeit top_p erreicht. (Standard: 0.95) | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.01) |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `images` | Erweiterbarer Slot: Verbinden Sie bis zu 14 Bilder (`image_1`...`image_14`). Optionale Referenzbild(er) zur Steuerung oder Animation des Videos. Bei der Aufgabe 'image_to_video' ist das erste Bild das Startbild und ein optionales zweites Bild das Endbild. | IMAGE | Nein | 0 bis 14 Bilder |
| `videos` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Videos (`video_1`...`video_3`). Optionale Referenzvideos zur Steuerung oder Bearbeitung. Jeweils bis zu 10 Sekunden lang. | VIDEO | Nein | 0 bis 3 Videos |

**Hinweise:**
- Der `prompt` darf nicht leer sein; andernfalls gibt der Node einen Fehler aus.
- Die Aufgabe `text_to_video` erzeugt ausschließlich aus dem Prompt – das Anhängen von Bildern oder Videos führt zu einem Fehler.
- Die Aufgabe `image_to_video` akzeptiert nur Bilder (keine Videos) und erfordert genau 1 oder 2 Bilder: Das erste ist das Startbild und das optionale zweite das Endbild.
- Die Aufgabe `edit` (alle Modelle) und die Aufgabe `extend` (nur Omni Flash 1.1 und 1.2) erfordern genau ein Eingabevideo und behalten das Seitenverhältnis dieses Eingabevideos bei, wodurch `aspect_ratio` überschrieben wird.
- Es können höchstens 14 Bilder und 3 Videos angehängt werden. Jedes angehängte Video muss 10 Sekunden oder kürzer sein, 15 Sekunden oder kürzer mit Omni Flash 1.2, und 25 Sekunden oder kürzer für die Aufgabe `extend`, deren Ergebnis höchstens 30 Sekunden lang sein kann.
- Omni Flash gibt immer ein 720p-Video mit 24 FPS und Audio aus; die Auflösungsauswahl ist nur mit Omni Flash 1.1 und 1.2 verfügbar.
- Die Steuerungen `temperature` und `top_p` sind nur beim Omni Flash-Modell verfügbar; Omni Flash 1.1 und 1.2 verwenden feste Generierungseinstellungen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `video` (erste Ausgabe) | Das erzeugte Video mit Audio. Für Omni Flash: 720p, 24 FPS. Für Omni Flash 1.1 und 1.2: die im Eingabeparameter `resolution` ausgewählte Auflösung. | VIDEO |
| `text` (zweite Ausgabe) | Der zusammen mit dem Video vom Modell erzeugte Textinhalt (kann leer sein). | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/de.md)

---
**Source fingerprint (SHA-256):** `1fc6017d4d6fbce8f04b2f0ded496553074b8498e3b7342179550fc768698897`
