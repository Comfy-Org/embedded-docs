# PixVerse Image to Video

Erzeugt ein Video aus einem Standbild und einem Text-Prompt mit PixVerse. Der Node lädt das Eingabebild hoch, wendet die ausgewählten Qualitäts-, Dauer- und Bewegungseinstellungen an und gibt anschließend das resultierende Video zurück, sobald die Generierung abgeschlossen ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image` | Eingabebild, das in ein Video umgewandelt werden soll | IMAGE | Ja | - |
| `prompt` | Prompt für die Videogenerierung (Standard: leerer String) | STRING | Ja | - |
| `quality` | Videoqualitätseinstellung (Standard: res_540p) | COMBO | Ja | `res_540p`<br>`res_1080p` |
| `duration_seconds` | Dauer des generierten Videos in Sekunden | COMBO | Ja | `dur_2`<br>`dur_5`<br>`dur_10` |
| `motion_mode` | Bewegungsstil, der auf die Videogenerierung angewendet wird | COMBO | Ja | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `seed` | Seed für die Videogenerierung (Standard: 0) | INT | Ja | 0-2147483647 |
| `negative_prompt` | Optionale Textbeschreibung unerwünschter Elemente in einem Bild (Standard: leerer String) | STRING | Nein | - |
| `pixverse_template` | Optionale Vorlage zur Beeinflussung des Generierungsstils, erstellt vom PixVerse Template-Node | CUSTOM | Nein | - |

**Hinweis:** Bei Verwendung der 1080p-Qualität wird der Bewegungsmodus automatisch auf normal gesetzt und die Dauer auf 5 Sekunden begrenzt. Bei anderen Dauern als 5 Sekunden wird der Bewegungsmodus ebenfalls automatisch auf normal gesetzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Generiertes Video basierend auf dem Eingabebild und den Parametern | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`
