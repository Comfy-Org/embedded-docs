# Tencent HY Image: Text zu Bild

Der Tencent HY Image: Text to Image-Node erzeugt ein Bild aus einer Textbeschreibung mit dem Hunyuan Image-Modell von Tencent. Der Prompt wird an die API gesendet, die ihn vor dem Rendern umschreibt und erweitert, und das fertige Bild wird als Bild-Batch zurückgegeben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Generierung verwendete Modell. Das ausgewählte Modell bestimmt, welche zusätzlichen Eingaben angezeigt werden. | DYNAMIC_COMBO | Ja | `"hy-image-3.5-preview"` |

### hy-image-3.5-preview Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibt das zu generierende Bild. Das Modell schreibt ihn vor dem Rendern um und erweitert ihn. Darf nicht leer sein (Standard: leer). | STRING | Ja | Beliebiger Text |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. `"auto"` lässt das Modell das Verhältnis anhand des Prompts auswählen und ist bei 4K nicht verfügbar. Wird ignoriert, wenn `resolution` auf `"custom"` gesetzt ist. | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (Standard: `"auto"`) |
| `resolution` | Pixelbereich des Bildes: 1K entspricht etwa 1024x1024, 2K etwa 2048x2048 und 4K etwa 4096x4096. Alles über 2K wird in 2K gerendert und vom Modell hochskaliert. Auf `"custom"` setzen, um `width` und `height` anstelle eines voreingestellten Bereichs zu verwenden. | COMBO | Ja | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (Standard: `"2K"`) |
| `width` | Breite des Bildes in Pixeln. Wird nur verwendet, wenn `resolution` auf `"custom"` gesetzt ist. | INT | Ja | 256-8192, Schrittweite 16 (Standard: 2048) |
| `height` | Höhe des Bildes in Pixeln. Wird nur verwendet, wenn `resolution` auf `"custom"` gesetzt ist. | INT | Ja | 256-8192, Schrittweite 16 (Standard: 2048) |
| `seed` | Seed für die Generierung. Ergebnisse variieren auch bei gleichem Seed zwischen den Durchläufen. | INT | Ja | 0-2147483647 (Standard: 42) |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll. Dies ist ein erweiterter Parameter. | BOOLEAN | Nein | true<br>false (Standard: false) |

`prompt` darf nicht leer sein. Bei der Auflösung `"custom"` müssen `width` und `height` beide Vielfache von 16 sein, und ihr Produkt darf die Flächenbegrenzung von 4096 x 4096 Pixeln (etwa 16,7 Megapixel) nicht überschreiten; jedes Seitenverhältnis funktioniert, obwohl das Modell ab etwa 6:1 beginnt, das Motiv zu wiederholen. Das Seitenverhältnis `"auto"` erfordert, dass das Modell eine Größe auswählt, daher funktioniert es nur innerhalb der 2K-Flächenbegrenzung: Wählen Sie bei 4K ein explizites Seitenverhältnis oder verwenden Sie `"custom"`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das generierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageTextToImageApi/de.md)

---
**Source fingerprint (SHA-256):** `1d4e70d688c5aa4e79b81447da559e201078454077da34769f2a4f544fbba63f`
