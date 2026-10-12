# ByteDanceImageReferenceNode

Der ByteDance Image Reference Node generiert Videos mithilfe eines Text-Prompts und ein bis vier Referenzbildern. Er sendet die Bilder und den Prompt an einen externen API-Dienst, der ein Video erstellt, das Ihrer Beschreibung entspricht und dabei den visuellen Stil und den Inhalt Ihrer Referenzbilder einbezieht. Der Node bietet verschiedene Steuerelemente für Videoauflösung, Seitenverhältnis, Dauer und andere Generierungsparameter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das KI-Modell, das für die Videogenerierung verwendet werden soll (Standard: `"seedance-1-0-lite-i2v-250428"`). | STRING | Ja | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` |
| `prompt` | Der Text-Prompt, der zur Generierung des Videos verwendet wird. | STRING | Ja | - |
| `images` | Ein bis vier Bilder. Jedes Bild muss zwischen 300x300 und 6000x6000 Pixeln groß sein, mit einem Seitenverhältnis zwischen 0,4 und 2,5. | IMAGE | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | STRING | Ja | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos (Standard: `"adaptive"`). | STRING | Ja | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 3 - 12 |
| `seed` | Seed für die Generierung (Standard: 0). | INT | Nein | 0 - 2147483647 |
| `watermark` | Ob ein "AI generated"-Wasserzeichen zum Video hinzugefügt werden soll (Standard: False). | BOOLEAN | Nein | - |

**Hinweis:** Der Prompt-Text darf die folgenden Parameterzeichenfolgen nicht enthalten: `--resolution`, `--ratio`, `--duration`, `--seed` oder `--watermark`. Diese Werte werden ausschließlich über ihre dedizierten Eingabe-Widgets gesteuert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei basierend auf dem Eingabe-Prompt und den Referenzbildern. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/de.md)

---
**Source fingerprint (SHA-256):** `77a0f9aee920d07a1374eaec8489eed494a4505369246c16007765d67e52ef99`
