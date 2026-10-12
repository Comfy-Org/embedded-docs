# OpenRouterImageNode

Dieser Node erzeugt oder bearbeitet Bilder über OpenRouter mithilfe der MAI-Image-2.6-Modelle von Microsoft. Er unterstützt die Text-zu-Bild-Generierung sowie bildgestützte Bearbeitung mit bis zu fünf Referenzbildern in sieben Seitenverhältnissen bei 1K- oder 1.5K-Auflösung.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das OpenRouter-Bildmodell, das zur Bilderzeugung verwendet wird. Wenn Sie ein Modell auswählen, werden die unten aufgeführten modellspezifischen Optionen angezeigt. | DYNAMIC_COMBO | Ja | `microsoft/mai-image-2.6`<br>`microsoft/mai-image-2.6-flash` |

### Mai Image 2.6 und Mai Image 2.6 Flash Eingaben

Wird von beiden Modelloptionen (`microsoft/mai-image-2.6` und `microsoft/mai-image-2.6-flash`) gemeinsam genutzt, die denselben Parametersatz bereitstellen.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibt das zu erzeugende Bild oder die auf die Referenzbilder anzuwendende Bearbeitung. Bis zu 20000 Zeichen. Standard: `""` (leer). Nach dem Entfernen umgebender Leerzeichen ist mindestens 1 Zeichen erforderlich. | STRING | Ja | 1 bis 20000 Zeichen |
| `aspect_ratio` | Seitenverhältnis des erzeugten Bildes; wird auch angewendet, wenn Referenzbilder verbunden sind. Standard: `"1:1"`. `"auto"` lässt das Modell das Verhältnis für Text-zu-Bild wählen (gerendert in der 1.5K-Größe) und behält beim Bearbeiten das Seitenverhältnis des ersten Referenzbildes bei. | COMBO | Ja | `"1:1"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"auto"` |
| `resolution` | Größenstufe der Ausgabe. 1K entspricht etwa 1 Megapixel (1:1 ist 1024x1024, 16:9 ist 1360x768); 1.5K entspricht etwa 2,3 Megapixeln (1:1 ist 1536x1536, 16:9 ist 2048x1152). Standard: `"1K"`. Wird ignoriert, wenn `aspect_ratio` `"auto"` ist. | COMBO | Ja | `"1K"`<br>`"1.5K"` |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die API hat keinen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. Standard: `42`. | INT | Ja | 0 bis 2147483647 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image_1` ... `image_5` | Erweiterbarer Slot: Verbinden Sie 1 bis 5 Referenzbilder für bildgestützte Bearbeitung; eine Batch-Eingabe zählt einmal pro Bild. Slots sind optional und können leer bleiben (mindestens 0 verbunden). | IMAGE | Nein | 0 bis 5 Bilder |

**Hinweise:**

- Insgesamt werden über alle verbundenen Slots hinweg maximal 5 Referenzbilder unterstützt; eine Batch-Eingabe zählt einmal pro Bild.
- Der `prompt` muss nach Entfernen umgebender Leerzeichen mindestens 1 Zeichen enthalten und darf 20000 Zeichen nicht überschreiten.
- Referenzbilder werden als PNG-Daten gesendet und sind auf insgesamt 2048 x 2048 Pixel begrenzt.
- Die Einstellung `aspect_ratio` wird auf die Ausgabe angewendet, auch wenn Referenzbilder verbunden sind.
- Wenn `aspect_ratio` `"auto"` ist, wird die Einstellung `resolution` ignoriert. Ohne Referenzbilder wählt das Modell das Verhältnis für Text-zu-Bild und rendert in der 1.5K-Größe; wenn Referenzbilder verbunden sind, wird das Seitenverhältnis des ersten Referenzbildes beibehalten.
- Der Seed-Wert beeinflusst das API-Ergebnis nicht; er bestimmt nur, ob der Node erneut ausgeführt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das erzeugte oder bearbeitete Bild. Wenn der Dienst mehrere Bilder zurückgibt, werden sie zu einer einzelnen gebündelten IMAGE-Ausgabe zusammengefasst. Ein Fehler wird ausgelöst, wenn kein Bild zurückgegeben wird oder wenn ein zurückgegebenes Bild nicht dekodiert werden kann. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterImageNode/de.md)

---
**Source fingerprint (SHA-256):** `d201c18deccd2523041a24427996f51127ca201dfe10fad60c6f768ab79bf852`
