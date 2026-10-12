# BriaRemoveVideoBackground

Dieser Node entfernt den Hintergrund aus einem Video mithilfe des Bria AI-Dienstes. Er verarbeitet das Eingabevideo und ersetzt den ursprünglichen Hintergrund durch eine Volltonfarbe Ihrer Wahl. Der Vorgang wird über eine externe API ausgeführt, und das Ergebnis wird als neue Videodatei zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Die Eingabevideodatei, aus der der Hintergrund entfernt wird. | VIDEO | Ja | N/A |
| `background_color` | Hintergrundfarbe für das Ausgabevideo. | COMBO | Ja | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Das Eingabevideo darf eine Dauer von höchstens 60 Sekunden haben. Die Ergebnisse sind auch dann nicht deterministisch, wenn der Seed-Wert unverändert bleibt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die verarbeitete Videodatei, bei der der Hintergrund entfernt und durch die ausgewählte Farbe ersetzt wurde, codiert als MP4 mit H.264-Codec. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/de.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
