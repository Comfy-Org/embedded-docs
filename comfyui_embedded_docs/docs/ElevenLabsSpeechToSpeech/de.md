# ElevenLabsSpeechToSpeech

Der ElevenLabs Speech-to-Speech-Node wandelt eine Eingabe-Audiodatei von einer Stimme in eine andere um. Er verwendet die ElevenLabs-API, um Sprache umzuwandeln, wobei der ursprüngliche Inhalt und die emotionale Tonalität des Audios erhalten bleiben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das für die Speech-to-Speech-Transformation verwendet werden soll. Das ausgewählte Modell bestimmt die unten aufgeführten verfügbaren Stimmeinstellungen. | DYNAMIC_COMBO | Ja | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voice` | Zielstimme für die Transformation. Von Voice Selector oder Instant Voice Clone verbinden. | CUSTOM | Ja | - |
| `audio` | Quell-Audio, das transformiert werden soll. | AUDIO | Ja | - |
| `stability` | Stimmstabilität. Niedrigere Werte ermöglichen eine größere emotionale Bandbreite, höhere Werte erzeugen konsistentere, aber möglicherweise monotonere Sprache (Standard: 0.5). | FLOAT | Ja | 0.0 - 1.0 |
| `output_format` | Audio-Ausgabeformat. | COMBO | Ja | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `seed` | Seed für Reproduzierbarkeit (Standard: 0). | INT | Ja | 0 - 4294967295 |
| `remove_background_noise` | Hintergrundgeräusche aus dem Eingabe-Audio mittels Audioisolierung entfernen (Standard: False). | BOOLEAN | Ja | - |

### eleven_multilingual_sts_v2 und eleven_english_sts_v2 Eingaben

Beide Modelle bieten dieselben unten aufgeführten Stimmeinstellungen.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `speed` | Sprachgeschwindigkeit. 1.0 ist normal, <1.0 langsamer, >1.0 schneller (Standard: 1.0). | FLOAT | Ja | 0.7 - 1.3 |
| `similarity_boost` | Ähnlichkeitsverstärkung. Höhere Werte machen die Stimme ähnlicher zum Original (Standard: 0.75). | FLOAT | Ja | 0.0 - 1.0 |
| `use_speaker_boost` | Ähnlichkeit zur ursprünglichen Sprecherstimme verstärken (Standard: False). | BOOLEAN | Ja | - |
| `style` | Stilüberzeichnung. Höhere Werte erhöhen den stilistischen Ausdruck, können aber die Stabilität verringern (Standard: 0.0). | FLOAT | Ja | 0.0 - 0.2 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die transformierte Audiodatei im angegebenen Ausgabeformat. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/de.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
