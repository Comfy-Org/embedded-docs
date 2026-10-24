# Flux.2 [max] Bild

Erzeugt ein Bild mit Flux.2 [max] über die BFL API anhand eines Prompts und expliziter Ausgabemaße, optional gesteuert durch Referenzbilder. Es werden dieselben Eingaben wie bei Flux.2 [pro] Image bereitgestellt.

**Hinweis:** Dieser Node ist im Quellcode als veraltet (deprecated) gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Prompt` | Prompt für die Bildgenerierung oder -bearbeitung. | STRING | Ja | - |
| `Breite` | Breite des generierten Bildes in Pixeln (Standard: 1024). | INT | Ja | 256 bis 2048 (Schrittweite 32) |
| `Höhe` | Höhe des generierten Bildes in Pixeln (Standard: 768). | INT | Ja | 256 bis 2048 (Schrittweite 32) |
| `Seed` | Der für die Erzeugung des Rauschens verwendete Zufalls-Seed (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |
| `Prompt-Upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiv, wird der Prompt automatisch für eine kreativere Generierung angepasst (Standard: `True`). Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | True / False |
| `Bilder` | Optionale Referenzbilder für die Bild-zu-Bild-Generierung. Jedes Bild wird vor dem Hochladen auf höchstens 2048x2048 Pixel herunterskaliert. | IMAGE | Nein | 0 bis 9 Bilder |

**Einschränkungen:**

* Das Verbinden von mehr als 9 Referenzbildern führt zu einem Fehler.
* Die Ausgabegröße wird pro Megapixel berechnet, sodass größere `width`- und `height`-Werte mehr kosten.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das generierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2MaxImageNode/de.md)

---
**Source fingerprint (SHA-256):** `cd540606835e7808861d9a96584731100b1bf9c996f18586fed39e8a2d32a29f`
