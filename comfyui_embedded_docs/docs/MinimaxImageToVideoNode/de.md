# MiniMax Bild zu Video

Erzeugt synchron Videos auf Basis eines Bildes und eines Prompts sowie optionaler Parameter unter Verwendung der MiniMax-API. Dieser Node nimmt ein Eingabebild und eine Textbeschreibung entgegen, um eine Videosequenz zu erstellen; dabei stehen verschiedene Modelloptionen und Konfigurationseinstellungen zur Verfügung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Bild, das als erstes Frame der Videogenerierung verwendet wird | IMAGE | Ja | - |
| `prompt_text` | Text-Prompt zur Steuerung der Videogenerierung (Standard: leerer String) | STRING | Ja | - |
| `model` | Modell, das für die Videogenerierung verwendet wird (Standard: "I2V-01") | COMBO | Ja | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" |
| `seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0) | INT | Nein | 0 bis 18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videoausgabe | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `90eef1d58fa0ae4897ab19d702ecad707948eb79181ac4927dba650056e954c8`
