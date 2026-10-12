# Flux Video Edit

Bearbeitet einen vorhandenen Videoclip anhand einer schriftlichen Anweisung. Sie können Objekte entfernen, hinzufügen oder ersetzen, die Umgebung ändern, das Material neu gestalten, Text im Bild ändern oder den gesprochenen Dialog ersetzen. Länge, Bildaufbau, Kamerabewegung und Audio stammen aus dem Quellclip; alles, was Sie im Prompt nicht erwähnen, soll daher unverändert bleiben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Quellclip von 0.7 bis 15 Sekunden, mindestens 160x160 Pixel. Die Ausgabe wird mit 24 fps gerendert und auf etwa 0.9 Megapixel pro Frame begrenzt; eine größere Quelle wird daher kleiner zurückgegeben. | VIDEO | Ja | 0.7 bis 15 Sekunden; mindestens 160x160 Pixel |
| `prompt` | Was geändert werden soll, in einfacher Sprache, bis zu 4096 Zeichen. Alles, was Sie nicht erwähnen, soll unverändert bleiben. Ersatzdialog muss in die Zeit passen, die der ursprüngliche Sprechanteil einnimmt, und ein stummer Clip bleibt stumm. Standard: leerer String. | STRING | Ja | 1 bis 4096 Zeichen |
| `auto_downscale` | Verkleinert Quellen, die im Bereich größer als 1280x704 Pixel sind, vor dem Upload automatisch. Das Seitenverhältnis bleibt erhalten; kleinere Videos werden nicht verändert. Standard: true. | BOOLEAN | Nein | true<br>false |
| `safety_tolerance` | Moderationstoleranz, 0 ist am strengsten. Standard: 4. | INT | Nein | 0 bis 4 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; FLUX wählt seinen eigenen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 4294967295 |

**Hinweis:** Der `prompt` muss mindestens 1 Zeichen und darf höchstens 4096 Zeichen enthalten. Das Quell-`video` muss zwischen 0.7 und 15 Sekunden lang und mindestens 160x160 Pixel groß sein; Uploads, die außerhalb dieser Grenzen liegen, werden abgelehnt, bevor die Anfrage gesendet wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Der bearbeitete Videoclip, der vom FLUX-Dienst zurückgegeben wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoEditNode/de.md)

---
**Source fingerprint (SHA-256):** `169b14700acfee3f6ccc247f08f3ae8c5f3c4610062a447e8215246460299b6a`
