# ByteDance Seedance 2.5: Video aus erstem und letztem Frame

Dieser Node generiert ein Video aus einem erforderlichen Bild des ersten Frames und einem optionalen Bild des letzten Frames mithilfe von ByteDance Seedance-Modellen. Sie beschreiben das Video mit einem Text-Prompt; der erste Frame gibt den Start des Videos vor und der letzte Frame das Ende. Unterstützt werden Seedance 2.5 und die Seedance 2.0-Familie (Seedance 2.0, Seedance 2.0 Fast und Seedance 2.0 Mini). Wenn Sie das Modell `Seedance 2.5 Draft` auswählen, wird stattdessen eine schnelle 480p-Vorschau gerendert; verbinden Sie die resultierende `draft_task_id` mit dem Node „ByteDance Seedance 2.5 Draft to Final Video“, um das finale 1080p-Video zu rendern.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Seedance 2.5 für das neueste Modell, Videos bis zu 30 Sekunden und mp4-Ausgabe; Seedance 2.5 Draft für eine schnelle 480p-Vorschau, deren `draft_task_id`-Ausgabe das finale 1080p-Video im Node ByteDance Seedance 2.5 Draft to Final Video rendert; Seedance 2.0 für maximale Qualität und 4k; Fast für Geschwindigkeitsoptimierung; Mini für die schnellste, kostengünstigste Generierung. Die Auswahl eines Modells blendet unten modellspezifische Eingaben ein. | DYNAMIC_COMBO | Ja | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Bild des ersten Frames für das Video. | IMAGE | Nein | - |
| `last_frame` | Bild des letzten Frames für das Video. | IMAGE | Nein | - |
| `first_frame_asset_id` | Seedance asset_id zur Verwendung als erster Frame. Schließt sich gegenseitig mit dem Bildeingang `first_frame` aus. Standard ist eine leere Zeichenkette. | STRING | Nein | - |
| `last_frame_asset_id` | Seedance asset_id zur Verwendung als letzter Frame. Schließt sich gegenseitig mit dem Bildeingang `last_frame` aus. Standard ist eine leere Zeichenkette. | STRING | Nein | - |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard ist 0. | INT | Ja | 0 bis 2147483647 |
| `watermark` | Ob dem Video ein Wasserzeichen hinzugefügt werden soll. Standard ist False. | BOOLEAN | Ja | False<br>True |

### Seedance 2.5 Eingaben

Diese Eingaben erscheinen, wenn `Seedance 2.5` ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Setzen Sie gesprochene Zeilen in doppelte Anführungszeichen, um den generierten Dialog zu steuern. | STRING | Ja | - |
| `resolution` | Auflösung des Ausgabevideos. Standard ist 720p. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (4-30). Standard ist 5. | INT | Ja | 4 bis 30 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren. Standard ist True. | BOOLEAN | Ja | False<br>True |
| `output_format` | Containerformat des Ausgabevideos. Standard ist mp4. | COMBO | Ja | `"mp4"` |

### Seedance 2.5 Draft Eingaben

Diese Eingaben erscheinen, wenn `Seedance 2.5 Draft` ausgewählt ist. Der Parametersatz entspricht dem obigen Seedance 2.5, außer dass `resolution` nur `"480p"` anbietet (Standard `"480p"`).

### Seedance 2.0 Eingaben

Diese Eingaben erscheinen, wenn `Seedance 2.0` ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. | STRING | Ja | - |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Seitenverhältnis des Ausgabevideos. Standard ist `adaptive`, wodurch das nächstgelegene unterstützte Seitenverhältnis zum Seitenverhältnis des Eingabeframes verwendet wird. | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (4-15). Standard ist 7. | INT | Ja | 4 bis 15 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren. Standard ist True. | BOOLEAN | Ja | False<br>True |

### Seedance 2.0 Fast und Seedance 2.0 Mini Eingaben

Gemeinsam verwendet von `Seedance 2.0 Fast` und `Seedance 2.0 Mini`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. | STRING | Ja | - |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `ratio` | Seitenverhältnis des Ausgabevideos. Standard ist `adaptive`, wodurch das nächstgelegene unterstützte Seitenverhältnis zum Seitenverhältnis des Eingabeframes verwendet wird. | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (4-15). Standard ist 7. | INT | Ja | 4 bis 15 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren. Standard ist True. | BOOLEAN | Ja | False<br>True |

**Parametereinschränkungen**

- Sie müssen den ersten Frame entweder als `first_frame`-Bild oder als `first_frame_asset_id` bereitstellen. Wenn Sie beides angeben, wird ein Fehler ausgelöst; wenn Sie keines von beiden angeben, wird ebenfalls ein Fehler ausgelöst.
- Die Eingaben `last_frame` und `last_frame_asset_id` sind optional, aber Sie können nicht beide für denselben Frame angeben.
- Asset-IDs müssen auf vorhandene, aktive Seedance Image-Assets verweisen.
- Die Eingabe `prompt` ist erforderlich und darf nicht leer sein.
- Jeder Lauf gibt seine Task-ID als `draft_task_id` zurück, aber nur die ID eines Laufs mit `Seedance 2.5 Draft` kann vom Node ByteDance Seedance 2.5 Draft to Final Video gerendert werden. Bei jedem anderen Modell muss die Ausgabe unverbunden bleiben, andernfalls schlägt der Lauf fehl.
- Bei `Seedance 2.5` ist das Seitenverhältnis der Ausgabe immer adaptiv und folgt dem eigenen Seitenverhältnis des ersten Frames, daher wird keine Eingabe `ratio` angezeigt.
- Bei Modellen der Seedance 2.0-Familie und lokalen Frame-Bildern werden die Bilder vor der Generierung mittig zugeschnitten und auf die Zielauflösung und das Zielseitenverhältnis der Ausgabe skaliert. Wenn `ratio` `adaptive` ist, wird das nächstgelegene unterstützte Seitenverhältnis zum Eingabebild verwendet.
- Lokale Frame-Bilder werden auf unterstütztes Seitenverhältnis und unterstützte Abmessungen validiert; übergroße Bilder werden herunterskaliert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video. | VIDEO |
| `draft_task_id` | Vom Lauf zurückgegebene Task-ID. Nur ein Lauf mit `Seedance 2.5 Draft` erzeugt einen Draft, den der Node ByteDance Seedance 2.5 Draft to Final Video rendern kann; bei jedem anderen Modell muss die Ausgabe unverbunden bleiben, andernfalls schlägt der Lauf fehl. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
