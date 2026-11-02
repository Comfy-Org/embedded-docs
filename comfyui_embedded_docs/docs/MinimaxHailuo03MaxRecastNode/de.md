# MiniMax H3 Max Recast

Recast ersetzt die Personen in einem Video durch die Personen aus Referenzfotos und behält dabei Bewegung, Kamera, Schnitte und Ton des Quellclips bei. Das Video wird hochgeladen, der Hailuo 03 Max-Job wird per Polling abgefragt, und das Recast-Video wird in der von Ihnen gewählten Auflösung zurückgegeben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell, das für die Videogenerierung verwendet wird. | DYNAMIC_COMBO | Ja | "MiniMax H3 Max" |

### MiniMax H3 Max Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Quellvideo, 5 bis 30 Sekunden lang; jede Einstellung muss 15 Sekunden oder kürzer sein. Das Seitenverhältnis muss zwischen 0.4 und 2.5 liegen. | VIDEO | Ja | 5 bis 30 Sekunden |
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 1 bis 4 Fotos (`image_1`...`image_4`), eines pro neuer Person, mit mindestens 256x256 Pixeln. Standardmäßig ersetzen sie die Hauptpersonen im Video von links nach rechts. | IMAGE | Ja | 1 bis 4 Bilder |
| `prompt` | Optional. Wer zu wem wird oder was sonst beibehalten oder geändert werden soll. Verweisen Sie auf die Fotos als `@Image1`..`@Image4`, zum Beispiel „der Mann wird zu @Image2“. | STRING | Ja | 0 bis 2000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "768P"<br>"1080P" |
| `enhance_realism` | Natürlichere Hauttexturen und eine bessere Einbindung der neuen Personen in die Szene (Standard: false). | BOOLEAN | Nein | true<br>false |
| `seed` | Zufälliger Seed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 4294967295 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das Recast-Video mit den neuen Personen an den vorgesehenen Stellen. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxRecastNode/de.md)

---
**Source fingerprint (SHA-256):** `a9e6f9edf12653f9f361992a097d1d57e7ba14b3e7dd20008b0e022cabc14c1b`
