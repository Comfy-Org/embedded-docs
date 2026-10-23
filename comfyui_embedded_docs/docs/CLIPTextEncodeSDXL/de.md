# ClipTextEncodeSdxl

Dieser Node ist dafür ausgelegt, Texteingaben mithilfe eines CLIP-Modells zu kodieren, das speziell für die SDXL-Architektur angepasst ist. Er verwendet ein duales Encoder-System (CLIP-L und CLIP-G), um Textbeschreibungen zu verarbeiten, was zu einer präziseren Bildgenerierung führt.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | CLIP-Modellinstanz, die für die Textkodierung verwendet wird. | CLIP |
| `width` | Gibt die Bildbreite in Pixeln an, Standardwert 1024. | INT |
| `height` | Gibt die Bildhöhe in Pixeln an, Standardwert 1024. | INT |
| `crop_w` | Breite des Zuschneidebereichs in Pixeln, Standardwert 0. | INT |
| `crop_h` | Höhe des Zuschneidebereichs in Pixeln, Standardwert 0. | INT |
| `target_width` | Zielbreite für das Ausgabebild, Standardwert 1024. | INT |
| `target_height` | Zielhöhe für das Ausgabebild, Standardwert 1024. | INT |
| `text_g` | Globale Textbeschreibung für die Beschreibung der Gesamtszene. | STRING |
| `text_l` | Lokale Textbeschreibung für die Beschreibung von Details. | STRING |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Enthält kodierten Text und konditionale Informationen, die für die Bildgenerierung benötigt werden. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/de.md)
