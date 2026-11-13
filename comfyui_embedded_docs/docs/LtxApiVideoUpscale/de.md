# LTX Video Upscale

Skaliert ein Video auf 1080p, 4K oder 8K hoch, wobei Seitenverhältnis, Bildrate und Audio beibehalten werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Wertebereich |
| --- | --- | --- | --- | --- |
| `video` | Hochzuskalierendes Video mit einer kurzen Seite von mindestens 480 Pixeln und maximal 7680x4320 in jeder Ausrichtung. Bis zu 2401 Frames für 1080p, 601 Frames für 4K und 241 Frames für 8K. | VIDEO | Ja | - |
| `resolution` | Ausgabegröße, so groß wie in 1920x1080, 3840x2160 oder 7680x4320 passend und für Hochformatvideos gedreht. Standard: `"4k"`. | COMBO | Ja | `"1080p"`<br>`"4k"`<br>`"8k"` |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 4294967295 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das hochskalierte Video, dessen Audio beibehalten wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoUpscale/de.md)

---
**Source fingerprint (SHA-256):** `e9b3b760365568ab2f6572c5f4f28758d67c4f5795fc39716ed4f648aafef80e`
