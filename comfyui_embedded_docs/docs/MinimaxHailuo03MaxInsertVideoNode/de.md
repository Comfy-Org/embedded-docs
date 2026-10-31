# MiniMax H3 Max Insert Video

Dieser Node ersetzt den Teil eines Videos zwischen der Start- und der Fortsetzungszeit durch eine neu generierte Szene, gesteuert durch einen Prompt und optionale Referenzbilder und -videos. Das Quellvideo wird bei `start_time` geschnitten und bei `resume_time` fortgesetzt; der entfernte Abschnitt wird neu generiert und wieder eingefügt. Verwenden Sie ihn, um eine Aufnahme zu korrigieren, eine Aktion auszutauschen oder zwei Teile eines Clips zu überbrücken.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell, das für die Videogenerierung verwendet werden soll. | DYNAMIC_COMBO | Ja | "MiniMax H3 Max" |

### MiniMax H3 Max Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Quellvideo, bis zu 60 Sekunden lang. Das Seitenverhältnis muss zwischen 0.4 und 2.5 liegen. | VIDEO | Ja | 0 bis 60 Sekunden |
| `reference_images` | Erweiterbarer Slot: Verbinden Sie bis zu 9 optionale Referenzbilder (`image_1`...`image_9`) für die neue Szene, mindestens 256x256 Pixel. Im Prompt werden sie in Verbindungsreihenfolge als `@Image1`..`@Image9` referenziert. | IMAGE | Nein | 0 bis 9 Bilder |
| `reference_videos` | Erweiterbarer Slot: Verbinden Sie bis zu 3 optionale Referenzvideos (`video_1`...`video_3`) für die neue Szene, jeweils 2 bis 15 Sekunden lang und insgesamt 15 Sekunden. Im Prompt werden sie in Verbindungsreihenfolge als `@Video1`..`@Video3` referenziert. | VIDEO | Nein | 0 bis 3 Videos |
| `prompt` | Die neue Szene. Ein Prompt oder mindestens eine Referenz ist erforderlich; Referenzen ohne Prompt werden oft ignoriert. | STRING | Ja | 0 bis 50000 Zeichen |
| `start_time` | Sekunde, an der das Quellvideo stoppt und die neue Szene beginnt (Standard: 2.0). | FLOAT | Ja | 1.625 bis 60.0 |
| `resume_time` | Sekunde, an der das Quellvideo nach der neuen Szene fortgesetzt wird (Standard: 3.0). Muss nach `start_time` liegen und mindestens 1.375 Sekunden vor dem Ende des Videos. Der Quellbereich zwischen `start_time` und `resume_time` wird entfernt. | FLOAT | Ja | 1.625 bis 60.0 |
| `duration` | Länge der neuen Szene in Sekunden (Standard: 5). | INT | Ja | 5 bis 13 |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "480P"<br>"768P" |
| `color_match` | Die Farben der neuen Szene an das Quellvideo anpassen (Standard: true). | BOOLEAN | Nein | true<br>false |
| `prompt_expansion` | Den Prompt mithilfe des Quellvideos umschreiben. Deaktivieren Sie dies, um reproduzierbare Ergebnisse für denselben Seed zu erhalten (Standard: true). | BOOLEAN | Nein | true<br>false |
| `seed` | Zufälliger Seed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Parametereinschränkungen

- `resume_time` muss größer als `start_time` sein und mindestens 1.375 Sekunden vor dem Ende des Videos liegen; andernfalls wird die Anfrage abgelehnt.
- Jedes Referenzvideo muss zwischen 2 und 15 Sekunden lang sein, und alle zusammen dürfen 15 Sekunden nicht überschreiten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das Quellvideo mit der neuen Szene, die zwischen Start- und Fortsetzungszeit eingefügt wurde. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxInsertVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `623ad0b37f51ce4640c0058676e008697e31563c2a77a3da79ba7936af2d3f99`
