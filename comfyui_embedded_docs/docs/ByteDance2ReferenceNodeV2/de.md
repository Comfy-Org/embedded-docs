# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video erzeugt, bearbeitet oder erweitert Videos mit ByteDance Seedance-Modellen (Seedance 2.5, 2.5 Draft, 2.0, 2.0 Fast und 2.0 Mini), gesteuert durch einen Text-Prompt und optionale Referenzbilder, -videos, -audios oder zuvor hochgeladene Bibliotheks-Assets. Der Node lädt die Referenzen hoch, übermittelt eine Generierungsaufgabe, wartet auf deren Abschluss und gibt die fertige Videodatei zurück. Wenn Sie `Seedance 2.5 Draft` auswählen, wird stattdessen eine schnelle 480p-Vorschau gerendert; verbinden Sie die resultierende `draft_task_id` mit dem Node ByteDance Seedance 2.5 Draft to Final Video, um das 1080p-Final zu rendern.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Modellauswahl. Seedance 2.5 für das neueste Modell, Videos bis zu 30 Sekunden und mp4-Ausgabe; Seedance 2.5 Draft für eine schnelle 480p-Vorschau, deren `draft_task_id`-Ausgabe das 1080p-Final im Node ByteDance Seedance 2.5 Draft to Final Video rendert; Seedance 2.0 für maximale Qualität und 4k; Fast für Geschwindigkeitsoptimierung; Mini für die schnellste, kostengünstigste Generierung. Die Auswahl eines Modells ändert die unten angezeigten Eingabe-Widgets. | DYNAMIC_COMBO | Ja | "Seedance 2.5"<br>"Seedance 2.5 Draft"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 0. | INT | Ja | 0 bis 2147483647 |
| `watermark` | Gibt an, ob dem Video ein Wasserzeichen hinzugefügt wird. Standard: False. Erweiterte Einstellung. | BOOLEAN | Ja | true<br>false |

### Seedance 2.5 Eingaben

Diese Eingaben erscheinen, wenn `model` auf "Seedance 2.5" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt für die Videogenerierung. Setzen Sie gesprochene Zeilen in doppelte Anführungszeichen, um den generierten Dialog zu steuern. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos. Standard: 720p. | COMBO | Ja | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Seitenverhältnis des Ausgabevideos. Standard: 16:9. | COMBO | Ja | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Dauer des Ausgabevideos in Sekunden (4-30). Standard: 5. | INT | Ja | 4 bis 30 |
| `generate_audio` | Aktiviert die Audiogenerierung für das Ausgabevideo. Standard: True. | BOOLEAN | Ja | true<br>false |
| `task_type` | Was mit den Referenzmedien gemacht werden soll. Jeder Wert außer auto wird beim Absenden der Aufgabe validiert, sodass nicht passende Einstellungen fehlschlagen, bevor die Generierung beginnt.<br>auto: Das Modell leitet die Aufgabe aus dem Prompt und den Eingaben ab; Einstellungen, die seiner Interpretation widersprechen, schlagen erst fehl, nachdem die Generierung begonnen hat.<br>reference: Generiert ein neues Video, gesteuert durch die Referenzbilder, -videos und -audios.<br>edit: Ändert ein verbundenes Referenzvideo (hinzufügen, entfernen, ersetzen); die Ausgabe behält die eigene Länge und das Seitenverhältnis des Quellclips, und die Widgets `duration` und `ratio` werden ignoriert.<br>extend: Setzt ein verbundenes Referenzvideo vorwärts oder rückwärts fort; der Prompt sollte "extend forward", "extend backward" oder "continue" lauten, das Seitenverhältnis folgt dem Quellclip, und die Ausgabe enthält nur das neu generierte Segment in der von Ihnen festgelegten Dauer, nicht den Quellclip. Standard: auto. | COMBO | Ja | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Containerformat des Ausgabevideos. Standard: mp4. | COMBO | Ja | "mp4" |

### Seedance 2.5 Draft Eingaben

Diese Eingaben erscheinen, wenn `model` auf "Seedance 2.5 Draft" gesetzt ist. Der Parametersatz entspricht dem obigen Seedance 2.5, außer dass `resolution` nur `"480p"` anbietet (Standard `"480p"`).

### Seedance 2.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf "Seedance 2.0" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt für die Videogenerierung. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Seitenverhältnis des Ausgabevideos. Standard: adaptive. | COMBO | Ja | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Dauer des Ausgabevideos in Sekunden (4-15). Standard: 7. | INT | Ja | 4 bis 15 |
| `generate_audio` | Aktiviert die Audiogenerierung für das Ausgabevideo. Standard: True. | BOOLEAN | Ja | true<br>false |

### Seedance 2.0 Fast und Seedance 2.0 Mini Eingaben

Diese Eingaben erscheinen, wenn `model` auf "Seedance 2.0 Fast" oder "Seedance 2.0 Mini" gesetzt ist. Beide Modelle verwenden denselben Eingabesatz.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt für die Videogenerierung. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | "480p"<br>"720p" |
| `ratio` | Seitenverhältnis des Ausgabevideos. Standard: adaptive. | COMBO | Ja | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Dauer des Ausgabevideos in Sekunden (4-15). Standard: 7. | INT | Ja | 4 bis 15 |
| `generate_audio` | Aktiviert die Audiogenerierung für das Ausgabevideo. Standard: True. | BOOLEAN | Ja | true<br>false |

### Referenzeingaben

