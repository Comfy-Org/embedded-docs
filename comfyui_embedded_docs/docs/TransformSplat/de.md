# TransformSplat

Der Node Transform Splat wendet Translation, Rotation und Skalierung auf einen Gaussian Splat an. Er verschiebt, dreht und skaliert den gesamten Splat als einzelnes Objekt und formt bei nicht-uniformer Skalierung zusätzlich jeden einzelnen Gaussian Splat neu, um präzise Ergebnisse zu erzielen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `splat` | Der zu transformierende Gaussian Splat | SPLAT | Ja | - |
| `translate_x` | Translation entlang der X-Achse (Standard: 0.0) | FLOAT | Ja | -100.0 bis 100.0 |
| `translate_y` | Translation entlang der Y-Achse (Standard: 0.0) | FLOAT | Ja | -100.0 bis 100.0 |
| `translate_z` | Translation entlang der Z-Achse (Standard: 0.0) | FLOAT | Ja | -100.0 bis 100.0 |
| `rotate_x` | Rotation um die X-Achse in Grad (Standard: 0.0) | FLOAT | Ja | -360.0 bis 360.0 |
| `rotate_y` | Rotation um die Y-Achse in Grad (Standard: 0.0) | FLOAT | Ja | -360.0 bis 360.0 |
| `rotate_z` | Rotation um die Z-Achse in Grad (Standard: 0.0) | FLOAT | Ja | -360.0 bis 360.0 |
| `scale_x` | Skalierungsfaktor entlang der X-Achse (Standard: 1.0) | FLOAT | Ja | 0.01 bis 100.0 |
| `scale_y` | Skalierungsfaktor entlang der Y-Achse (Standard: 1.0) | FLOAT | Ja | 0.01 bis 100.0 |
| `scale_z` | Skalierungsfaktor entlang der Z-Achse (Standard: 1.0) | FLOAT | Ja | 0.01 bis 100.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `splat` | Der transformierte Gaussian Splat mit aktualisierten Positionen, Skalierungen und Rotationen | SPLAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TransformSplat/de.md)

---
**Source fingerprint (SHA-256):** `19e6a7da7b4f0d8c9674ead2d35d742df460576b01c4ab4108dd59a2d08dfcb0`
