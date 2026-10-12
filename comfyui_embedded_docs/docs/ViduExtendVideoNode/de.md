# Vidu-Videoerweiterung

Der Vidu Video Extension-Node erzeugt zusätzliche Frames, um die Länge eines vorhandenen Videos zu verlängern. Er verwendet ein angegebenes KI-Modell, um basierend auf dem Quellvideo und einem optionalen Text-Prompt eine Fortsetzung zu erstellen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das für die Videoerweiterung verwendet werden soll. Die Auswahl eines Modells zeigt seine spezifischen Dauer- und Auflösungseinstellungen an. | DYNAMIC_COMBO | Ja | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `video` | Das Quellvideo, das erweitert werden soll. | VIDEO | Ja | - |
| `prompt` | Ein optionaler Text-Prompt für das erweiterte Video (max. 2000 Zeichen; Standard: leer). | STRING | Ja | - |
| `seed` | Ein Seed-Wert zur Steuerung der Zufälligkeit der Generierung (Standard: 1). | INT | Ja | 0 bis 2147483647 |
| `end_frame` | Ein optionales Bild, das als Ziel-Endframe für die Erweiterung verwendet werden soll. | IMAGE | Nein | - |

### viduq2-pro und viduq2-turbo Eingaben

Diese Einstellungen gelten für beide Modelle.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `duration` | Dauer des erweiterten Videos in Sekunden (Standard: 4). Diese Einstellung erscheint nach der Auswahl eines Modells. | INT | Ja | 1 bis 7 |
| `resolution` | Auflösung des Ausgabevideos. Diese Einstellung erscheint nach der Auswahl eines Modells. | COMBO | Ja | `"720p"`<br>`"1080p"` |

**Hinweis:** Das Quellvideo `video` muss eine Dauer zwischen 4 und 55 Sekunden haben. Wenn `end_frame` angegeben wird, muss sein Seitenverhältnis zwischen 1:4 und 4:1 liegen, und seine Breite und Höhe müssen jeweils mindestens 128 Pixel betragen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die neu generierte Videodatei, die das erweiterte Material enthält. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
