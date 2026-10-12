# HeyGen Text-zu-Sprache

Erzeugt Sprach-Audio aus Text mithilfe von HeyGens Starfish-TTS-Engine. Dieser Node enthält HeyGens beliebteste Stimmen in 17 Sprachen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `text` | Text, der synthetisiert werden soll (bis zu 5000 Zeichen). Die erzeugte Sprachausgabe muss mindestens 1 Sekunde lang sein. | STRING | Ja | 1 bis 5000 Zeichen |
| `voice` | Zu verwendende Stimme (ausgewählt aus HeyGens beliebtesten Starfish-kompatiblen Stimmen). | STRING | Ja | Mehrere Optionen verfügbar |
| `custom_voice_id` | Optionale HeyGen-Stimmen-ID. Wenn festgelegt, überschreibt sie die oben ausgewählte Stimme. Die Stimme muss die Starfish-Engine unterstützen (Standard: leer). | STRING | Nein | Jede gültige HeyGen-Stimmen-ID |
| `speed` | Geschwindigkeitsmultiplikator für die Sprachausgabe (Standard: 1.0). | FLOAT | Nein | 0.5 bis 2.0 (Schritt: 0.05) |
| `ssml` | Text als SSML-Markup behandeln (für Pausen, Betonung und Aussprachesteuerung) (Standard: False). | BOOLEAN | Nein | True / False |
| `seed` | Wird nicht an HeyGen gesendet; ändern Sie ihn, um eine erneute Ausführung zu erzwingen (Standard: 42). | INT | Nein | 0 bis 2147483647 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Das aus dem eingegebenen Text erzeugte synthetisierte Sprach-Audio. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTextToSpeechNode/de.md)

---
**Source fingerprint (SHA-256):** `82300626657db8ab16e96ae96b7dfe3291b77bf75efec35971dc772e5123cce7`
