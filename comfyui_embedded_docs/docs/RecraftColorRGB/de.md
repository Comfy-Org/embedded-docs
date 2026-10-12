# RecraftColorRGB

Erstellen Sie eine Recraft-Farbe, indem Sie einzelne Rot-, Grün- und Blauwerte angeben. Dieser Node nimmt ganzzahlige RGB-Werte (0-255) entgegen und konvertiert sie in ein Recraft-Farbformat, das in anderen Recraft-Operationen verwendet werden kann. Optional können Sie auch eine vorhandene Recraft-Farbkette bereitstellen, um sie um die neue Farbe zu erweitern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `r` | Rotwert der Farbe (Standard: 0) | INT | Ja | 0-255 |
| `g` | Grünwert der Farbe (Standard: 0) | INT | Ja | 0-255 |
| `b` | Blauwert der Farbe (Standard: 0) | INT | Ja | 0-255 |
| `recraft_color` | Optionale vorhandene Recraft-Farbkette, die um die neue RGB-Farbe erweitert werden soll | COLOR | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `recraft_color` | Das erstellte Recraft-Farbobjekt, das die angegebenen RGB-Werte enthält, oder die erweiterte Farbkette, wenn eine vorhandene bereitgestellt wurde | COLOR |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/de.md)

---
**Source fingerprint (SHA-256):** `2246d266bc36d1aa7f115402b049f895f2b15d0085b84d1b0a813cdfb1b6e2fc`
