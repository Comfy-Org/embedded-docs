# ComfySoftSwitchNode

Der Node Soft Switch wählt anhand einer booleschen Bedingung zwischen zwei möglichen Eingabewerten. Er gibt den Wert der Eingabe `on_true` aus, wenn `switch` wahr ist, und den Wert der Eingabe `on_false`, wenn `switch` falsch ist. Dieser Node ist auf Lazy-Auswertung ausgelegt, d. h., er wertet nur die Eingabe aus, die je nach Schaltzustand tatsächlich benötigt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `switch` | Die boolesche Bedingung, die bestimmt, welche Eingabe durchgelassen wird. Wenn wahr, wird die Eingabe `on_true` ausgewählt. Wenn falsch, wird die Eingabe `on_false` ausgewählt. | BOOLEAN | Ja | True or False |
| `on_false` | Der Wert, der ausgegeben wird, wenn die Bedingung `switch` falsch ist. Diese Eingabe ist optional, aber mindestens eine der Eingaben `on_false` oder `on_true` muss verbunden sein. | MATCH_TYPE | Nein | Gleicher Datentyp wie `on_true` |
| `on_true` | Der Wert, der ausgegeben wird, wenn die Bedingung `switch` wahr ist. Diese Eingabe ist optional, aber mindestens eine der Eingaben `on_false` oder `on_true` muss verbunden sein. | MATCH_TYPE | Nein | Gleicher Datentyp wie `on_false` |

**Hinweis:** Die Eingaben `on_false` und `on_true` müssen denselben Datentyp haben, wie durch das interne Template des Nodes definiert. Mindestens eine dieser beiden Eingaben muss verbunden sein, andernfalls gibt der Node die Validierungsmeldung „At least one of on_false or on_true must be connected to Switch node“ zurück. Da der Node lazy ist, gibt er, wenn nur eine Eingabe verbunden ist, immer den Wert dieser Eingabe aus, unabhängig vom Zustand von `switch`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Der ausgewählte Wert. Er entspricht dem Datentyp der verbundenen Eingabe `on_false` oder `on_true`. Wenn beide Eingaben verbunden sind, gibt er `on_true` aus, wenn `switch` wahr ist, und `on_false`, wenn `switch` falsch ist. | MATCH_TYPE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/de.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
