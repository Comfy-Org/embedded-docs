# MiniMax H3 Erneut generieren in 2K

Dieser Node rendert eine MiniMax H3 768P-Videoausgabe erneut in 2K-Auflösung. Er lädt das unveränderte 768P-Video und den exakten Prompt hoch, der zu seiner Generierung verwendet wurde, startet einen MiniMax H3-Neugenerierungsjob und gibt das neu gerenderte 2K-Video zurück. Wenn bei der ursprünglichen Generierung erste oder letzte Frames oder Referenzmedien verwendet wurden, verbinden Sie dieselben Eingaben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, das für die Videoneugenerierung verwendet werden soll. Die Auswahl von „MiniMax H3“ zeigt die Einstellungen für Prompt, Auflösung und Referenzmedien an. | DYNAMIC_COMBO | Ja | "MiniMax H3" |
| `video` | Das MiniMax H3 768P-Ausgabevideo, das neu gerendert werden soll. Verbinden Sie die unveränderte Ausgabe eines MiniMax H3-Video-Nodes (24 FPS, 4-15 Sekunden). 2K-Ausgaben können nicht verwendet werden. | VIDEO | Ja | 24 FPS, 4-15 Sekunden |
| `first_frame` | Erstes Frame-Bild aus der ursprünglichen Generierung, falls eines verwendet wurde. | IMAGE | Nein | Bild |
| `last_frame` | Letztes Frame-Bild aus der ursprünglichen Generierung, falls eines verwendet wurde. | IMAGE | Nein | Bild |
| `watermark` | Ob dem Video ein AIGC-Wasserzeichen hinzugefügt werden soll. Standard ist false. | BOOLEAN | Ja | false / true |

### MiniMax H3 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Der exakte Prompt, der zum Generieren des Quellvideos verwendet wurde. Darf nicht leer sein. | STRING | Ja | Text (mehrzeilig) |
| `resolution` | Auflösung, in der das Quellvideo neu gerendert werden soll. | COMBO | Ja | "2K" |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie `image_1` bis `image_9` (bis zu 9 Bilder). Referenzbilder aus der ursprünglichen Generierung, in derselben Reihenfolge. | IMAGE | Nein | 0-9 Bilder |
| `reference_videos` | Erweiterbarer Slot: Verbinden Sie `video_1` bis `video_3` (bis zu 3 Videos). Referenzvideos aus der ursprünglichen Generierung, in derselben Reihenfolge. | VIDEO | Nein | 0-3 Videos |
| `reference_audios` | Erweiterbarer Slot: Verbinden Sie `audio_1` bis `audio_3` (bis zu 3 Clips). Audioreferenzen aus der ursprünglichen Generierung, in derselben Reihenfolge. Kann nicht ohne ein Referenzbild oder Referenzvideo verwendet werden. | AUDIO | Nein | 0-3 Clips |

### Einschränkungen

- Der `prompt` darf nicht leer sein.
- Das Quellvideo (`video`) muss eine unveränderte MiniMax H3 768P-Ausgabe sein: 24 FPS, Breite und Höhe durch 32 teilbar, höchstens 1.032.192 Gesamtpixel und 107 bis 362 Frames in Schritten von 17 (4 bis 15 Sekunden bei 24 FPS). 2K-Ausgaben können nicht als Quelle verwendet werden.
- `first_frame` und `last_frame` sind nicht mit Referenzmedien (`reference_images`, `reference_videos`, `reference_audios`) kombinierbar. Verwenden Sie Frames für einen Bild-zu-Video-Prompt oder Referenzmedien für einen Referenz-zu-Video-Prompt.
- `reference_audios` erfordert mindestens eine Eingabe von `reference_images` oder `reference_videos`.
- `first_frame`, `last_frame` und jedes `reference_image` müssen ein Seitenverhältnis zwischen 0,4 und 2,5 haben und mindestens 256x256 Pixel groß sein.
- `reference_videos`: Jedes Video muss 23,976 bis 60 FPS und 2 bis 15 Sekunden lang sein; die Gesamtdauer darf 15 Sekunden nicht überschreiten.
- `reference_audios`: Jeder Clip muss 2 bis 15 Sekunden lang sein; die Gesamtdauer darf 15 Sekunden nicht überschreiten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das neu gerenderte MiniMax H3-Video in 2K-Auflösung. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/de.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
