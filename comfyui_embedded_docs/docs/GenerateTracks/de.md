# Videospuren generieren

Der Node `GenerateTracks` erzeugt mehrere parallele Bewegungsbahnen (Tracks) für die Videogenerierung. Er definiert einen Hauptpfad von einer Startposition zu einer Endposition und generiert dann eine Reihe von Tracks, die parallel zu diesem Pfad verlaufen und gleichmäßig voneinander beabstandet sind. Sie können die Form des Pfads (gerade Linie oder Bezier-Kurve), die Geschwindigkeit der Bewegung entlang des Pfads und die Frames steuern, in denen die Tracks sichtbar sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des Video-Frames in Pixeln. Der Standardwert ist 832. | INT | Ja | 16 - 4096 |
| `height` | Die Höhe des Video-Frames in Pixeln. Der Standardwert ist 480. | INT | Ja | 16 - 4096 |
| `start_x` | Normalisierte X-Koordinate (0-1) für die Startposition. Der Standardwert ist 0.0. | FLOAT | Ja | 0.0 - 1.0 |
| `start_y` | Normalisierte Y-Koordinate (0-1) für die Startposition. Der Standardwert ist 0.0. | FLOAT | Ja | 0.0 - 1.0 |
| `end_x` | Normalisierte X-Koordinate (0-1) für die Endposition. Der Standardwert ist 1.0. | FLOAT | Ja | 0.0 - 1.0 |
| `end_y` | Normalisierte Y-Koordinate (0-1) für die Endposition. Der Standardwert ist 1.0. | FLOAT | Ja | 0.0 - 1.0 |
| `num_frames` | Die Gesamtzahl der Frames, für die Trackpositionen generiert werden sollen. Der Standardwert ist 81. | INT | Ja | 1 - 1024 |
| `num_tracks` | Die Anzahl der zu generierenden parallelen Tracks. Der Standardwert ist 5. | INT | Ja | 1 - 100 |
| `track_spread` | Normalisierter Abstand zwischen den Tracks. Die Tracks werden senkrecht zur Bewegungsrichtung verteilt. Der Standardwert ist 0.025. | FLOAT | Ja | 0.0 - 1.0 |
| `bezier` | Aktiviert einen Bezier-Kurvenpfad unter Verwendung des Mittelpunkts als Kontrollpunkt. Der Standardwert ist False. | BOOLEAN | Ja | True / False |
| `mid_x` | Normalisierter X-Kontrollpunkt für die Bezier-Kurve. Wird nur verwendet, wenn `bezier` aktiviert ist. Der Standardwert ist 0.5. | FLOAT | Ja | 0.0 - 1.0 |
| `mid_y` | Normalisierter Y-Kontrollpunkt für die Bezier-Kurve. Wird nur verwendet, wenn `bezier` aktiviert ist. Der Standardwert ist 0.5. | FLOAT | Ja | 0.0 - 1.0 |
| `interpolation` | Steuert das Timing/die Geschwindigkeit der Bewegung entlang des Pfads (Standard: "linear"):<br>"linear" – konstante Geschwindigkeit<br>"ease_in" – beginnt langsam und beschleunigt<br>"ease_out" – beginnt schnell und wird langsamer<br>"ease_in_out" – sanfte Beschleunigung und Verlangsamung<br>"constant" – behält alle Positionen am Startpunkt | COMBO | Ja | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | Optionale Maske, die sichtbare Frames angibt. Falls angegeben, werden Frames, in denen die Maske mindestens ein Pixel ungleich null enthält, für alle Tracks als sichtbar markiert. | MASK | Nein | - |

**Hinweis:** Die Parameter `mid_x` und `mid_y` werden nur verwendet, wenn der Parameter `bezier` auf `True` gesetzt ist. Wenn `bezier` `False` ist, verläuft der Pfad als gerade Linie vom Start- zum Endpunkt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `TRACKS` | Ein Tracks-Objekt, das die generierten Pfadkoordinaten und Sichtbarkeitsinformationen für alle Tracks über alle Frames enthält. | TRACKS |
| `track_length` | Die Anzahl der Frames, für die Tracks generiert wurden, entsprechend der Eingabe `num_frames`. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/de.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
