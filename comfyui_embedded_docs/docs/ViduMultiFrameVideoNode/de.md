# Vidu Multi-Frame-Videogenerierung

Dieser Node erzeugt ein Video, indem er Übergänge zwischen mehreren Keyframes erstellt. Er beginnt mit einem Startbild und animiert durch eine Abfolge benutzerdefinierter Endbilder und Prompts, wodurch eine einzelne Videodatei als Ausgabe entsteht.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Videogenerierung zu verwendende Vidu-Modell. | COMBO | Ja | "viduq2-pro"<br>"viduq2-turbo" |
| `start_image` | Das Startbild. Das Seitenverhältnis muss zwischen 1:4 und 4:1 liegen. | IMAGE | Ja | Seitenverhältnis 1:4 bis 4:1 |
| `seed` | Ein Seed-Wert für die Zufallszahlengenerierung, um reproduzierbare Ergebnisse zu gewährleisten (Standard: 1). | INT | Ja | 0 bis 2147483647 |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | "720p"<br>"1080p" |
| `frames` | Anzahl der Keyframe-Übergänge (2-9). Bei Auswahl eines Werts werden die erforderlichen Eingaben für jeden Frame dynamisch eingeblendet. | DYNAMIC_COMBO | Ja | "2"<br>"3"<br>"4"<br>"5"<br>"6"<br>"7"<br>"8"<br>"9" |

### Frame-Eingaben (gemeinsam genutzt von allen Optionen der Frame-Anzahl)

Wenn `frames` auf eine Zahl gesetzt ist, werden für jeden Frame `i` von 1 bis zu dieser Zahl die folgenden drei Eingaben angezeigt. Wenn beispielsweise "3" ausgewählt wird, werden `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2` und `prompt3` / `end_image3` / `duration3` hinzugefügt.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt{i}` | Text-Prompt für den Übergang von Frame {i}. Mehrzeiliges Textfeld. Maximal 2000 Zeichen. | STRING | Ja | Bis zu 2000 Zeichen |
| `end_image{i}` | Endbild für Segment {i}. Das Seitenverhältnis muss zwischen 1:4 und 4:1 liegen. | IMAGE | Ja | Seitenverhältnis 1:4 bis 4:1 |
| `duration{i}` | Dauer für Segment {i} in Sekunden (Standard: 4). | INT | Ja | 2 bis 7 |

**Hinweise:**

- Alle Eingaben sind erforderlich. `seed` hat einen Standardwert, ist aber dennoch eine erforderliche Eingabe.
- `start_image` und jedes `end_image{i}` müssen ein Seitenverhältnis zwischen 1:4 und 4:1 haben.
- Jedes `prompt{i}` hat eine maximale Länge von 2000 Zeichen.
- Jedes `duration{i}` muss zwischen 2 und 7 Sekunden liegen.
- Die Anzahl der Frames kann zwischen 2 und 9 liegen, daher reichen die möglichen Frame-Indizes von 1 bis 9.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei mit allen animierten Übergängen. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
