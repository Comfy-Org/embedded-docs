# Flux.2 [pro] Bild

Erzeugt ein Bild mit Flux.2 [pro] über die BFL-API anhand eines Prompts und expliziter Ausgabedimensionen, optional geleitet durch Referenzbilder.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `Prompt` | Prompt für die Bilderzeugung oder -bearbeitung. | STRING | Ja | - |
| `Breite` | Breite des generierten Bildes in Pixeln (Standard: 1024). | INT | Ja | 256 bis 2048 (Schritt 32) |
| `Höhe` | Höhe des generierten Bildes in Pixeln (Standard: 768). | INT | Ja | 256 bis 2048 (Schritt 32) |
| `Seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |
| `prompt_upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiv, wird der Prompt automatisch für eine kreativere Generierung angepasst (Standard: `True`). Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | True / False |
| `Bilder` | Optionale Referenzbilder für die Bild-zu-Bild-Generierung. Jedes Bild wird vor dem Hochladen auf höchstens 2048x2048 Pixel herunterskaliert. | IMAGE | Nein | 0 bis 9 Bilder |

**Einschränkungen:**

* Das Verbinden von mehr als 9 Referenzbildern führt zu einem Fehler.
* Die Ausgabegröße wird pro Megapixel berechnet, daher kosten größere `width`- und `height`-Werte mehr.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `IMAGE` | Das generierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ProImageNode/de.md)

---
**Source fingerprint (SHA-256):** `ffa3934abaa38e030eedf2624e7a91333e24a92d7ac89af8637e59d59341eb6d`
