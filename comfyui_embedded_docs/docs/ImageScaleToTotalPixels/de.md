# Bild auf Gesamtpixelzahl skalieren

Der Node ImageScaleToTotalPixels dient dazu, Bilder auf eine angegebene Gesamtzahl von Pixeln zu skalieren, während das Seitenverhältnis beibehalten wird. Er bietet verschiedene Methoden zum Hochskalieren des Bildes, um die gewünschte Pixelanzahl zu erreichen.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das Eingabebild, das auf die angegebene Gesamtzahl von Pixeln hochskaliert werden soll. | `IMAGE` |
| `upscale_method` | Die Methode, die zum Hochskalieren des Bildes verwendet wird. Sie beeinflusst die Qualität und die Eigenschaften des hochskalierten Bildes. | COMBO[STRING] |
| `megapixels` | Die Zielgröße des Bildes in Megapixeln. Diese bestimmt die Gesamtzahl der Pixel im hochskalierten Bild. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das hochskalierte Bild mit der angegebenen Gesamtzahl von Pixeln unter Beibehaltung des ursprünglichen Seitenverhältnisses. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/de.md)
