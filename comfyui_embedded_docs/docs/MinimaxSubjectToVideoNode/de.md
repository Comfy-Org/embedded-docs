# MinimaxSubjectToVideoNode

Erzeugt synchron ein Video basierend auf einem Subjektbild und einem Text-Prompt unter Verwendung der MiniMax-API. Dieser Node nimmt ein Bild eines Subjekts und eine Beschreibung entgegen, um ein Video zu erstellen, das dieses Subjekt gemäß dem Prompt animiert oder zeigt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `subject` | Bild des Subjekts, auf das für die Videogenerierung referenziert werden soll | IMAGE | Ja | - |
| `prompt_text` | Text-Prompt zur Steuerung der Videogenerierung (Standard: leerer String) | STRING | Ja | - |
| `model` | Modell, das für die Videogenerierung verwendet werden soll (Standard: "S2V-01") | COMBO | Nein | `"S2V-01"` |
| `seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0) | INT | Nein | 0 bis 18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video basierend auf dem eingegebenen Subjektbild und dem Prompt | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `e7d496d8e24a776bbea4afe102858e7d31c4f2e273889703eb02cc61e8389055`
