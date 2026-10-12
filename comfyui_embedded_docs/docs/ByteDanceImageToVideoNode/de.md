# ByteDance Bild zu Video

Der Node „ByteDance Image to Video“ generiert über eine API Videos mit ByteDance-Modellen auf Basis eines Eingabebilds und eines Text-Prompts. Er nimmt ein Startbild als erstes Frame und erstellt eine Videosequenz, die der bereitgestellten Beschreibung folgt. Der Node bietet verschiedene Anpassungsoptionen für Videoauflösung, Seitenverhältnis, Dauer und andere Generierungsparameter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Videogenerierung zu verwendende ByteDance-Modell (Standard: `"seedance-1-0-pro-fast-251015"`). | COMBO | Ja | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Der Text-Prompt, der zur Generierung des Videos verwendet wird. Muss nach dem Entfernen von Leerzeichen mindestens 1 Zeichen lang sein. | STRING | Ja | - |
| `image` | Das erste Frame, das für das Video verwendet wird. Muss zwischen 300x300 und 6000x6000 Pixeln liegen, mit einem Seitenverhältnis zwischen 0,4 und 2,5. | IMAGE | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden (Standard: 5). Für das Modell `seedance-1-5-pro-251215` beträgt die minimal unterstützte Dauer 4 Sekunden. | INT | Ja | 3 - 12 |
| `seed` | Seed, der für die Generierung verwendet werden soll (Standard: 0). | INT | Nein | 0 - 2147483647 |
| `camera_fixed` | Gibt an, ob die Kamera fixiert werden soll. Die Plattform hängt eine Anweisung zum Fixieren der Kamera an Ihren Prompt an, garantiert aber nicht den tatsächlichen Effekt (Standard: False). | BOOLEAN | Nein | `False`<br>`True` |
| `watermark` | Ob dem Video ein „AI generated“-Wasserzeichen hinzugefügt werden soll (Standard: False). | BOOLEAN | Nein | `False`<br>`True` |
| `generate_audio` | Dieser Parameter wird für alle Modelle außer `seedance-1-5-pro-251215` ignoriert (Standard: False). | BOOLEAN | Nein | `False`<br>`True` |

**Hinweis:** Der Prompt darf die folgenden Wörter nicht enthalten (Groß-/Kleinschreibung wird nicht unterschieden): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Diese Parameter werden über ihre jeweiligen Eingaben festgelegt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei basierend auf den Eingabeparametern für Bild und Prompt. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`
