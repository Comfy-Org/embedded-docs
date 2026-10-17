# MOSS-Image Layout Prompt

Erstellt den Layout-Prompt, den MOSS-Image liest. Er nimmt die im Node „Create Bounding Boxes“ gezeichneten Elemente und gibt ein JSON-Layout mit einem Eintrag pro Box aus: deren Label, deren Bildunterschrift und deren Rechteck im Pixelraum der Ziel-Leinwand. Setzen Sie `width` und `height` auf die Größe des Bildes, das Sie generieren möchten, und verbinden Sie dann die Ausgabe mit dem Prompt-Eingang des Text-Encoders. Wenn keine Elemente verbunden sind, wird der Prompt-Text unverändert zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Beschreibung des gesamten Bildes. Sie wird zur Bildunterschrift des Layouts. | STRING | Ja | - |
| `element` | Die zu platzierenden Elemente, entnommen aus dem Node „Create Bounding Boxes“. Jede Box trägt ihre Bildunterschrift bei; Textboxen tragen auch ihren Text bei, und Boxen, die eine Farbpalette tragen, behalten diese. | ARRAY | Ja | - |
| `width` | Breite des generierten Bildes in Pixeln. Die Boxen werden in dieses Pixelraster umgewandelt, verwenden Sie also die Größe des Bildes, das Sie generieren möchten (Standard: 1024). | INT | Ja | 16 bis 16384 (Schritt: 16) |
| `height` | Höhe des generierten Bildes in Pixeln. Die Boxen werden in dieses Pixelraster umgewandelt, verwenden Sie also die Größe des Bildes, das Sie generieren möchten (Standard: 1024). | INT | Ja | 16 bis 16384 (Schritt: 16) |
| `character_boxes` | Nummern der Boxen, die als Zeichen anstelle von Objekten gekennzeichnet werden sollen, wie in der Vorschau von „Create Bounding Boxes“ getaggt, zum Beispiel „1, 3“. Jede Zahl in der Zeichenkette wird gelesen, daher funktioniert jedes Trennzeichen (Standard: leer). | STRING | Ja | - |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `prompt` | Der Layout-Prompt: ein JSON-Objekt, das die Bildunterschrift, einen Eintrag pro Box und das Box-Koordinatenformat enthält. Der Eingabetext wird unverändert weitergegeben, wenn keine Elemente verbunden sind. | STRING |

## Hinweise

Box-Rechtecke kommen von „Create Bounding Boxes“ als normalisierte Koordinaten zwischen 0 und 1000 an und werden im Layout in Pixeln relativ zur Mitte der Leinwand in der Reihenfolge `yxyx` geschrieben. Die Werte `width` und `height` müssen daher mit dem von Ihnen generierten Bild übereinstimmen, andernfalls landen die Boxen an der falschen Stelle.

Eine Box, die Text enthält, wird immer als Text gekennzeichnet, eine Box, deren Nummer in `character_boxes` aufgeführt ist, wird als Zeichen gekennzeichnet, und jede andere Box wird als Objekt gekennzeichnet.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageLayoutPrompt/de.md)

---
**Source fingerprint (SHA-256):** `da012a8d0dceaf6391110c90bd677d7929920d60fe961c00e5011b037206aa9a`
