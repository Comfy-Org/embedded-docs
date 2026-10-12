# MoonvalleyTxt2VideoNode

Der Moonvalley Marey Text to Video-Node generiert Videoinhalte aus Textbeschreibungen mithilfe der Moonvalley API. Er nimmt einen Text-Prompt entgegen und wandelt ihn mit anpassbaren Einstellungen für Auflösung, Qualität und Stil in ein Video um. Der Node übernimmt den gesamten Prozess vom Senden der Generierungsanfrage bis zum Herunterladen der finalen Videoausgabe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Textbeschreibung des zu generierenden Videoinhalts | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt-Text (Standard: umfangreiche Liste ausgeschlossener Elemente wie synthetisch, Szenenschnitt, Artefakte, Rauschen usw.) | STRING | Nein | - |
| `resolution` | Auflösung des Ausgabevideos (Standard: "16:9 (1920 x 1080)") | STRING | Nein | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" |
| `prompt_adherence` | Guidance-Skala zur Steuerung der Generierung (Standard: 4.0) | FLOAT | Nein | 1.0-20.0 |
| `seed` | Zufälliger Seed-Wert (Standard: 9) | INT | Nein | 0-4294967295 |
| `steps` | Inferenzschritte (Standard: 33) | INT | Nein | 1-100 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Die generierte Videoausgabe basierend auf dem Text-Prompt | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/de.md)

---
**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`
