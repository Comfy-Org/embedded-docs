# ElevenLabsTextToSoundEffects

Der ElevenLabs Text to Sound Effects-Node erzeugt Audio-Klangeffekte aus einer Textbeschreibung. Er verwendet die ElevenLabs-API, um Klangeffekte basierend auf Ihrem Prompt zu erstellen, sodass Sie die Dauer, das Schleifenverhalten und die Genauigkeit, mit der der Klang dem Text folgt, steuern können.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell für die Klangeffektgenerierung. Derzeit ist nur ein Modell verfügbar: `eleven_sfx_v2`. | DYNAMIC_COMBO | Ja | `"eleven_sfx_v2"` |
| `text` | Textbeschreibung des zu generierenden Klangeffekts. (Standard: leer) | STRING | Ja | N/A |
| `output_format` | Audio-Ausgabeformat. | COMBO | Ja | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### eleven_sfx_v2 Eingaben

Diese Parameter werden angezeigt, wenn das Modell `eleven_sfx_v2` ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `duration` | Dauer des generierten Klangs in Sekunden. (Standard: 5.0) | FLOAT | Ja | 0.5 bis 30.0 |
| `loop` | Erstellt einen nahtlos in einer Schleife laufenden Klangeffekt. (Standard: False) | BOOLEAN | Nein | True<br>False |
| `prompt_influence` | Wie genau die Generierung dem Prompt folgt. Höhere Werte bewirken, dass der Klang dem Text genauer folgt. (Standard: 0.3) | FLOAT | Ja | 0.0 bis 1.0 |

**Hinweis:** Der Parameter `text` darf nicht leer sein; er wird validiert, bevor die Anfrage zur Klanggenerierung gesendet wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die generierte Klangeffekt-Audiodatei. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/de.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
