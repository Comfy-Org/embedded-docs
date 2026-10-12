# ByteDance Seedance 2.5 Text zu Video

Dieser Node erzeugt ein Video aus einem Text-Prompt unter Verwendung der Modelle Seedance 2.5 oder 2.0 von ByteDance. Er sendet den Prompt an das ausgewählte Modell, wartet, bis die Videoverarbeitung abgeschlossen ist, und gibt die resultierende Videodatei zurück. Wenn Sie das Modell `Seedance 2.5 Draft` auswählen, wird stattdessen eine schnelle 480p-Vorschau gerendert; verbinden Sie die resultierende `draft_task_id` mit dem ByteDance Seedance 2.5 Draft to Final Video Node, um das 1080p-Finale zu rendern.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Videogenerierung zu verwendende Seedance-Modell. Seedance 2.5 ist das neueste Modell und unterstützt Videos bis zu 30 Sekunden und mp4-Ausgabe; Seedance 2.5 Draft rendert eine schnelle 480p-Vorschau, deren Ausgabe `draft_task_id` im ByteDance Seedance 2.5 Draft to Final Video Node das 1080p-Finale rendert; Seedance 2.0 ist für maximale Qualität und 4k; Seedance 2.0 Fast ist für Geschwindigkeitsoptimierung; Seedance 2.0 Mini ist für die schnellste, kostengünstigste Generierung. Die Auswahl eines Modells blendet zusätzliche Eingaben für den Prompt, die Auflösung, das Seitenverhältnis, die Dauer und die Audiogenerierung ein. | DYNAMIC_COMBO | Ja | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Nein | 0 bis 2147483647 |
| `watermark` | Ob dem Video ein Wasserzeichen hinzugefügt werden soll. (Standard: False) Dies ist eine erweiterte Einstellung. | BOOLEAN | Nein | True / False |

### Seedance 2.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Setzen Sie gesprochene Dialogzeilen in doppelte Anführungszeichen, um den generierten Dialog zu steuern. | STRING | Ja | — |
| `resolution` | Auflösung des Ausgabevideos. (Standard: `"720p"`) | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Seitenverhältnis des Ausgabevideos. (Standard: `"16:9"`) | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden. (Standard: 5) | INT | Ja | 4 bis 30 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren. (Standard: True) | BOOLEAN | Ja | True / False |
| `output_format` | Containerformat des Ausgabevideos. (Standard: `"mp4"`) | COMBO | Ja | `"mp4"` |

### Seedance 2.5 Draft Eingaben

Diese Eingaben erscheinen, wenn `Seedance 2.5 Draft` ausgewählt ist. Der Parametersatz entspricht dem obigen Seedance 2.5, mit der Ausnahme, dass `resolution` nur `"480p"` anbietet (Standard: `"480p"`).

### Seedance 2.0 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. | STRING | Ja | — |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Seitenverhältnis des Ausgabevideos. (Standard: `"16:9"`) | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden. (Standard: 7) | INT | Ja | 4 bis 15 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren. (Standard: True) | BOOLEAN | Ja | True / False |

### Seedance 2.0 Fast und Seedance 2.0 Mini Eingaben

Gemeinsam genutzt von Seedance 2.0 Fast und Seedance 2.0 Mini; beide Modelle stellen dieselben Parameter bereit.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. | STRING | Ja | — |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `ratio` | Seitenverhältnis des Ausgabevideos. (Standard: `"16:9"`) | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Dauer des Ausgabevideos in Sekunden. (Standard: 7) | INT | Ja | 4 bis 15 |
| `generate_audio` | Audiogenerierung für das Ausgabevideo aktivieren. (Standard: True) | BOOLEAN | Ja | True / False |

**Hinweis:** Die `model`-Auswahl ist dynamisch; die unter jedem Modellabschnitt angezeigten Eingaben erscheinen, wenn dieses Modell ausgewählt ist. Der Prompt muss nach Entfernen von Leerzeichen mindestens 1 Zeichen lang sein. Die Auflösungs- und Dauerbeschränkungen hängen vom ausgewählten Modell ab: Seedance 2.5 unterstützt 480p/720p/1080p und 4 bis 30 Sekunden, Seedance 2.0 unterstützt 480p/720p/1080p/4k und 4 bis 15 Sekunden, und Seedance 2.0 Fast und Seedance 2.0 Mini unterstützen nur 480p/720p und 4 bis 15 Sekunden; Seedance 2.5 Draft unterstützt nur 480p und 4 bis 30 Sekunden. Jeder Lauf gibt seine Task-ID als `draft_task_id` zurück, aber nur die ID eines `Seedance 2.5 Draft`-Laufs kann vom ByteDance Seedance 2.5 Draft to Final Video Node gerendert werden; bei jedem anderen Modell muss die Ausgabe unverbunden bleiben, andernfalls schlägt der Lauf fehl. Der Wert `seed` steuert nur, ob der Node erneut ausgeführt wird; er macht die Ergebnisse nicht deterministisch.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die generierte Videodatei. | VIDEO |
| `draft_task_id` | Task-ID, die vom Lauf zurückgegeben wird. Nur ein Lauf mit `Seedance 2.5 Draft` erzeugt einen Entwurf, den der ByteDance Seedance 2.5 Draft to Final Video Node rendern kann; bei jedem anderen Modell muss die Ausgabe unverbunden bleiben, andernfalls schlägt der Lauf fehl. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `2abad0c4eab5a1286c8da9237bcec52b275c40188b3b7dc9eede5d5f4cbb11d3`
