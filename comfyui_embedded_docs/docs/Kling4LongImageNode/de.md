# Kling 4.0 Long Image

Generieren Sie ein hochformatiges Bild mit Kling 4.0: ein vollständiges Webseiten-Design oder eine E-Commerce-Produktdetailseite. Wählen Sie den `skill`, der dem gewünschten Layout entspricht, und der Node zeigt die Eingaben für dieses Layout an.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Skill` | Zu generierendes Layout. `"webpage"` entwirft eine vollständige Seite um ein optionales Stilbild und Motiv; `"ecommerce"` erstellt eine Produktdetailseite aus Produktfotos. | DYNAMIC_COMBO | Ja | `"webpage"`<br>`"ecommerce"` |

### `webpage` Eingaben

Diese Eingaben erscheinen, wenn `skill` auf `"webpage"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `style_image` | Optionale Referenz für den visuellen Stil und das Layout. Verweisen Sie darauf als `@Image1`. | IMAGE | Nein | Einzelbild |
| `subject_image` | Optionales Motiv, das beibehalten und um das die Seite gestaltet werden soll. Verweisen Sie darauf als `@Image2`. | IMAGE | Nein | Einzelbild |
| `prompt` | Optionale Beschreibung der Seite. Verweisen Sie auf das Stilbild als `@Image1` und auf das Motivbild als `@Image2`, und geben Sie die Sprache für den Seitentext an, zum Beispiel "All visible text must be in English only." Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabebildes. Standard: `"1K"`. | COMBO | Ja | `"1K"`<br>`"2K"` |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

### `ecommerce` Eingaben

Diese Eingaben erscheinen, wenn `skill` auf `"ecommerce"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `product_images` | Erweiterbare Slots für die Produktfotos (`image_1` ... `image_3`). Verweisen Sie im Prompt darauf als `@Image1`, `@Image2`, `@Image3`. | AUTOGROW | Ja | 1 bis 3 Bilder |
| `prompt` | Optionale Beschreibung der Seite. Verweisen Sie auf die Produktbilder als `@Image1`, `@Image2`, `@Image3`. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `length` | Länge der generierten Seite. Standard: `"medium"`. | COMBO | Ja | `"short"`<br>`"medium"`<br>`"long"` |
| `resolution` | Auflösung des Ausgabebildes. Standard: `"1K"`. | COMBO | Ja | `"1K"`<br>`"2K"` |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* In `ecommerce` können höchstens 3 Produktbilder verbunden werden.
* Jedes Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 2:5 und 5:2 haben.
* Bei `webpage` führt ein Prompt, der `@Image1` oder `@Image2` erwähnt, zu einem Fehler, wenn das jeweilige Bild nicht verbunden ist.
* Der Preis eines Aufrufs hängt vom Skill, der Auflösung und bei `ecommerce` von der Seitenlänge ab.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das generierte lange Bild, das von Kling heruntergeladen wird, sobald die Aufgabe abgeschlossen ist. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4LongImageNode/de.md)

---
**Source fingerprint (SHA-256):** `f1e687bcc8334229c60b318118120b85ddd580d1b62f343164f9803b98a1f987`
