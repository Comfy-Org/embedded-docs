# Vidu2ReferenceVideoNode

Der Node „Vidu2 Reference-to-Video Generation“ erstellt ein Video aus einem Text-Prompt und mehreren Referenzbildern. Sie können bis zu sieben Subjekte definieren, jedes mit einem eigenen Satz von Referenzbildern, und sie im Prompt mit `@subject{subject_id}` referenzieren. Der Node generiert ein Video mit konfigurierbarer Dauer, Seitenverhältnis und Bewegung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das KI-Modell, das für die Videogenerierung verwendet wird. | COMBO | Ja | `"viduq2"` |
| `subjects` | Geben Sie für jedes Subjekt bis zu 3 Referenzbilder an (insgesamt 7 Bilder über alle Subjekte hinweg). Referenzieren Sie sie in Prompts über `@subject{subject_id}`. | AUTOGROW | Ja | N/A |
| `prompt` | Die Textbeschreibung, die zur Steuerung der Videogenerierung verwendet wird. Wenn der Parameter `audio` aktiviert ist, enthält das Video generierte Sprache und Hintergrundmusik basierend auf diesem Prompt. | STRING | Ja | N/A |
| `audio` | Wenn aktiviert, enthält das Video generierte Sprache und Hintergrundmusik basierend auf dem Prompt (Standard: `False`). | BOOLEAN | Nein | N/A |
| `duration` | Die Länge des generierten Videos in Sekunden (Standard: `5`). | INT | Nein | 1 bis 10 |
| `seed` | Eine Zahl, die verwendet wird, um die Zufälligkeit der Generierung für reproduzierbare Ergebnisse zu steuern (Standard: `1`). | INT | Nein | 0 bis 2147483647 |
| `aspect_ratio` | Die Form des Videobildes. | COMBO | Nein | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `resolution` | Die Pixelauflösung des Ausgabevideos (Standard: `"720p"`). | COMBO | Nein | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | Steuert die Bewegungsamplitude von Objekten im Bild (Standard: `"auto"`). | COMBO | Nein | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Einschränkungen:**

* Der `prompt` muss zwischen 1 und 2000 Zeichen lang sein.
* Sie können mehrere Subjekte definieren, aber die Gesamtzahl der Referenzbilder über alle Subjekte hinweg darf 7 nicht überschreiten.
* Jedes einzelne Subjekt kann maximal 3 Referenzbilder haben.
* Jedes Referenzbild muss ein Breiten-zu-Höhen-Verhältnis zwischen 1:4 und 4:1 haben.
* Jedes Referenzbild muss mindestens 128 Pixel in Breite und Höhe haben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `da4b0a24e186f24cff8031c786bb765299b00bbfa13cc4161d53d3a68e466744`
