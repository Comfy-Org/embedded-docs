# Breeze Voice Selector

Wählt eine vorgestellte Breeze-Stimme oder eine beliebige Breeze-Stimmen-ID aus und übergibt sie an Breeze Text to Speech. Der Node löst nur eine ID auf und führt keinen API-Aufruf aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `language` | Sprachgruppe der vorgestellten Stimmen oder `custom`, um eine ID einzugeben. Standard: `"English"`. | DYNAMIC_COMBO | Ja | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### Eingaben für Sprache "English", "Chinese" und "Japanese"

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `voice` | Vorgestellte Stimme in dieser Sprache. | COMBO | Ja | Mehrere Optionen verfügbar |

### Eingaben für Sprache "custom"

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `voice_id` | Beliebige Breeze-Stimmen-ID, beispielsweise eine Stimme, die von den anderen Breeze-Nodes erstellt wurde. Nur Buchstaben, Ziffern, `_` und `-`. Standard: leer. | STRING | Ja | Breeze-Stimmen-ID |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `voice` | Die ausgewählte Breeze-Stimme. | BREEZE_VOICE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/de.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`
