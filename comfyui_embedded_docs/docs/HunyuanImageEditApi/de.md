# Tencent HY Image: Bearbeiten

Der Node Tencent HY Image: Edit bearbeitet oder kombiniert Referenzbilder anhand einer Textanweisung mit dem Hunyuan-Image-Modell von Tencent. Verbinden Sie ein bis fünf Bilder, beschreiben Sie die Änderung im Prompt und verweisen Sie auf die Bilder als `@Image1`, `@Image2` und so weiter. Der Node lädt die Referenzbilder hoch, sendet die Anfrage an die API und gibt das bearbeitete Ergebnis zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Bearbeitung verwendete Modell. Das ausgewählte Modell bestimmt, welche zusätzlichen Eingaben angezeigt werden. | DYNAMIC_COMBO | Ja | `"hy-image-3.5-preview"` |

### hy-image-3.5-preview Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Die Bearbeitungsanweisungen. Unterstützt Referenzen im Stil von `@Image1` auf die verbundenen Bilder. Darf nicht leer sein (Standard: leer). | STRING | Ja | Beliebiger Text |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. `"auto"` folgt dem Seitenverhältnis des ersten Referenzbilds und ist bei 4K nicht verfügbar. Wird ignoriert, wenn `resolution` `"custom"` ist. | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (Standard: `"auto"`) |
| `resolution` | Pixelbereich der Ausgabe: 1K entspricht etwa 1024x1024, 2K etwa 2048x2048 und 4K etwa 4096x4096. Alles über 2K wird in 2K gerendert und vom Modell hochskaliert. Auf `"custom"` setzen, um `width` und `height` anstelle eines voreingestellten Bereichs zu verwenden. | COMBO | Ja | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (Standard: `"2K"`) |
| `width` | Breite der Ausgabe in Pixeln. Wird nur verwendet, wenn `resolution` `"custom"` ist. | INT | Ja | 256-8192, Schrittweite 16 (Standard: 2048) |
| `height` | Höhe der Ausgabe in Pixeln. Wird nur verwendet, wenn `resolution` `"custom"` ist. | INT | Ja | 256-8192, Schrittweite 16 (Standard: 2048) |
| `seed` | Seed für die Generierung. Die Ergebnisse variieren auch zwischen Durchläufen mit demselben Seed. | INT | Ja | 0-2147483647 (Standard: 42) |
| `reference_detail` | Wie viele Details der Referenzbilder das Modell sieht: `"standard"` erlaubt bis zu 1024x1024 Pixel pro Bild, `"high"` bis zu 2048x2048 und bewahrt kleinen Text und feine Details besser, dauert aber länger. Dies ist ein erweiterter Parameter. | COMBO | Nein | `"standard"`<br>`"high"` (Standard: `"standard"`) |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt wird. Dies ist ein erweiterter Parameter. | BOOLEAN | Nein | true<br>false (Standard: false) |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Die Referenzbilder, die bearbeitet oder kombiniert werden sollen. Erweiterbarer Slot: Verbinden Sie 1 bis 5 Bilder (`image_1` bis `image_5`). Verweisen Sie im Prompt auf sie als `@Image1` ... `@Image5`, nummeriert in Eingabereihenfolge; eine gebündelte Eingabe zählt einmal pro Bild. | IMAGE | Ja | 1-5 Bilder |

`prompt` darf nicht leer sein, und eine Prompt-Referenz wie `@Image3` löst einen Fehler aus, wenn nur 1 oder 2 Bilder verbunden sind. Insgesamt können höchstens 5 Referenzbilder verwendet werden, wobei jedes Bild eines Batches separat gezählt wird. Bei der Auflösung `"custom"` müssen `width` und `height` beide Vielfache von 16 sein, und ihr Produkt darf das Flächenlimit von 4096 x 4096 Pixeln (etwa 16,7 Megapixel) nicht überschreiten; jedes Seitenverhältnis funktioniert, obwohl das Modell ab etwa 6:1 beginnt, das Motiv zu wiederholen. Das Seitenverhältnis `"auto"` funktioniert nur innerhalb des 2K-Flächenlimits, wählen Sie daher bei 4K ein explizites Seitenverhältnis oder verwenden Sie `"custom"`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das bearbeitete Bild, das aus den Referenzbildern und dem Prompt erzeugt wurde. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageEditApi/de.md)

---
**Source fingerprint (SHA-256):** `46c112347b51a2983521f87bbeb047289515f4073c48ba5d909fd3bae4597633`
