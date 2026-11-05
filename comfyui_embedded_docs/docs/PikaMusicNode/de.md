# Pika Music

Dieser Node erzeugt mit Pika Musik aus einer Textbeschreibung und optionalem Songtext oder covert einen von Ihnen bereitgestellten Song. Wählen Sie `"text to music"`, um einen neuen Song in einer von Ihnen festgelegten Länge zu schreiben, oder `"cover"`, um einen Song neu aufzunehmen und seine Länge beizubehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mode` | Was der Node tut: `"text to music"` schreibt einen neuen Song, `"cover"` nimmt einen bereitgestellten Song neu auf. Jeder Modus blendet unten seine eigenen Eingaben ein. Standard: `"text to music"`. | DYNAMIC_COMBO | Ja | `"text to music"`<br>`"cover"` |

### Eingaben für Text zu Musik

Diese Eingaben erscheinen, wenn `mode` auf `"text to music"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Wie die Musik klingen soll. Darf nicht leer sein. Standard: "" (leerer String). | STRING | Ja | 1 bis 4000 Zeichen |
| `lyrics` | Optionaler Songtext. Abschnitts-Tags wie `[Verse]` und `[Chorus]` sind erlaubt. Standard: "" (leerer String). | STRING | Ja | 0 bis 8000 Zeichen |
| `duration` | Länge des Songs in Sekunden. Standard: 30.0. | FLOAT | Ja | 10.0 bis 360.0 (Schritt: 0.1) |
| `rewrite_prompt` | Erweitert einen kurzen oder vagen Prompt vor der Generierung mit einem Modell. Standard: False. | BOOLEAN | Ja | true<br>false |
| `seed` | Seed für das Sampling. Standard: 42. | INT | Ja | 0 bis 2147483647 |

### Cover-Eingaben

Diese Eingaben erscheinen, wenn `mode` auf `"cover"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `source_audio` | Der zu covernde Song. Das Ergebnis hat dieselbe Länge, begrenzt auf 5 bis 360 Sekunden. | AUDIO | Ja | - |
| `prompt` | Wie das Cover klingen soll. Darf nicht leer sein. Standard: "" (leerer String). | STRING | Ja | 1 bis 4000 Zeichen |
| `lyrics` | Optionaler Songtext. Abschnitts-Tags wie `[Verse]` und `[Chorus]` sind erlaubt. Standard: "" (leerer String). | STRING | Ja | 0 bis 8000 Zeichen |
| `rewrite_prompt` | Erweitert einen kurzen oder vagen Prompt vor der Generierung mit einem Modell. Standard: False. | BOOLEAN | Ja | true<br>false |
| `seed` | Seed für das Sampling. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:**

* Der Prompt muss zwischen 1 und 4000 Zeichen lang sein, der Songtext höchstens 8000 Zeichen.
* Der Cover-Modus ignoriert `duration`: Die Ausgabe entspricht der Länge von `source_audio`, begrenzt auf 5 bis 360 Sekunden.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Der generierte Song oder das Cover des bereitgestellten Titels. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaMusicNode/de.md)

---
**Source fingerprint (SHA-256):** `e3051b2d0cfff72cf7e359d7383f4e0d133df0338ff42a00f0649387f504ec28`
