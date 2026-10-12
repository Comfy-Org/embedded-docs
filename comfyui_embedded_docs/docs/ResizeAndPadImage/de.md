# ResizeAndPadImage

Der Node ResizeAndPadImage ändert die Größe eines Bildes, sodass es in vorgegebene Abmessungen passt, während das ursprüngliche Seitenverhältnis erhalten bleibt. Er skaliert das Bild proportional herunter, um in die Zielbreite und -höhe zu passen, und fügt anschließend an den Rändern Padding hinzu, um verbleibenden Platz auszufüllen. Die Padding-Farbe und die Interpolationsmethode können angepasst werden, um das Erscheinungsbild der aufgefüllten Bereiche und die Qualität der Größenänderung zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, dessen Größe geändert und das aufgefüllt werden soll | IMAGE | Ja | - |
| `target_width` | Die gewünschte Breite des Ausgabebilds (Standard: 512) | INT | Ja | 1 bis MAX_RESOLUTION |
| `target_height` | Die gewünschte Höhe des Ausgabebilds (Standard: 512) | INT | Ja | 1 bis MAX_RESOLUTION |
| `padding_color` | Die Farbe für die Padding-Bereiche um das skalierte Bild (Standard: „white“) | COMBO | Ja | "white"<br>"black" |
| `interpolation` | Die Interpolationsmethode, die zum Skalieren des Bildes verwendet wird (Standard: „area“) | COMBO | Ja | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das skalierte und aufgefüllte Ausgabebild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/de.md)

---
**Source fingerprint (SHA-256):** `cc516caee9f466d557e1c8e3c7fcef25acc1e33d181bc4b100302dc93530cb95`
