# Grok Image

Der Grok Image-Node generiert ein oder mehrere Bilder aus einer Textbeschreibung mithilfe des Grok-KI-Modells. Er sendet Ihren Prompt an einen externen Dienst und gibt die generierten Bilder als Tensoren zurück, die in Ihrem Workflow verwendet werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das spezifische Grok-Modell, das für die Bilderzeugung verwendet werden soll. Unterschiedliche Modelle können unterschiedliche Qualität, Geschwindigkeit oder Funktionen bieten. | COMBO | Ja | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | Der Text-Prompt, der zum Generieren des Bildes verwendet wird. Diese Beschreibung gibt der KI vor, was erstellt werden soll. Muss mindestens 1 Zeichen lang sein (Text, der nur aus Leerzeichen besteht, wird nicht akzeptiert). | STRING | Ja | N/A |
| `aspect_ratio` | Das gewünschte Breiten-Höhen-Verhältnis für das generierte Bild. | COMBO | Ja | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Anzahl der zu generierenden Bilder (Standard: 1). | INT | Ja | 1 bis 10 |
| `seed` | Seed, anhand dessen bestimmt wird, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `resolution` | Die gewünschte Ausgabeauflösung für die generierten Bilder (Standard: „1K“). | COMBO | Nein | `"1K"`<br>`"2K"` |
| `quality` | Qualitätsstufe, die nur vom Modell `grok-imagine-image-2.0` unterstützt wird (Standard: „medium“; „low“ ist eine der verfügbaren Optionen). Bei allen anderen Modellen wird diese Einstellung ignoriert. | COMBO | Nein | Mehrere Optionen verfügbar |

**Hinweis:** Der Parameter `seed` wird hauptsächlich verwendet, um zu steuern, wann der Node innerhalb eines Workflows erneut ausgeführt wird. Aufgrund der Natur des externen KI-Dienstes sind die generierten Bilder nicht reproduzierbar und über mehrere Ausführungen hinweg nicht identisch, selbst bei identischem Seed.

**Hinweis zur Preisgestaltung:** Die Kosten für die Generierung von Bildern hängen vom ausgewählten `model`, `resolution`, `quality` und `number_of_images` ab. Beim Modell `grok-imagine-image-2.0` kostet die Qualität „low“ 0,04 $ pro Bild bei 1K-Auflösung und 0,06 $ pro Bild bei 2K-Auflösung; andere Qualitätsstufen kosten 0,06 $ pro Bild bei 1K und 0,08 $ pro Bild bei 2K. Das Modell `grok-imagine-image-quality` kostet 0,05 $ pro Bild bei 1K-Auflösung und 0,07 $ pro Bild bei 2K-Auflösung. Das Modell `grok-imagine-image-pro` kostet 0,07 $ pro Bild. Das Modell `grok-imagine-image` kostet 0,02 $ pro Bild.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `output` | Das generierte Bild oder ein Batch von Bildern. Wenn `number_of_images` 1 ist, wird ein einzelner Bild-Tensor zurückgegeben. Wenn der Wert größer als 1 ist, wird ein Batch von Bild-Tensoren zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/de.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
