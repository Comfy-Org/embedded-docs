# VOID-Quadmask-Vorverarbeitung

## Überblick

Der Node VOIDQuadmaskPreprocess bereitet eine Maske für das VOID-Inpainting vor, indem er sie in eine spezielle vierstufige „Quadmask“ umwandelt. Er nimmt eine Eingabemaske entgegen, dilatiert optional den primären Bereich und quantisiert anschließend die Maskenwerte in vier verschiedene Stufen, die unterschiedliche semantische Bereiche repräsentieren (primäres Objekt, Überlappung, betroffener Bereich und Hintergrund). Schließlich invertiert und normalisiert er die Maske, sodass die Ausgabewerte im Bereich [0, 1] liegen, wobei 1,0 den zu entfernenden Bereich und 0,0 den zu behaltenden Bereich angibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `mask` | Die Eingabemaske, die vorverarbeitet werden soll. | MASK | Ja | N/A |
| `dilate_width` | Dilatationsradius für den primären Maskenbereich. Ein Wert von 0 bedeutet, dass keine Dilatation angewendet wird. (Standard: 0) | INT | Nein | 0 bis 50 (Schritt: 1) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `quadmask` | Die vorverarbeitete Quadmask mit Werten in [0, 1], die vier diskrete Stufen repräsentiert: 1,0 (primäres zu entfernendes Objekt), ~0,75 (Überlappung von primärem und betroffenem Bereich), ~0,50 (betroffener Bereich) und 0,0 (zu behaltender Hintergrund). | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/de.md)

---
**Source fingerprint (SHA-256):** `a972ff74686baaa3a3659a74517d3b6f7335e8f62d09be9329d0e71d1fad137a`
