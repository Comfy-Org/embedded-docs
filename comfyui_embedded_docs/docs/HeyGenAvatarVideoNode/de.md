# HeyGenAvatarVideoNode

Erzeugt ein Talking-Presenter-Video aus einem HeyGen-Avatar. Dieser Node erstellt ein Video eines KI-Avatars, der Ihren bereitgestellten Text spricht oder Lippensynchronisation zu Ihrem eigenen Audio durchführt, unter Verwendung der Rendering-Engines von HeyGen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `engine` | Rendering-Engine; jede Option listet nur die Avatare auf, die sie unterstützt. `"auto"` bietet jeden Avatar an und wählt seine beste Engine (Avatar IV wird bevorzugt). Avatar V hat die höchste Wiedergabetreue, Avatar III ist am kostengünstigsten. | DYNAMIC_COMBO | Ja | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | Optionale HeyGen-Avatar-Look-ID. Wenn gesetzt, überschreibt sie den oben ausgewählten Avatar. Jeder der über 3000 öffentlichen Looks von HeyGen (oder Ihre privaten Avatare) kann verwendet werden. Standard: `""`. | STRING | Nein |  |
| `speech` | Steuert den Avatar mit einem Textskript (HeyGen Text-to-Speech) oder Ihrem eigenen Audio. Anzeigename: „Sprachquelle“. | DYNAMIC_COMBO | Ja | `"script"`<br>`"audio"` |
| `resolution` | Ausgabeauflösung des Videos. Standard: `"1080p"`. | COMBO | Nein | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Ausgabe-Seitenverhältnis. `"auto"` folgt dem Quellmaterial des Avatars. Standard: `"auto"`. | COMBO | Nein | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Optionale einfarbige Hintergrundfarbe als Hex-Code (z. B. `"#00ff00"`). Leer lassen, um den eigenen Hintergrund des Avatars zu verwenden. Wenn angegeben, muss der Wert mit `#` beginnen. Standard: `""`. | STRING | Nein |  |
| `seed` | Wird nicht an HeyGen gesendet; ändern Sie ihn, um einen erneuten Lauf zu erzwingen. Standard: `42`. | INT | Nein | Min.: 0<br>Max.: 2147483647 |

### `auto` Eingaben

Wenn `engine` auf `"auto"` gesetzt ist, ist der folgende Unterparameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `avatar` | Avatar-Look zur Darstellung des Videos (aus der öffentlichen Bibliothek von HeyGen kuratiert). Die beste Engine, die der Look unterstützt, wird automatisch ausgewählt. | COMBO | Ja | Mehrere Optionen verfügbar |

### `avatar_iv` Eingaben

Wenn `engine` auf `"avatar_iv"` gesetzt ist, ist der folgende Unterparameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `avatar` | Avatar-Looks, die die Avatar-IV-Engine unterstützen. | COMBO | Ja | Mehrere Optionen verfügbar |

### `avatar_iii` Eingaben

Wenn `engine` auf `"avatar_iii"` gesetzt ist, ist der folgende Unterparameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `avatar` | Avatar-Looks, die die Avatar-III-Engine unterstützen. | COMBO | Ja | Mehrere Optionen verfügbar |

### `avatar_v` Eingaben

Wenn `engine` auf `"avatar_v"` gesetzt ist, ist der folgende Unterparameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `avatar` | Avatar-Looks, die die Avatar-V-Engine unterstützen. | COMBO | Ja | Mehrere Optionen verfügbar |

### `script` Eingaben

Wenn `speech` auf `"script"` gesetzt ist, sind die folgenden Unterparameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `text` | Text, den der Avatar sprechen soll (bis zu 5000 Zeichen). Die generierte Sprache muss mindestens 1 Sekunde lang sein. Standard: `""`. | STRING | Ja | Min.: 1 Zeichen<br>Max.: 5000 Zeichen |
| `voice` | Stimme für das Skript. Die Standardoption verwendet die Stimme, die HeyGen dem Avatar zugewiesen hat. Wird ignoriert, wenn `custom_voice_id` gesetzt ist. | COMBO | Ja | `"(avatar's default voice)"`<br>Mehrere allgemeine Stimmenoptionen verfügbar |
| `custom_voice_id` | Optionale HeyGen-Stimmen-ID. Wenn gesetzt, überschreibt sie die oben ausgewählte Stimme. Jede Stimme aus der HeyGen-Bibliothek (2000+) kann verwendet werden. Standard: `""`. | STRING | Nein |  |
| `voice_speed` | Sprachgeschwindigkeitsmultiplikator. Standard: `1.0`. | FLOAT | Nein | Min.: 0.5<br>Max.: 1.5<br>Schritt: 0.05 |

### `audio` Eingaben

Wenn `speech` auf `"audio"` gesetzt ist, ist der folgende Unterparameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `audio` | Audio, zu dem der Avatar lippensynchronisiert wird, bis zu 10 Minuten. | AUDIO | Ja |  |

Hinweis: `engine` und `speech` sind Selektoren, die abhängig vom gewählten Wert unterschiedliche Unterparameter einblenden. Der Selektor `speech` hat zwei sich gegenseitig ausschließende Modi: Im Modus `"script"` ist `text` erforderlich; wenn `custom_voice_id` angegeben ist, überschreibt es `voice`. Im Modus `"audio"` synchronisiert der Avatar die Lippen mit dem bereitgestellten Audioclip. Wenn angegeben, muss `background_color` ein Hex-Farbcode sein, der mit `#` beginnt. Wenn `custom_avatar_id` gesetzt ist, überschreibt es die Auswahl `avatar`, und die ausgewählte `engine` muss von diesem Avatar-Look unterstützt werden; andernfalls wird ein Fehler ausgelöst, es sei denn, `engine` ist `"auto"`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `VIDEO` | Das generierte Avatar-Präsentator-Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`
