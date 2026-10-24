# Bria Product Holding

Dieser Node platziert mit Bria ein Produkt in den Händen einer Person. Die Identität, Pose und der Hintergrund der Person bleiben erhalten, während die Szene mit etwa 1 Megapixel neu gerendert wird; daher ist das Ergebnis nicht pixelgenau auf das Eingabefoto ausgerichtet. Alle Produktbilder beschreiben ein Produkt aus verschiedenen Blickwinkeln oder Verarbeitungsstadien.

## Eingaben

Der Selektor `moderation` zeigt eine zusätzliche Moderationsoption an, wenn er auf `"true"` gesetzt ist.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `person_image` | Das Foto der Person, die das Produkt hält. Der Alphakanal wird vor dem Hochladen des Bildes entfernt. | IMAGE | Ja | - |
| `product_images` | 1 bis 3 Bilder eines Produkts: das Produkt selbst, seine Verpackung, ein anderer Blickwinkel oder ein Begleitartikel. Bei einer Batch-Eingabe zählt jedes Bild einzeln, und transparente Bereiche werden als Weiß behandelt. | AUTOGROW | Ja | 1 bis 3 Bilder |
| `instruction` | Optionale zusätzliche Anweisung, die der integrierten Anweisung von Bria hinzugefügt wird, z. B. welche Hand verwendet werden soll oder in welche Richtung das Etikett zeigt. Standard: `""` (leere Zeichenkette). | STRING | Ja | - |
| `aspect_ratio` | `"auto"` behält den Bildausschnitt des Personenfotos bei etwa 1 Megapixel bei. Ein festes Seitenverhältnis ergibt 0,6 bis 1 Megapixel, zum Beispiel 768x1024 für `"3:4"`. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Seed, der mit der Anfrage an Bria gesendet wird. Standard: 42. | INT | Ja | 1 bis 2147483647 |
| `moderation` | Moderationseinstellungen. Wenn auf `"true"` gesetzt, wird das unten stehende Moderations-Flag verfügbar. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Moderation "true" Eingaben

Dieser Parameter erscheint nur, wenn `moderation` auf `"true"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Bild. Standard: `False`. | BOOLEAN | Nein | True / False |

**Einschränkungen:**

* `product_images` akzeptiert maximal 3 Bilder; bei einer Batch-Eingabe wird jedes Bild einzeln gezählt.
* Transparente Pixel in den Produktbildern werden vor dem Hochladen auf Weiß komponiert.
* Der Alphakanal von `person_image` wird vor dem Hochladen entfernt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das bearbeitete Foto, bei dem das Produkt in den Händen der Person platziert ist. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaProductHolding/de.md)

---
**Source fingerprint (SHA-256):** `91a4a4dde0e9d7fe2480130da87edf1f8ed9d4ae0c86f8a8d030c36987dcdb8e`
