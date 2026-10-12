# Vidu4ReferenceVideoNode

Generieren Sie ein Video aus Referenzbildern, optionalem Referenzaudio und einem Prompt mit einem Vidu Q4-Modell. Dies ist die Referenz-zu-Video-Variante der Vidu Q4-Generierungs-Nodes.

Die Auswahl eines `model` zeigt die für dieses Modell spezifischen Parameter an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell zur Videogenerierung. Die Auswahl eines Modells zeigt die für dieses spezifischen Parameter an: `reference_images`, `reference_audios`, `prompt`, `aspect_ratio`, `resolution`, `duration`, `audio` und `seed`. | DYNAMIC_COMBO | Ja | `"Vidu Q4 Preview"` |
| `reference_images` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzbilder (`image_1`, `image_2`, ...) für das generierte Video; jedes Bild eines Batches zählt zur Gesamtzahl. Verweisen Sie im Prompt der Reihenfolge nach darauf: Bild 1, Bild 2 und so weiter. | IMAGE | Ja | Bis zu 15 Bilder |
| `reference_audios` | Erweiterbarer Slot: Verbinden Sie optionale Stimmreferenzen (`audio_1`, `audio_2`, `audio_3`), jeweils 3 bis 12 Sekunden. Es wird nur die Stimme verwendet, nicht die Wörter: Schreiben Sie den Dialog in den Prompt und weisen Sie eine Stimme der Reihenfolge nach zu, zum Beispiel `image 1 says "Hello!" in the voice from audio 1`. Erfordert, dass `audio` aktiviert ist. | AUDIO | Nein | Bis zu 3 Clips |
| `prompt` | Eine textliche Beschreibung für die Videogenerierung, bis zu 5000 Zeichen. Erforderlich, um die Referenzen zu beschreiben, die Sie verwenden möchten. | STRING | Ja | Beliebiger Text |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"3:4"`<br>`"4:3"` |
| `resolution` | Auflösung des Ausgabevideos (Standard: `"720p"`). | COMBO | Ja | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 3 bis 16 |
| `audio` | Wenn aktiviert, wird Video mit Ton ausgegeben, einschließlich Dialog und Soundeffekten (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Dieser Parameter hat eine „Control after generate"-Funktionalität (Standard: 42). | INT | Ja | 1 bis 2147483647 |

**Hinweis:** Insgesamt können höchstens 15 Referenzbilder verwendet werden, wobei jedes Bild eines Batches zählt. Jedes Bild muss mindestens 128x128 Pixel groß sein und ein Seitenverhältnis zwischen 1:5 und 5:1 aufweisen. Referenzaudio erfordert, dass `audio` aktiviert ist, andernfalls wird ein Fehler ausgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ReferenceVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `f37ceec93a6140d69332415b8fd748d55e6a608177430975b4b42ab33e593489`
