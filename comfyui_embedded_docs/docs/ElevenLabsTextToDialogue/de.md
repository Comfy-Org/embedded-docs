# ElevenLabsTextToDialogue

Der ElevenLabs Text to Dialogue-Node erzeugt aus Text einen Audio-Dialog mit mehreren Sprechern. Er ermöglicht es Ihnen, eine Konversation zu erstellen, indem Sie verschiedene Textzeilen und eigene Stimmen für jeden Teilnehmer angeben. Der Node sendet die Dialoganfrage an die ElevenLabs API und gibt das generierte Audio zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `stability` | Stimmstabilität. Niedrigere Werte ermöglichen eine breitere emotionale Bandbreite, höhere Werte erzeugen konsistentere, aber möglicherweise monotonere Sprache. (Standard: 0.5) | FLOAT | Ja | 0.0 - 1.0 |
| `apply_text_normalization` | Textnormalisierungsmodus. `"auto"` überlässt die Entscheidung dem System, `"on"` wendet die Normalisierung immer an, `"off"` überspringt sie. | COMBO | Ja | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Modell für die Dialoggenerierung (Standard: `"eleven_v4"`). | COMBO | Ja | `"eleven_v3"`<br>`"eleven_v4"`<br>`"eleven_v4_turbo"` |
| `inputs` | Anzahl der Dialogeinträge. Durch Auswahl einer Zahl werden entsprechend viele Text- und Voice-Eingabepaare erzeugt. | DYNAMIC_COMBO | Ja | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | ISO-639-1-Sprachcode (z. B. 'en', 'es', 'ja'). Leer lassen für automatische Erkennung. (Standard: leer) | STRING | Ja | - |
| `seed` | Seed für die Reproduzierbarkeit. (Standard: 1) | INT | Ja | 0 - 4294967295 |
| `output_format` | Audio-Ausgabeformat. | COMBO | Ja | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Eingaben für Dialogeinträge

Gemeinsam für alle `inputs`-Optionen.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `text1` ... `text10` | Textinhalt für den entsprechenden Dialogeintrag. Der Node erstellt ein `text`-Feld für jeden ausgewählten Dialogeintrag. Jeder Textwert muss mindestens ein Zeichen enthalten. | STRING | Ja | - |
| `voice1` ... `voice10` | Stimme für den entsprechenden Dialogeintrag. Von einem Voice Selector- oder Instant Voice Clone-Node verbinden. Der Node erstellt ein `voice`-Feld für jeden ausgewählten Dialogeintrag. | ELEVENLABS_VOICE | Ja | - |

**Hinweis:** Der `inputs`-Selektor kann bis zu 10 Dialogeinträge erstellen. Jeder Eintrag erfordert sowohl ein `text`-Feld als auch ein `voice`-Feld. Der `text`-Wert darf nicht leer sein. Die `voice`-Eingabe erwartet eine Voice-ID, die von einem kompatiblen ElevenLabs Voice-Node bereitgestellt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Das generierte Dialog-Audio mit mehreren Sprechern im ausgewählten Ausgabeformat. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/de.md)

---
**Source fingerprint (SHA-256):** `bff737be0c828990d7286de4372e995295a4716febd388d7cc02c2a9987a6c80`
