# CenterCropImages

Der Node „Center Crop Images“ schneidet ein Bild von der Mitte auf eine angegebene Breite und Höhe zu. Er berechnet den zentralen Bereich des Eingabebilds und extrahiert einen rechteckigen Bereich mit den definierten Abmessungen. Ist die angeforderte Zuschnittgröße größer als das Bild, wird der Zuschnitt auf die Grenzen des Bildes beschränkt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, das zugeschnitten werden soll. | IMAGE | Ja | - |
| `width` | Die Breite des Zuschnittbereichs (Standard: 512). | INT | Ja | 1 bis 8192 |
| `height` | Die Höhe des Zuschnittbereichs (Standard: 512). | INT | Ja | 1 bis 8192 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das resultierende Bild nach dem mittigen Zuschnitt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/de.md)

---
**Source fingerprint (SHA-256):** `1b22529602e3aca816b583158c4bb5aa51de3478ac8068c2a69a3392fb12746f`
