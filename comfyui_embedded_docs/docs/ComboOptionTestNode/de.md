# ComboOptionTestNode

Dieser Node übernimmt zwei Auswahlen aus Kombinationsfeldern und leitet sie unverändert direkt an seine Ausgaben weiter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `combo` | Die erste Auswahl, ausgewählt aus einer Gruppe von drei Testoptionen. | COMBO | Ja | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | Die zweite Auswahl, ausgewählt aus einer anderen Gruppe von drei Testoptionen. | COMBO | Ja | `"option4"`<br>`"option5"`<br>`"option6"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output_1` | Gibt den im ersten Kombinationsfeld (`combo`) ausgewählten Wert unverändert zurück. | COMBO |
| `output_2` | Gibt den im zweiten Kombinationsfeld (`combo2`) ausgewählten Wert unverändert zurück. | COMBO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/de.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
