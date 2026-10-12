# LtxvApiImageToVideo

Der LTXV Image To Video-Node erzeugt ein Video in professioneller Qualität aus einem einzelnen Startbild. Er verwendet eine externe API, um anhand Ihres Text-Prompts eine Videosequenz zu erstellen, sodass Sie Dauer, Auflösung und Bildrate anpassen können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Erstes Einzelbild, das für das Video verwendet wird. | IMAGE | Ja | - |
| `model` | Das KI-Modell, das zur Videogenerierung verwendet werden soll. Das Modell „Pro“ ist auf Qualität optimiert, während das Modell „Fast“ auf Geschwindigkeit optimiert ist. | COMBO | Ja | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Eine Textbeschreibung, die den Inhalt und die Bewegung des generierten Videos steuert (Standard: leer). | STRING | Ja | - |
| `duration` | Die Länge des Videos in Sekunden (Standard: 8). | COMBO | Ja | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | Die Ausgabeauflösung des generierten Videos. | COMBO | Ja | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Die Anzahl der Bilder pro Sekunde für das Video (Standard: 25). | COMBO | Ja | `25`<br>`50` |
| `generate_audio` | Wenn auf true gesetzt, enthält das generierte Video KI-generierten Ton, der zur Szene passt (Standard: False). | BOOLEAN | Nein | - |

**Wichtige Einschränkungen:**

* Die Eingabe `image` muss genau ein Bild enthalten.
* Der `prompt` muss zwischen 1 und 10.000 Zeichen lang sein.
* Wenn Sie eine `duration` von mehr als 10 Sekunden auswählen, müssen Sie das Modell **"LTX-2 (Fast)"**, eine Auflösung von **"1920x1080"** und **25** FPS verwenden. Diese Kombination ist für längere Videos erforderlich.

**Hinweis:** Dieser Node ist als veraltet markiert. Die auf dem Node angezeigten geschätzten Kosten hängen vom ausgewählten `model`, `duration` und `resolution` ab.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`
