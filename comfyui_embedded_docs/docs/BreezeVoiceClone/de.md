# Breeze Voice Clone

Erstellt eine Breeze-Stimme aus einer Aufnahme eines einzelnen Sprechers. Die Stimme wird in Ihrem Konto gespeichert und als Voice-Handle zurückgegeben, zusammen mit einer Audiovorschau, die zeigt, wie sie klingt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Aufnahme eines einzelnen Sprechers, mindestens 3 Sekunden lang. Nur die ersten 60 Sekunden werden verwendet. | AUDIO | Ja | - |
| `remove_background_noise` | Bereinigt die Aufnahme vor dem Klonen. Standard: false. | BOOLEAN | Nein | true<br>false |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `voice` | Die neue Breeze-Stimme für Breeze Text to Speech. | BREEZE_VOICE |
| `preview` | Audiovorschau der geklonten Stimme. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/de.md)

---
**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`
