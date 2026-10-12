# HappyHorseReferenceVideoApi

Dieser Node erzeugt ein Video mit einer Person oder einem Objekt aus Referenzbildern unter Verwendung des HappyHorse-Modells. Er unterstützt Darbietungen mit einem einzelnen Charakter sowie Interaktionen zwischen mehreren Charakteren. Die Referenzbilder werden hochgeladen und verwendet, um die Charaktere im generierten Video darzustellen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das HappyHorse-Referenz-zu-Video-Modell, das für die Generierung verwendet werden soll. | DYNAMIC_COMBO | Ja | `"happyhorse-1.1-r2v"`<br>`"happyhorse-1.0-r2v"` |
| `seed` | Seed, der für die Generierung verwendet werden soll (Standard: 0). Kann so eingestellt werden, dass er sich nach jeder Generierung automatisch ändert. | INT | Ja | 0 bis 2147483647 |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: False). | BOOLEAN | Ja | True or False |

### HappyHorse 1.1 Eingaben (happyhorse-1.1-r2v)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der das Video beschreibt. Verwenden Sie Bezeichner wie 'character1' und 'character2', um auf die Referenzcharaktere zu verweisen. | STRING | Ja | N/A |
| `resolution` | Die Auflösung des generierten Videos. | COMBO | Ja | `"720P"`<br>`"1080P"` |
| `ratio` | Das Seitenverhältnis des generierten Videos. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"`<br>`"5:4"`<br>`"4:5"` |
| `duration` | Die Dauer des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 3 bis 15 |

### HappyHorse 1.0 Eingaben (happyhorse-1.0-r2v)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der das Video beschreibt. Verwenden Sie Bezeichner wie 'character1' und 'character2', um auf die Referenzcharaktere zu verweisen. | STRING | Ja | N/A |
| `resolution` | Die Auflösung des generierten Videos. | COMBO | Ja | `"720P"`<br>`"1080P"` |
| `ratio` | Das Seitenverhältnis des generierten Videos. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Die Dauer des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 3 bis 15 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 1 bis 9 Referenzbilder der Person oder des Objekts, die bzw. das im Video zu sehen sein soll. Mindestens ein Referenzbild muss bereitgestellt werden. | IMAGE | Ja | 1 bis 9 (pro Modell) |

Hinweis: Mindestens ein Referenzbild muss bereitgestellt werden, andernfalls löst der Node einen Fehler aus. Jedes Referenzbild muss mindestens 400 x 400 Pixel groß sein und ein Seitenverhältnis zwischen 1:2,5 und 2,5:1 aufweisen. Der Prompt darf nicht leer sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `252c918afc4cf38be9c7d09b7112075b9adb23490ec9fed1717a8548519d2554`
