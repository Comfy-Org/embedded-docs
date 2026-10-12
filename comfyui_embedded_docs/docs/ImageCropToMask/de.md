# ImageCropToMask

Der Node schneidet ein Bild auf die Begrenzungsbox seiner Maske zu und erzeugt ein zentriertes Motiv vor einer einfarbigen Hintergrundfarbe. Der Node setzt das maskierte Bild über den gewählten Hintergrund zusammen und skaliert das Ergebnis auf die angegebenen Ausgabemaße, wodurch es für 3D-Pipelines geeignet ist, die ein zentriertes, hintergrundfreies Motiv in einer festen Auflösung erwarten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Das Eingabebild oder der Stapel von Bildern, der zugeschnitten werden soll. | IMAGE | Ja | — |
| `masks` | Die Maske oder der Stapel von Masken, die den Motivbereich definiert. Eine einzelne Maske wird auf alle Bilder angewendet; andernfalls muss die Stapelgröße der Maske mit der Stapelgröße der Bilder übereinstimmen. Wenn die Maskenauflösung von der Bildauflösung abweicht, wird die Maske automatisch angepasst. | MASK | Ja | — |
| `width` | Ausgabebreite in Pixeln. (Standard: 1024) | INT | Ja | 64 bis 4096 (Schritt 8) |
| `height` | Ausgabehöhe in Pixeln. (Standard: 1024) | INT | Ja | 64 bis 4096 (Schritt 8) |
| `pad_factor` | Zusätzlicher Rand um die Begrenzungsbox der Maske als Multiplikator. (Standard: 1.0) | FLOAT | Ja | 1.0 bis 2.0 (Schritt 0.01) |
| `grow_mask` | Vergrößert oder verkleinert die Maske um diese Anzahl von Pixeln vor dem Zuschneiden. Positive Werte erweitern die Maske, negative Werte verkleinern sie. (Standard: 0) | INT | Ja | -32 bis 32 (Schritt 1) |
| `background` | Hintergrundfarbe hinter dem maskierten Motiv. (Standard: #000000) | COLOR | Ja | — |

Hinweis: Der Zuschneidebereich wird um die Begrenzungsbox der Maske zentriert und sein Seitenverhältnis entspricht `width` / `height`. Der Node erkennt und korrigiert automatisch eine invertierte Maske (Vordergrundpixel entlang des Randes, Hintergrund in der Mitte). Wenn die Maske keine Vordergrundpixel enthält, versucht der Node die invertierte Maske; wenn diese ebenfalls leer ist, protokolliert er eine Warnung und schneidet das gesamte Bild zu. Ein Fehler wird ausgelöst, wenn die Stapelgröße der Maske nicht mit der Stapelgröße der Bilder übereinstimmt und es sich nicht um eine einzelne Maske handelt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `images` | Die zugeschnittenen zusammengesetzten Bilder (maskiertes Motiv vor der gewählten Hintergrundfarbe), skaliert auf `width` x `height`. Die Stapelgröße entspricht der Stapelgröße der Eingabebilder. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/de.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
