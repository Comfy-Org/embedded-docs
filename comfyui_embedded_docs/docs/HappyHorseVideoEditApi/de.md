# HappyHorseVideoEditApi

Bearbeiten Sie ein Video mithilfe von Textanweisungen oder Referenzbildern mit dem HappyHorse-Modell. Die Ausgabedauer beträgt 3–15 Sekunden und entspricht dem Eingabevideo; Eingaben, die länger als 15 Sekunden sind, werden abgeschnitten.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das zu verwendende HappyHorse-Videobearbeitungsmodell. Diese Auswahl bestimmt, welche Optionen für Prompt, Auflösung, Seitenverhältnis und Referenzbild verfügbar sind. | DYNAMIC_COMBO | Ja | "happyhorse-1.0-video-edit" |
| `video` | Das zu bearbeitende Video. | VIDEO | Ja | 3 bis 60 Sekunden |
| `seed` | Seed, der für die Generierung verwendet werden soll (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `watermark` | Gibt an, ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: False). Erweiterter Parameter. | BOOLEAN | Ja | True<br>False |

### happyhorse-1.0-video-edit Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Bearbeitungsanweisungen oder Anforderungen für die Stilübertragung. Muss mindestens 1 Zeichen lang sein. | STRING | Ja | - |
| `resolution` | Die Ausgabauflösung. | COMBO | Ja | "720P"<br>"1080P" |
| `ratio` | Seitenverhältnis. Wenn nicht geändert, nähert es sich dem Seitenverhältnis des Eingabevideos an. | COMBO | Ja | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 0 bis 5 Referenzbilder (`image1`...`image5`), um die Bearbeitung zu steuern. | IMAGE | Nein | 0 bis 5 Bilder |

**Hinweis:** Das Eingabevideo muss 3 bis 60 Sekunden lang sein. Die Ausgabedauer beträgt 3–15 Sekunden und entspricht dem Eingabevideo; Eingabevideos, die länger als 15 Sekunden sind, werden abgeschnitten. Der `prompt` muss mindestens 1 Zeichen lang sein.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die bearbeitete Videoausgabe. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/de.md)

---
**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`
