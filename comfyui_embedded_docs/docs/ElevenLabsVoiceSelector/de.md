# ElevenLabs-Stimmenauswahl

Der ElevenLabs Voice Selector-Node ermöglicht es Ihnen, eine bestimmte Stimme aus einer vordefinierten Liste von ElevenLabs-Text-to-Speech-Stimmen auszuwählen. Er nimmt einen Stimmennamen als Eingabe entgegen und gibt die entsprechende Stimmenkennung aus, die für die Audiogenerierung benötigt wird. Dieser Node vereinfacht den Prozess der Auswahl einer kompatiblen Stimme für die Verwendung mit anderen ElevenLabs-Audio-Nodes.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `voice` | Wählen Sie eine Stimme aus den vordefinierten ElevenLabs-Stimmen. | STRING | Ja | `"Adam (male, american)"`<br>`"Antoni (male, british)"`<br>`"Arnold (male, american)"`<br>`"Bella (female, american)"`<br>`"Domi (female, american)"`<br>`"Elli (female, american)"`<br>`"Josh (male, american)"`<br>`"Rachel (female, american)"`<br>`"Sam (male, american)"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `voice` | Die eindeutige Kennung für die ausgewählte ElevenLabs-Stimme, die an andere Nodes für die Text-to-Speech-Generierung übergeben werden kann. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/de.md)

---
**Source fingerprint (SHA-256):** `72e2239bb0da15a88cd346ede2051b4fb717f3bf49faaf5d63c0622b03ccd80d`
