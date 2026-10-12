# PixverseV6ExtendVideoNode

This node continues an existing video using the PixVerse V6 model, optionally generating a native audio track alongside the continuation. The source video must be shorter than 40 seconds and no larger than 1920 pixels on either side. The output keeps the source video's resolution, so the quality setting controls how well the continuation is rendered rather than the frame size.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Video, das fortgesetzt werden soll. | VIDEO | Ja | Kürzer als 40 Sekunden; höchstens 1920 Pixel Breite und Höhe |
| `model` | Modell- und Generierungseinstellungen. | DYNAMIC_COMBO | Ja | "PixVerse V6" |

### PixVerse V6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der beschreibt, wie das Video fortgesetzt werden soll. (Standard: leer) | STRING | Ja | 1–5000 Zeichen |
| `quality` | Renderqualität der generierten Fortsetzung: 1080p sieht deutlich besser aus als 540p oder 360p. Es wird nie skaliert – die Ausgabe behält die Auflösung des Quellvideos bei. (Standard: "720p") | COMBO | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Länge des generierten Videos in Sekunden. (Standard: 5) | INT | Ja | 1–15 |
| `generate_audio` | Eine native Audiospur zusammen mit dem Video generieren. (Standard: true) | BOOLEAN | Ja | true / false |
| `seed` | Seed für die Videogenerierung. PixVerse zeichnet ihn auf, reproduziert damit aber keinen Durchlauf. (Standard: 42) | INT | Ja | 0–2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente im Video. (Standard: leer) | STRING | Nein | Bis zu 2048 Zeichen |
| `style` | Ein optionaler visueller Stil, der auf das gesamte Video angewendet wird. (Standard: "none") | COMBO | Nein | Mehrere Optionen verfügbar; "none" ist der Standard |

**Hinweis:** Das Quell-`video` muss kürzer als 40 Sekunden und an Breite und Höhe jeweils höchstens 1920 Pixel groß sein; längere oder größere Videos werden abgelehnt. Die generierte Ausgabe behält die Auflösung des Quellvideos bei, daher steuert `quality`, wie gut die Fortsetzung gerendert wird, und nicht die Bildgröße. Der `prompt` ist erforderlich und muss nach dem Entfernen von Leerzeichen zwischen 1 und 5000 Zeichen lang sein. Der `negative_prompt` ist, sofern angegeben, auf 2048 Zeichen begrenzt. Der `seed` wird von PixVerse aufgezeichnet, kann aber nicht verwendet werden, um denselben Durchlauf zu reproduzieren.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Fortsetzungsvideo, in derselben Auflösung wie das Quellvideo. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ExtendVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `8bd2a04a5da95b39fb963922e2e54a7aa4efb670260fa38313d21db3af295029`
