# FishAudioVoiceSelector

Der Fish Audio Voice Selector-Node wählt eine Stimme aus der Fish Audio-Bibliothek für die Text-zu-Sprache-Generierung aus. Sie können eine der integrierten Voreinstellungen wählen oder "custom" auswählen, um eine beliebige Voice-Modell-ID von fish.audio einzugeben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `voice` | Wählen Sie eine Stimme oder 'custom', um eine beliebige fish.audio Voice-Modell-ID einzugeben. | DYNAMIC_COMBO | Ja | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Die voreingestellten Stimmenoptionen decken Englisch (en), Chinesisch (zh) und Japanisch (ja) ab und erfordern keine zusätzlichen Eingaben.

### Benutzerdefinierte Eingaben

Diese Eingaben erscheinen, wenn `voice` auf "custom" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | Voice-Modell-ID von fish.audio, z. B. die ID in https://fish.audio/m/<id>/. Standard: leerer String. | STRING | Ja | Beliebige gültige Fish Audio Voice-Modell-ID |

Hinweis: Wenn `voice` auf "custom" gesetzt ist, darf `voice_id` nach dem Trimmen von Leerzeichen nicht leer sein; andernfalls löst der Node einen Fehler "Custom voice ID is empty." aus. Wenn eine nicht erkannte Stimmenoption übergeben wird, löst der Node einen Fehler "Unknown voice" aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `voice` | Die ausgewählte Fish Audio Voice-Modell-ID. Für eine voreingestellte Stimme wird die entsprechende Voice-ID aus der Fish Audio-Bibliothek zurückgegeben; für "custom" wird der eingegebene `voice_id`-Wert zurückgegeben. | FISHAUDIO_VOICE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/de.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
