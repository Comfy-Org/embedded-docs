# PixverseV6TextToVideoNode

Der Node PixVerse V6 Text to Video erzeugt ein Video aus einem Text-Prompt unter Verwendung des PixVerse-V6-Modells. Der Node sendet den Prompt zusammen mit dem gewählten Seitenverhältnis, der Auflösung, der Dauer und anderen Einstellungen an PixVerse, wartet, bis die Generierung abgeschlossen ist, und gibt anschließend das resultierende Video zurück – einschließlich einer nativen Audiospur, wenn die Audiogenerierung aktiviert ist.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell- und Generierungseinstellungen. Wählen Sie das Modell aus und konfigurieren Sie seine Generierungsoptionen. | DYNAMIC_COMBO | Ja | "PixVerse V6" |

### PixVerse V6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Videogenerierung. (Standard: "") | STRING | Ja | 1–5000 Zeichen |
| `aspect_ratio` | Ausgabe-Seitenverhältnis. Wählen Sie eines der von PixVerse V6 unterstützten Seitenverhältnisse. | COMBO | Ja | Mehrere Optionen verfügbar |
| `quality` | Ausgabeauflösung. Legt die lange Kante fest: 360p entspricht 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (Standard: "720p") | COMBO | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Länge des generierten Videos in Sekunden. (Standard: 5) | INT | Ja | 1–15 |
| `generate_audio` | Generiert eine native Audiospur zusammen mit dem Video. (Standard: True) | BOOLEAN | Ja | True<br>False |
| `multi_clip` | Lässt das Modell das Video in mehrere Einstellungen schneiden, anstatt eine durchgehende Aufnahme zu verwenden. (Standard: False) | BOOLEAN | Ja | True<br>False |
| `seed` | Seed für die Videogenerierung. PixVerse zeichnet ihn auf, reproduziert damit aber keinen Durchlauf. Unterstützt Randomisierung nach der Generierung. (Standard: 42) | INT | Ja | 0–2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente im Video. (Standard: "") | STRING | Nein | 0–2048 Zeichen |
| `style` | Ein optionaler visueller Stil, der auf das gesamte Video angewendet wird. (Standard: "none") | COMBO | Nein | Mehrere Optionen verfügbar |

**Hinweis:** Der Parameter `prompt` ist erforderlich und darf nach dem Entfernen von Leerraum nicht leer sein; seine maximale Länge beträgt 5000 Zeichen. Der Parameter `negative_prompt` ist auf 2048 Zeichen begrenzt. Wenn der Parameter `style` auf "none" (den Standardwert) gesetzt wird, wird kein visueller Stil angewendet. Der Parameter `seed` wird von PixVerse aufgezeichnet, kann aber nicht verwendet werden, um denselben Durchlauf zu reproduzieren. Der Node wartet darauf, dass PixVerse die Videogenerierung abschließt, und lädt das Video anschließend herunter; wenn die Anfrage fehlschlägt – zum Beispiel, weil PixVerse bereits die maximale Anzahl gleichzeitiger Generierungen erreicht hat, dem Anbieterkonto Credits fehlen oder die Inhaltsmoderation den Prompt ablehnt – gibt der Node einen Fehler zurück.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video. Wenn `generate_audio` aktiviert ist, enthält das Video die native Audiospur. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`
