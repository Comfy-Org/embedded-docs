# Wan2ReferenceVideoApi

Dieser Node generiert ein Video mit einer Person oder einem Objekt auf Grundlage der bereitgestellten Referenzmaterialien. Er verwendet das Wan 2.7-Modell, um Videos aus einem Text-Prompt zu erstellen, und unterstützt Darbietungen mit einem einzelnen Charakter sowie Interaktionen zwischen mehreren Charakteren. Sie müssen mindestens ein Referenzvideo oder ein Referenzbild bereitstellen, damit die Generierung funktioniert.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das spezifische Modell, das für die Videogenerierung verwendet werden soll. | DYNAMIC_COMBO | Ja | "wan2.7-r2v" |
| `seed` | Seed für die Generierung, der hilft, die Zufälligkeit der Ausgabe zu steuern (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `watermark` | Ob ein KI-generiertes Wasserzeichen zum Ergebnis hinzugefügt werden soll (Standard: False). Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | True<br>False |

### wan2.7-r2v Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt, der das Video beschreibt. Verwenden Sie Bezeichner wie 'character1' und 'character2', um auf die Referenzcharaktere zu verweisen. Muss mindestens einen Charakter enthalten. | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll (Standard: leer). | STRING | Nein | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | "720P"<br>"1080P" |
| `ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Die Länge des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 2 bis 10 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `reference_videos` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Referenzvideos (Slots `video1` bis `video3`). Insgesamt ist mindestens ein Referenzvideo oder Referenzbild erforderlich. | VIDEO | Nein | 0 bis 3 Elemente |
| `reference_images` | Erweiterbarer Slot: Verbinden Sie bis zu 5 Referenzbilder (Slots `image1` bis `image5`). Insgesamt ist mindestens ein Referenzvideo oder Referenzbild erforderlich. | IMAGE | Nein | 0 bis 5 Elemente |

**Wichtige Einschränkungen:**

* Sie müssen mindestens ein Referenzvideo oder Referenzbild in den Eingaben `reference_videos` oder `reference_images` bereitstellen. Andernfalls löst der Node einen Fehler aus.
* Die kombinierte Gesamtzahl von Referenzvideos und Referenzbildern darf 5 nicht überschreiten.
* Die Eingabe `prompt` muss mindestens einen Charakter enthalten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
