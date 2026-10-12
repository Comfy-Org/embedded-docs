# Grok Video

Der Node Grok Video erzeugt ein kurzes Video aus einer Textbeschreibung. Er kann mithilfe eines Prompts ein Video von Grund auf neu erstellen oder aus einem einzelnen Eingabebild ein Video generieren. Der Node sendet die Anfrage an eine externe API und gibt das generierte Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Videoerzeugung zu verwendende Modell (Standard: `"grok-imagine-video-1.5-lite"`). | COMBO | Ja | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"`<br>`"grok-imagine-video-1.5-lite"` |
| `prompt` | Textbeschreibung des gewünschten Videos. Optional für die Modelle `grok-imagine-video-1.5`, wenn ein Eingabebild bereitgestellt wird. | STRING | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. `1080p` ist für `grok-imagine-video` nicht verfügbar. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. Wird ignoriert, wenn ein Eingabebild bereitgestellt wird; das Video folgt dann dem Seitenverhältnis des Bildes. | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden (Standard: 6). | INT | Ja | 1 bis 15 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `image` | Optionales Startbild. Wenn es weggelassen wird, wird das Video allein aus dem Text-Prompt generiert. | IMAGE | Nein | - |

**Hinweis:** Wenn ein `image` bereitgestellt wird, wird nur ein Eingabebild unterstützt; die Angabe mehrerer Bilder führt zu einem Fehler. Der `prompt` muss nach dem Entfernen von Leerzeichen nicht leer sein, wenn kein Bild bereitgestellt wird oder wenn `grok-imagine-video` verwendet wird, selbst mit einem Bild. Für die Modelle `grok-imagine-video-1.5` ist der `prompt` nur dann optional, wenn ein Eingabebild bereitgestellt wird. Die Auflösung `1080p` ist für `grok-imagine-video` nicht verfügbar. Wenn `aspect_ratio` auf `"auto"` gesetzt ist, wird das Seitenverhältnis automatisch vom Dienst gewählt; wenn ein Eingabebild bereitgestellt wird, wird `aspect_ratio` ignoriert und das Video folgt dem Seitenverhältnis des Bildes.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `ed5a1c39598a319d5b350b19f39a352dedd1150471695d25f7637fc0f8735d02`
