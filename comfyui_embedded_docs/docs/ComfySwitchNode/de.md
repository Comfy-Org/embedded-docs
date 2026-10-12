# ComfySwitchNode

Der If/Else Switch-Node wählt anhand einer booleschen Bedingung zwischen zwei möglichen Eingaben aus. Wenn `switch` aktiviert (true) ist, wird die Eingabe `on_true` an den Ausgang weitergegeben; wenn deaktiviert (false), wird `on_false` weitergegeben. Die Eingaben werden lazy ausgewertet, sodass nur der ausgewählte Zweig ausgewertet wird und die andere Eingabe nicht verbunden werden muss.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `switch` | Eine boolesche Bedingung, die bestimmt, welche Eingabe an den Ausgang weitergegeben wird. Wenn aktiviert (true), wird die Eingabe `on_true` ausgewählt. Wenn deaktiviert (false), wird die Eingabe `on_false` ausgewählt. | BOOLEAN | Ja |  |
| `on_false` | Die Daten, die an den Ausgang weitergegeben werden, wenn `switch` deaktiviert (false) ist. Diese Eingabe wird nur angefordert, wenn `switch` false ist. | MATCH_TYPE | Nein |  |
| `on_true` | Die Daten, die an den Ausgang weitergegeben werden, wenn `switch` aktiviert (true) ist. Diese Eingabe wird nur angefordert, wenn `switch` true ist. | MATCH_TYPE | Nein |  |

**Hinweis zu den Eingabeanforderungen:** Die Eingaben `on_false` und `on_true` werden bedingt angefordert. Der Node fragt `on_true` nur ab, wenn `switch` true ist, und fragt `on_false` nur ab, wenn `switch` false ist. Beide Eingaben müssen denselben Datentyp haben, und dieser Typ muss mit dem Datentyp der Ausgabe übereinstimmen. Wenn die ausgewählte Eingabe nicht verbunden ist, gibt der Node keinen Wert aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die ausgewählten Daten: der Wert von `on_true`, wenn `switch` true ist, oder der Wert von `on_false`, wenn `switch` false ist. | MATCH_TYPE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/de.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
