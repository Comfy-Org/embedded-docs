# Breeze Voice Localize

Erstellt eine Kopie einer Stimme, die eine andere Sprache muttersprachlich spricht, anstatt eine Fremdsprache mit ihrem ursprünglichen Akzent vorzulesen. Die Kopie wird in Ihrem Konto gespeichert und mit einer Audiovorschau zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `voice` | Zu kopierende Breeze-Stimme. | BREEZE_VOICE | Ja | - |
| `language` | Sprache, die die neue Stimme spricht. Standard: `"English"`. | COMBO | Ja | Mehrere Optionen verfügbar |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `voice` | Die lokalisierte Kopie der Stimme, benannt nach der Originalstimme und der Sprache. | BREEZE_VOICE |
| `preview` | Audiovorschau der lokalisierten Stimme. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/de.md)

---
**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`
