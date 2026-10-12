# MoonvalleyImg2VideoNode

Der Node „Moonvalley Marey Image to Video“ wandelt ein Referenzbild mithilfe der Moonvalley API in ein Video um. Er nimmt ein Eingabebild und einen Text-Prompt entgegen, um ein Video mit angegebener Auflösung, Qualitätseinstellungen und kreativen Steuerungsmöglichkeiten zu generieren. Der Node übernimmt den gesamten Prozess vom Hochladen des Bildes bis zur Videogenerierung und zum Download.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Referenzbild, das zur Videogenerierung verwendet wird | IMAGE | Ja | - |
| `prompt` | Textbeschreibung für die Videogenerierung (mehrzeilige Eingabe) | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt-Text, um unerwünschte Elemente auszuschließen (Standard: umfangreiche Liste negativer Prompts) | STRING | Nein | - |
| `resolution` | Auflösung des Ausgabevideos (Standard: "16:9 (1920 x 1080)") | COMBO | Nein | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" |
| `prompt_adherence` | Guidance-Skala zur Steuerung der Generierung (Standard: 4.5, Schrittweite: 1.0) | FLOAT | Nein | 1.0 - 20.0 |
| `seed` | Zufälliger Seed-Wert (Standard: 9, Steuerung nach Generierung aktiviert) | INT | Nein | 0 - 4294967295 |
| `steps` | Anzahl der Denoising-Schritte (Standard: 33, Schrittweite: 1) | INT | Nein | 1 - 100 |

**Einschränkungen:**

- Das Eingabebild muss Abmessungen zwischen 300x300 Pixeln und der maximal zulässigen Höhe/Breite haben
- Die Textlänge von Prompt und Negative Prompt ist auf die maximale Prompt-Länge von Moonvalley Marey begrenzt

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videoausgabe | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/de.md)

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`
