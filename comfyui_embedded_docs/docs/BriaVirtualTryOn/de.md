# Bria Virtual Try-On

Dieser Node kleidet eine Person mit Bria in Kleidungsstücke oder Accessoires ein. Die Identität, Pose und der Hintergrund der Person bleiben erhalten, während die Szene mit etwa 1 Megapixel neu gerendert wird, sodass das Ergebnis nicht pixelgenau am Eingabefoto ausgerichtet ist. Jedes Kleidungsbild ersetzt das passende Teil, das die Person bereits trägt.

## Eingaben

Der Selektor `moderation` blendet eine zusätzliche Moderationsoption ein, wenn er auf `"true"` gesetzt ist.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `person_image` | Das Foto der Person, die die Kleidungsstücke anprobiert. Der Alphakanal wird vor dem Hochladen des Bildes verworfen. | IMAGE | Ja | - |
| `garment_images` | 1 bis 3 Kleidungsstücke oder Accessoires, die zusammen getragen werden; jedes ersetzt das passende Teil, das die Person trägt. Eine gebatchte Eingabe zählt pro Bild einmal, und transparente Bereiche werden als Weiß behandelt. | AUTOGROW | Ja | 1 bis 3 Bilder |
| `instruction` | Optionale zusätzliche Anweisung, die zu Brias integrierter Anweisung hinzugefügt wird, z. B. welches Kleidungsstück obenauf getragen werden soll. Standard: `""` (leerer String). | STRING | Ja | - |
| `aspect_ratio` | `"auto"` behält den Bildausschnitt des Personenfotos bei etwa 1 Megapixel bei. Ein festes Verhältnis liefert 0,6 bis 1 Megapixel, zum Beispiel 768x1024 für `"3:4"`. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Seed, der mit der Anfrage an Bria gesendet wird. Standard: 42. | INT | Ja | 1 bis 2147483647 |
| `moderation` | Moderationseinstellungen. Wenn auf `"true"` gesetzt, wird die unten stehende Moderationsoption verfügbar. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Moderation "true" Eingaben

Dieser Parameter erscheint nur, wenn `moderation` auf `"true"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Bild. Standard: `False`. | BOOLEAN | Nein | True / False |

**Einschränkungen:**

* `garment_images` akzeptiert maximal 3 Bilder, gezählt pro Bild, wenn die Eingabe gebatcht ist.
* Transparente Pixel in den Kleidungsbildern werden vor dem Hochladen mit Weiß hinterlegt.
* Der Alphakanal von `person_image` wird vor dem Hochladen verworfen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das bearbeitete Foto, auf dem die Person die bereitgestellten Kleidungsstücke trägt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVirtualTryOn/de.md)

---
**Source fingerprint (SHA-256):** `32f89c8685d8624bdef2c17ba5ba916b030d1dc88718b83c79aadb9a5fa378de`
