# Pruna P-Video Upscale

## Pruna P-Video Upscale

Pruna P-Video Upscale vergrößert ein Video auf 720p, 1080p, 2K oder 4K und behält dabei sein Seitenverhältnis und seine Tonspur bei. Der Clip wird an Pruna gesendet, die Vorhersage wird abgefragt, und das hochskalierte Video wird zurückgegeben. Eine Quelle, die bereits die Zielgröße erreicht oder überschreitet, behält ihre Abmessungen und wird lediglich verbessert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Zu vergrößerndes Video, bis zu 512 MiB. Videos mit mehr als 10 Megapixeln können nur an das 2K- oder 4K-Ziel gesendet werden. | VIDEO | Ja | Bis zu 512 MiB |
| `target` | Ausgabepixelbereich: 720p entspricht etwa 0,9 Megapixeln, 1080p 2,1, 2K 3,7 und 4K 8,3. Der längste Clip wird durch das Ziel begrenzt: 2400, 1200, 600 oder 300 Frames, etwa 100, 50, 25 oder 12,5 Sekunden bei 24 fps (Standard: "1080p"). | COMBO | Ja | "720p"<br>"1080p"<br>"2K"<br>"4K" |
| `fps` | Ausgabebildrate (Standard: "source"). "source" behält die Bildrate des Videos bei, bis zu 60; eine höhere Rate wird interpoliert. Eine Ausgabe über 30 fps kostet doppelt so viel. | COMBO | Ja | "source"<br>"16"<br>"24"<br>"25"<br>"30"<br>"48"<br>"50"<br>"60" |
| `turbo` | Schnelleres Upscaling mit weicheren Details zum gleichen Preis (Standard: false). | BOOLEAN | Nein | true<br>false |

### Parametereinschränkungen

- Der Clip muss 512 MiB oder kleiner sein, gemessen nachdem er zu H.264 MP4 neu kodiert wurde.
- Das Frame-Limit wird bei bis zu 30 fps gezählt: 2400 Frames für 720p, 1200 für 1080p, 600 für 2K und 300 für 4K. Ein längerer Clip erfordert ein niedrigeres Ziel, eine niedrigere `fps` oder einen kürzeren Ausschnitt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das hochskalierte Video mit seinem Originalaudio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaPVideoUpscaleNode/de.md)

---
**Source fingerprint (SHA-256):** `e8fc88b6177085e0852d17ff92b0a22a26c9914c012a9a244b19da9b2c0e38c2`
