# Kling 4.0 Image

Erzeugen oder bearbeiten Sie Bilder mit Kling 4.0 anhand eines Text-Prompts und bis zu 10 Referenzbildern. Fordern Sie ein einzelnes Bild an oder lassen Sie den Node eine Reihe zusammengehöriger Bilder zurückgeben, die dieselben Charaktere und denselben Stil beibehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbare Slots für Referenzbilder (`image_1` ... `image_10`). Verweisen Sie im Prompt mit `@Image1`, `@Image2` usw. auf sie. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `prompt` | Beschreibung des Bildes. Verweisen Sie auf die verbundenen Bilder als `@Image1`, `@Image2`, ... Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabebildes. Standard: `"2K"`. | COMBO | Ja | `"2K"`<br>`"4K"`<br>`"8K"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabebildes. `"auto"` folgt den Referenzbildern, andernfalls dem Prompt. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"9:16"`<br>`"2:3"`<br>`"3:4"`<br>`"1:1"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `series_amount` | Erzeugt eine Reihe zusammengehöriger Bilder, die dieselben Charaktere und denselben Stil beibehalten. `"auto"` lässt das Modell 2 bis 10 Bilder auswählen. Standard: `"disabled"`. | COMBO | Ja | `"disabled"`<br>`"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* Es können höchstens 10 Referenzbilder verbunden werden.
* Jedes Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 2:5 und 5:2 aufweisen.
* Ein Prompt, der `@ImageN` erwähnt, löst einen Fehler aus, wenn weniger als N Bilder verbunden sind.
* Wenn `series_amount` auf `"disabled"` gesetzt ist, gibt der Node ein Bild zurück; jeder andere Wert gibt einen Batch mit entsprechend vielen Bildern zurück.
* Der Preis eines Aufrufs skaliert mit der Auflösung, der Anzahl der Referenzbilder und der Anzahl der Bilder in der Serie.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das erzeugte Bild oder ein Batch von Bildern, wenn `series_amount` aktiviert ist. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageNode/de.md)

---
**Source fingerprint (SHA-256):** `7840b108419e759942aed332456cab73e748d9f018462011da3b1293646a4ffe`
