# Textüberlagerung zeichnen

Dieser Node zeichnet Text über ein Bild oder einen Batch von Bildern. Er erstellt ein Text-Overlay mit konfigurierbarer Schriftgröße, Farbe, vertikaler Position, horizontaler Ausrichtung und optionaler schwarzer Kontur und kombiniert das Overlay anschließend mit den Originalbildpixeln.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Das Eingabebild oder der Batch von Bildern, auf die Text gezeichnet werden soll | IMAGE | Ja | |
| `text` | Der auf das Bild zu legende Text (Standard: ""). Unterstützt mehrere Zeilen: Die Escape-Sequenzen `\n` und `\t` werden in Zeilenumbrüche und Tabulatoren umgewandelt, und lange Zeilen werden automatisch umgebrochen, damit sie in die Bildbreite passen. | STRING | Ja | |
| `font_size` | Schriftgröße als Prozentsatz der Bildhöhe (Standard: 5.0) | FLOAT | Ja | 0.5 bis 50.0 (Schritt 0.5) |
| `color` | Farbe des Textes (Standard: "#ffffff") | COLOR | Ja | |
| `position` | Vertikale Position des Textes auf dem Bild (Standard: "top") | COMBO | Ja | "top"<br>"bottom" |
| `align` | Horizontale Ausrichtung des Textes (Standard: "left") | COMBO | Ja | "left"<br>"center"<br>"right" |
| `outline` | Zeichnet eine schwarze Kontur um den Text (Standard: True) | BOOLEAN | Ja | |

Hinweis: Wenn `text` leer ist oder nur Leerzeichen enthält, gibt der Node die Eingabebilder unverändert zurück. Das Text-Overlay wird einmal gerendert und auf jedes Bild im Batch angewendet. Wenn der gerenderte Textblock höher ist als der verfügbare Bildbereich, wird die Schriftgröße automatisch reduziert, bis er passt oder eine Mindestgröße erreicht.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `images` | Die Eingabebilder mit dem darüber zusammengesetzten Text-Overlay | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/de.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
