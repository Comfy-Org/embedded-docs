# Breeze Voice Remix

Erstellt eine geänderte Kopie einer Stimme in derselben Sprache, entweder aus einer schriftlichen Beschreibung der Änderung oder aus einer benannten Voreinstellung. Die Kopie wird in Ihrem Konto gespeichert und mit einer Audiovorschau zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `voice` | Zu ändernde Breeze-Stimme. | BREEZE_VOICE | Ja | - |
| `change` | `custom` beschreibt die Änderung als Text, `preset` wählt eine benannte Änderung. Standard: `"custom"`. | DYNAMIC_COMBO | Ja | `"custom"`<br>`"preset"` |
| `strength` | Höhere Werte verändern die Stimme stärker. Standard: 4.0. | FLOAT | Nein | 1.0 bis 10.0 (Schritt 0.1) |
| `seed` | Steuert, ob der Knoten erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 2147483647 |

### Eingaben für die Änderung "custom"

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Wie sich die Stimme ändern soll, zum Beispiel älter und rauchig. Standard: leer. | STRING | Ja | Mehrzeiliger Text |

### Eingaben für die Änderung "preset"

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `preset` | Benannte Änderung, gruppiert nach Alter, Geschlecht, Tonhöhe, Tempo, Energie und Emotion. | COMBO | Ja | Mehrere Optionen verfügbar |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `voice` | Die geänderte Kopie der Stimme. | BREEZE_VOICE |
| `preview` | Audiovorschau der neu abgemischten Stimme. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceRemix/de.md)

---
**Source fingerprint (SHA-256):** `1bb135706fa760c6a6e8f4b9cb12a3f1506db375ee09cbd511b62d2bb24a9d2c`
