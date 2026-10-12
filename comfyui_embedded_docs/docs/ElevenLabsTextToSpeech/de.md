# ElevenLabs Text-zu-Sprache

Der Node ElevenLabs Text to Speech wandelt geschriebenen Text mithilfe der ElevenLabs-API in gesprochenes Audio um. Er ermöglicht die Auswahl einer bestimmten Stimme und die Feinabstimmung verschiedener Spracheigenschaften wie Stabilität, Geschwindigkeit und Stil, um eine individuell angepasste Audioausgabe zu erzeugen. Der Text muss mindestens ein Zeichen enthalten.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das für die Text-zu-Sprache-Konvertierung verwendet werden soll. Bei Auswahl eines Modells werden dessen spezifische Parameter eingeblendet. | DYNAMIC_COMBO | Nein | `"eleven_v4"`<br>`"eleven_v4_turbo"`<br>`"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `voice` | Stimme, die für die Sprachsynthese verwendet werden soll. Von Voice Selector oder Instant Voice Clone verbinden. | CUSTOM | Ja | N/A |
| `text` | Der in Sprache umzuwandelnde Text. Muss mindestens ein Zeichen enthalten. | STRING | Ja | N/A |
| `stability` | Stimmstabilität. Niedrigere Werte ermöglichen eine größere emotionale Bandbreite, höhere Werte erzeugen konsistentere, aber möglicherweise monotonere Sprache (Standard: 0.5). | FLOAT | Nein | 0.0 - 1.0 |
| `apply_text_normalization` | Textnormalisierungsmodus. 'auto' lässt das System entscheiden, 'on' wendet die Normalisierung immer an, 'off' überspringt sie. | COMBO | Nein | `"auto"`<br>`"on"`<br>`"off"` |
| `language_code` | ISO-639-1-Sprachcode (z. B. 'en', 'es', 'ja'). Leer lassen für automatische Erkennung (Standard: ""). | STRING | Nein | N/A |
| `seed` | Seed für Reproduzierbarkeit (Determinismus nicht garantiert) (Standard: 1). | INT | Nein | 0 - 2147483647 |
| `output_format` | Audioausgabeformat. | COMBO | Nein | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### eleven_multilingual_v2 Eingaben

Diese Parameter werden verfügbar, wenn `model` auf `"eleven_multilingual_v2"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `speed` | Sprechgeschwindigkeit. 1.0 ist normal, <1.0 langsamer, >1.0 schneller (Standard: 1.0). | FLOAT | Nein | 0.7 - 1.2 |
| `similarity_boost` | Ähnlichkeitsverstärkung. Höhere Werte machen die Stimme dem Original ähnlicher (Standard: 0.75). | FLOAT | Nein | 0.0 - 1.0 |
| `use_speaker_boost` | Ähnlichkeit zur Stimme des ursprünglichen Sprechers verstärken (Standard: False). | BOOLEAN | Nein | True / False |
| `style` | Stilüberzeichnung. Höhere Werte erhöhen den stilistischen Ausdruck, können aber die Stabilität verringern (Standard: 0.0). | FLOAT | Nein | 0.0 - 0.2 |

### eleven_v3 Eingaben

Diese Parameter werden verfügbar, wenn `model` auf `"eleven_v3"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `speed` | Sprechgeschwindigkeit. 1.0 ist normal, <1.0 langsamer, >1.0 schneller (Standard: 1.0). | FLOAT | Nein | 0.7 - 1.3 |
| `similarity_boost` | Ähnlichkeitsverstärkung. Höhere Werte machen die Stimme dem Original ähnlicher (Standard: 0.75). | FLOAT | Nein | 0.0 - 1.0 |

### eleven_v4 und eleven_v4_turbo Eingaben

Diese Parameter werden verfügbar, wenn `model` auf `"eleven_v4"` oder `"eleven_v4_turbo"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `similarity_boost` | Ähnlichkeitsverstärkung. Höhere Werte machen die Stimme dem Original ähnlicher (Standard: 0.75). | FLOAT | Nein | 0.0 - 1.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Das aus der Text-zu-Sprache-Konvertierung erzeugte Audio. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/de.md)

---
**Source fingerprint (SHA-256):** `2f8aadca9f4fee9614ce4488aa206119ecf714518b7c0c340b1bfa766f59672e`
