# Flux.2 Bild

Generieren Sie Bilder mit dem Modell Flux.2 [pro] oder Flux.2 [max] aus einem Text-Prompt und optionalen Referenzbildern. Der Node sendet die Anfrage an die BFL API, fragt so lange ab, bis das Ergebnis bereit ist, und gibt das generierte Bild zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Die zu verwendende Flux.2-Modellversion. Wenn Sie ein Modell auswählen, werden zusätzliche Parameter für Breite, Höhe und optionale Referenzbilder freigeschaltet. | DYNAMIC_COMBO | Ja | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `prompt` | Prompt für die Bilderzeugung oder -bearbeitung (Standard: leerer String). | STRING | Ja | N/A |
| `seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0). Unterstützt die Option zur Steuerung nach der Generierung, um den Wert nach jedem Lauf zu randomisieren. | INT | Ja | 0 bis 18446744073709551615 |

### Flux.2 [pro] und Flux.2 [max] Eingaben

Von beiden Modellen gemeinsam verwendet – die Parametersätze sind identisch.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model.width` | Die Breite des generierten Bilds in Pixeln (Standard: 1024). | INT | Ja | 256 bis 2048 (Schrittweite 32) |
| `model.height` | Die Höhe des generierten Bilds in Pixeln (Standard: 768). | INT | Ja | 256 bis 2048 (Schrittweite 32) |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model.images` | Optionale Referenzbild(er) für die Bild-zu-Bild-Generierung. Bis zu 8 Bilder. Erweiterbarer Slot: 1..8 Elemente verbinden (`image_1`...`image_8`). | IMAGE | Nein | 0 bis 8 Bilder |

**Hinweis:**
- Die maximale Anzahl an Referenzbildern beträgt 8. Wenn mehr als 8 Bilder bereitgestellt werden, wird ein Fehler ausgelöst. Batch-Bilder zählen zu diesem Limit, da jedes Bild in einem Batch einzeln gezählt wird.
- Referenzbilder werden skaliert, sodass die Gesamtzahl der Pixel 2048 x 2048 nicht überschreitet, bevor sie an die API gesendet werden.
- Die Werte von `model.width` und `model.height` beeinflussen die Generierungskosten. Die Kosten hängen außerdem vom ausgewählten Modell und davon ab, ob Referenzbilder bereitgestellt werden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das generierte Bild als Tensor, heruntergeladen aus dem Ergebnis der BFL API. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/de.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
