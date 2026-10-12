# ByteDance2ReferenceNode

Dieser Node generiert, bearbeitet oder erweitert Videos mithilfe der KI-Modelle Seedance 2.5 oder Seedance 2.0 von ByteDance. Sie beschreiben das Video in einem Text-Prompt und können Referenzbilder, -videos und -audios anhängen, um das Ergebnis zu steuern; unterstützt werden multimodale Referenzen, Videobearbeitung und Videoerweiterung. Dies ist die Legacy-Version des Seedance-Referenz-zu-Video-Nodes; sie ist veraltet und wird nicht mehr empfohlen.

## Eingaben

Die Auswahl von `model` bestimmt, welche der unten aufgeführten Parameter verfügbar sind. `video_editing` und `output_format` erscheinen nur, wenn Seedance 2.5 ausgewählt ist. Die erweiterbaren Referenz-Slots und die Optionen zur automatischen Größenanpassung von Referenzvideos werden von allen Modellen gemeinsam genutzt und sind unter Referenzeingaben beschrieben.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das KI-Modell, das zur Videogenerierung verwendet wird. Seedance 2.5 für das neueste Modell, Videos bis zu 30 Sekunden und mp4/mov-Ausgabe; Seedance 2.0 für maximale Qualität und 4k; Fast für Geschwindigkeitsoptimierung; Mini für die schnellste und kostengünstigste Generierung. Die Auswahl eines Modells blendet die unten aufgeführten modellspezifischen Eingaben ein. | DYNAMIC_COMBO | Ja | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647<br>Schritt: 1 |
| `watermark` | Gibt an, ob dem Video ein Wasserzeichen hinzugefügt werden soll (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | `True`<br>`False` |

### Seedance 2.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Setzen Sie gesprochene Zeilen in doppelte Anführungszeichen, um den generierten Dialog zu steuern. Muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist (Standard: leer). | STRING | Ja | Beliebiger Text |
| `resolution` | Auflösung des Ausgabevideos (Standard: `"720p"`). | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Seitenverhältnis des Ausgabevideos (Standard: `"16:9"`). | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 4 bis 30<br>Schritt: 1 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |
| `video_editing` | Aktivieren, wenn der Prompt ein verbundenes Referenzvideo bearbeitet, beispielsweise um ein Objekt darin zu ersetzen. Die Ausgabe behält dann die eigene Länge und das Seitenverhältnis des Quellclips bei, und die Widgets für Dauer und Seitenverhältnis werden ignoriert. Deaktiviert lassen, um ein neues Video zu generieren oder eines auf die von Ihnen festgelegte Dauer zu verlängern (Standard: False). | BOOLEAN | Ja | `True`<br>`False` |
| `output_format` | Containerformat des Ausgabevideos (Standard: `"mp4"`). | COMBO | Ja | `"mp4"` |

### Seedance 2.0 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist (Standard: leer). | STRING | Ja | Beliebiger Text |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Seitenverhältnis des Ausgabevideos (Standard: `"adaptive"`). | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 7). | INT | Ja | 4 bis 15<br>Schritt: 1 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |

### Seedance 2.0 Fast und Seedance 2.0 Mini Eingaben

Gemeinsam genutzt von Seedance 2.0 Fast und Seedance 2.0 Mini. Diese beiden Modelle bieten denselben Eingabesatz wie Seedance 2.0, mit der Ausnahme, dass `resolution` auf 480p und 720p beschränkt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist (Standard: leer). | STRING | Ja | Beliebiger Text |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `ratio` | Seitenverhältnis des Ausgabevideos (Standard: `"adaptive"`). | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 7). | INT | Ja | 4 bis 15<br>Schritt: 1 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |

### Referenzeingaben

