# Breeze Voice Design

Erstellt eine neue Breeze-Stimme aus einer schriftlichen Beschreibung. Geben Sie eine Beschreibung der Stimme und einen Satz an, den sie sprechen soll; die Stimme wird aus dieser Vorschau erstellt und in Ihrem Konto gespeichert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `description` | Beschreibung der Stimme mit 3 bis 500 Zeichen: Alter, Geschlecht, Akzent, Ton, Tempo. Standard: leer. | STRING | Ja | 3 bis 500 Zeichen |
| `preview_text` | Der Satz, den die neue Stimme in der Vorschau spricht, bis zu 500 Zeichen. Schreiben Sie ihn in der ausgewählten Sprache, da die Stimme aus dieser Vorschau erstellt wird. Standard: leer. | STRING | Ja | 1 bis 500 Zeichen |
| `language` | Sprache des Vorschautextes. Englisch und Chinesisch können beide Modelle verwenden; andere Sprachen verwenden Breeze TTS 2 Multilingual. | DYNAMIC_COMBO | Ja | Mehrere Optionen verfügbar |
| `strength` | Wie genau die Stimme der Beschreibung folgt. Standard: 4.0. | FLOAT | Nein | 1.0 bis 10.0 (Schritt: 0.1) |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 2147483647 |

### Eingaben für die Sprachen „English" und „Chinese"

Diese werden nur angezeigt, wenn `language` auf English oder Chinese gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` oder `Breeze TTS 2 Multilingual`. Standard: `"Breeze TTS 2"`. | COMBO | Ja | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `voice` | Die neue Breeze-Stimme, benannt nach der Beschreibung. | BREEZE_VOICE |
| `preview` | Audio-Vorschau der entworfenen Stimme. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceDesign/de.md)

---
**Source fingerprint (SHA-256):** `5b0ea4ccd03e442972a71ec839be7b755f569686400e472967a09a956de0982f`