Diese erweiterbaren Referenz-Slots sind für alle Modelle verfügbar. Die maximale Anzahl an Slots unterscheidet sich je Modell: Seedance 2.5 unterstützt bis zu 30 Bilder, 10 Videos, 10 Audios und 30 Assets; Seedance 2.0, 2.0 Fast und 2.0 Mini unterstützen bis zu 9 Bilder, 3 Videos, 3 Audios und 9 Assets.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 1..N Referenzbilder, die die Ausgabe steuern. Das Anzahllimit gilt pro Modell (siehe Modellabschnitte). Bilder werden auf ihr Seitenverhältnis (0,4 bis 2,5) validiert und automatisch auf eine maximale Seitenlänge von 6000 Pixeln herunterskaliert. | IMAGE | Nein | 1..9 Slots (Seedance 2.0-Familie)<br>1..30 Slots (Seedance 2.5) |
| `reference_videos` | Erweiterbarer Slot: Verbinden Sie 1..N Referenzvideos. Das Anzahllimit gilt pro Modell (siehe Modellabschnitte). Jedes Video muss mindestens 1,8 Sekunden lang sein und muss in die Pixelgrenzen für das ausgewählte Modell und die Auflösung passen. | VIDEO | Nein | 1..3 Slots (Seedance 2.0-Familie)<br>1..10 Slots (Seedance 2.5) |
| `reference_audios` | Erweiterbarer Slot: Verbinden Sie 1..N Referenz-Audiospuren. Das Anzahllimit gilt pro Modell (siehe Modellabschnitte). Jedes Audio muss mindestens 1,8 Sekunden lang sein. | AUDIO | Nein | 1..3 Slots (Seedance 2.0-Familie)<br>1..10 Slots (Seedance 2.5) |
| `reference_assets` | Erweiterbarer Slot: Verbinden Sie 1..N Asset-ID-Strings für Medien, die bereits in die virtuelle Seedance-Bibliothek hochgeladen wurden. Jedes Asset muss Active sein. Sie können im Prompt mit Tokens wie `asset1` oder `asset 1` auf ein Asset verweisen; der Node ersetzt sie durch die Positionsbezeichnung des Assets (zum Beispiel "Image 2" oder "Video 1"). | STRING | Nein | 1..9 Slots (Seedance 2.0-Familie)<br>1..30 Slots (Seedance 2.5) |
| `auto_downscale` | Skaliert Referenzvideos automatisch herunter, die das Pixelbudget des Modells für die ausgewählte Auflösung überschreiten. Das Seitenverhältnis bleibt erhalten; Videos, die bereits innerhalb der Grenzen liegen, bleiben unverändert. Standard: True. | BOOLEAN | Nein | true<br>false |
| `auto_upscale` | Skaliert Referenzvideos automatisch hoch, die unter der minimalen Pixelanzahl des Modells für die ausgewählte Auflösung liegen. Das Seitenverhältnis bleibt erhalten; Videos, die das Minimum bereits erfüllen, bleiben unverändert. Hinweis: Das Hochskalieren einer niedrig aufgelösten Quelle fügt keine echten Details hinzu und kann Generierungen mit geringerer Qualität erzeugen. Standard: False. Erweiterte Einstellung. | BOOLEAN | Nein | true<br>false |

**Hinweis:** Zum Ausführen des Nodes ist mindestens ein Referenzbild, -video oder -Asset erforderlich (Seedance 2.5 akzeptiert auch reine Audio-Referenzen). Referenzvideos und -audios müssen jeweils mindestens 1,8 Sekunden lang sein, und die kombinierte Dauer aller Referenzvideos (und separat aller Referenz-Audios) darf die maximale Gesamtsekundenzahl des ausgewählten Modells nicht überschreiten. Referenzbilder müssen ein Seitenverhältnis zwischen etwa 2:5 und 5:2 (0,4 bis 2,5) haben, mindestens 300x300 Pixel groß sein und werden automatisch auf eine maximale Seitenlänge von 6000 Pixeln herunterskaliert. Die Optionen `task_type` "edit" und "extend" sind nur mit Seedance 2.5 verfügbar und erfordern beide mindestens ein Referenzvideo; bei Verwendung von "edit" behält die Ausgabe die eigene Länge und das Seitenverhältnis des Quellclips, und die Widgets `duration` und `ratio` werden ignoriert; bei Verwendung von "extend" enthält die Ausgabe nur das neu generierte Segment in der von Ihnen festgelegten Dauer. Referenzierte Assets müssen den Status Active haben, andernfalls schlägt die Aufgabe fehl. Jeder Lauf gibt seine Task-ID als `draft_task_id` zurück, aber nur die ID eines `Seedance 2.5 Draft`-Laufs kann vom Node ByteDance Seedance 2.5 Draft to Final Video gerendert werden; bei jedem anderen Modell muss die Ausgabe unverbunden bleiben, andernfalls schlägt der Lauf fehl.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `video` | Das generierte Video, das vom Anbieter heruntergeladen wird, sobald die Generierungsaufgabe abgeschlossen ist. Enthält Audio, wenn die Audiogenerierung aktiviert ist. | VIDEO |
| `draft_task_id` | Task-ID, die vom Lauf zurückgegeben wird. Nur ein `Seedance 2.5 Draft`-Lauf erzeugt einen Entwurf, den der Node ByteDance Seedance 2.5 Draft to Final Video rendern kann; bei jedem anderen Modell muss die Ausgabe unverbunden bleiben, andernfalls schlägt der Lauf fehl. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `12fee29b280ff71e29f268f52131d1c15cf3066e0804356b735b61d97c80a6a9`