Für alle Modelle verfügbar. Die maximale Anzahl von Slots hängt vom ausgewählten Modell ab: Seedance 2.5 unterstützt mehr Referenzen als die Seedance 2.0-Modelle.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzbilder (`image_1`, `image_2`, ...), die die Videogenerierung steuern. Bilder werden automatisch auf eine maximale Seitenlänge von 6000 Pixeln herunterskaliert und müssen mindestens 300x300 Pixel groß sein, mit einem Seitenverhältnis zwischen 0,4 und 2,5. | IMAGE | Nein | Bis zu 30 (Seedance 2.5)<br>Bis zu 9 (Seedance 2.0-Modelle) |
| `reference_videos` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzvideos (`video_1`, `video_2`, ...), die die Videogenerierung steuern; wird für Videobearbeitung und Videoerweiterung verwendet. | VIDEO | Nein | Bis zu 10 (Seedance 2.5)<br>Bis zu 3 (Seedance 2.0-Modelle) |
| `reference_audios` | Erweiterbarer Slot: Verbinden Sie einen oder mehrere Referenz-Audioclips (`audio_1`, `audio_2`, ...), die die Videogenerierung steuern. | AUDIO | Nein | Bis zu 10 (Seedance 2.5)<br>Bis zu 3 (Seedance 2.0-Modelle) |
| `auto_downscale` | Referenzvideos automatisch herunterskalieren, die das Pixelbudget des Modells für die ausgewählte Auflösung überschreiten. Das Seitenverhältnis bleibt erhalten; Videos, die bereits innerhalb der Grenzen liegen, werden nicht verändert (Standard: True). | BOOLEAN | Nein | `True`<br>`False` |
| `auto_upscale` | Erweiterte Einstellung. Referenzvideos automatisch hochskalieren, die unter der minimalen Pixelanzahl des Modells für die ausgewählte Auflösung liegen. Das Seitenverhältnis bleibt erhalten; Videos, die das Minimum bereits erfüllen, werden nicht verändert. Hinweis: Das Hochskalieren einer niedrig aufgelösten Quelle fügt keine echten Details hinzu und kann Generierungen mit geringerer Qualität erzeugen (Standard: False). | BOOLEAN | Nein | `True`<br>`False` |
| `reference_assets` | Erweiterbarer Slot: IDs zuvor erstellter Seedance-Assets aus der virtuellen Bibliothek (Bild, Video oder Audio), die als Referenzen verwendet werden sollen (`asset_1`, `asset_2`, ...). Jedes Asset muss existieren und den Status Aktiv haben. Im Prompt können Assets als `asset1`, `asset 1` usw. referenziert werden; der Node ersetzt diese Tokens durch Bezeichnungen wie "Image 2". | STRING | Nein | Bis zu 30 (Seedance 2.5)<br>Bis zu 9 (Seedance 2.0-Modelle) |

**Wichtige Einschränkungen:**

* Mindestens eine Referenz ist erforderlich. Für Seedance 2.0, 2.0 Fast und 2.0 Mini müssen Sie mindestens eine Bild- oder Video-Referenz bereitstellen (über `reference_images`, `reference_videos` oder einen Bild- oder Video-Eintrag in `reference_assets`). Seedance 2.5 akzeptiert zusätzlich reine Audio-Referenzen (über `reference_audios` oder einen Audio-Eintrag in `reference_assets`).
* Die Referenzanzahl ist modellabhängig und wird über direkte Eingaben und Asset-Referenzen zusammen validiert: Seedance 2.5 erlaubt bis zu 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` und 30 `reference_assets`; die Seedance 2.0-Modelle erlauben bis zu 9 Bilder, 3 Videos, 3 Audioclips und 9 Assets.
* Jedes Referenzvideo muss mindestens 1,8 Sekunden lang sein, und jeder Referenz-Audioclip muss mindestens 1,8 Sekunden lang sein. Die Gesamtdauer aller Referenzvideos und aller Referenzaudios muss innerhalb des Limits des ausgewählten Modells bleiben (15,1 Sekunden für die Seedance 2.0-Modelle).
* Referenzvideos müssen außerdem die Pixelanzahl-Grenzen des Modells für die ausgewählte Auflösung erfüllen. Wenn `auto_downscale` aktiviert ist (Standard), werden übergroße Videos automatisch angepasst; wenn `auto_upscale` aktiviert ist, werden zu kleine Videos vergrößert. Wenn eine der automatischen Anpassungen deaktiviert ist, lösen Videos außerhalb der entsprechenden Grenze einen Fehler aus.
* Wenn `video_editing` bei Seedance 2.5 aktiviert ist, werden die Eingaben `duration` und `ratio` ignoriert; die Ausgabe entspricht der eigenen Länge und dem Seitenverhältnis des Referenzvideos. Wenn der Anbieter den Prompt als Bearbeitung eines Referenzvideos interpretiert, schlägt die Generierung fehl, es sei denn, `video_editing` ist aktiviert oder der Prompt wird umformuliert, um ein neues Video zu beschreiben.
* Wenn der Anbieter die für das Video generierte Audiospur ablehnt (zum Beispiel wegen einer möglichen Urheberrechtsübereinstimmung), schlägt die Aufgabe fehl; das Deaktivieren von `generate_audio` erzeugt ein stummes Video.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/de.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
