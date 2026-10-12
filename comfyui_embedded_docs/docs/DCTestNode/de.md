# DCTestNode

DCTestNode ist ein Logik-Node, der abhängig von der Auswahl des Benutzers in einer dynamischen Combo-Auswahl verschiedene Datentypen zurückgibt. Er fungiert als bedingter Router, bei dem die gewählte Option bestimmt, welches Eingabefeld aktiv ist und welchen Werttyp der Node ausgibt. Der Node ist in ComfyUI als Ausgabe-Node gekennzeichnet.

## Eingaben

Der Node verwendet eine dynamische Combo-Auswahl: Der Parameter `combo` ist immer sichtbar, und die anderen Eingabefelder erscheinen nur, wenn die zugehörige Option ausgewählt ist.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `combo` | Die Hauptauswahl, die bestimmt, welches Eingabefeld aktiv ist und was der Node ausgibt. | DYNAMIC_COMBO | Ja | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### option1 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Ein Texteingabefeld. Dieses Feld ist nur aktiv und erforderlich, wenn `combo` auf `"option1"` gesetzt ist. | STRING | Ja | - |

### option2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `integer` | Ein Ganzzahleingabefeld. Dieses Feld ist nur aktiv und erforderlich, wenn `combo` auf `"option2"` gesetzt ist. | INT | Ja | - |

### option3 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Ein Bildeingabefeld. Dieses Feld ist nur aktiv und erforderlich, wenn `combo` auf `"option3"` gesetzt ist. | IMAGE | Ja | - |

### option4 Eingaben

Wenn `combo` auf `"option4"` gesetzt ist, zeigt der Node eine zweite dynamische Combo-Auswahl (`subcombo`) an, die eine verschachtelte Gruppe von Eingabefeldern steuert.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `subcombo` | Eine sekundäre dynamische Combo-Auswahl, die erscheint, wenn `combo` auf `"option4"` gesetzt ist. Sie bestimmt, welche verschachtelten Eingabefelder aktiv sind. | DYNAMIC_COMBO | Ja | `"opt1"`<br>`"opt2"` |
| `float_x` | Eine Dezimalzahleingabe. Dieses Feld ist nur aktiv und erforderlich, wenn `combo` auf `"option4"` und `subcombo` auf `"opt1"` gesetzt ist. | FLOAT | Ja | - |
| `float_y` | Eine Dezimalzahleingabe. Dieses Feld ist nur aktiv und erforderlich, wenn `combo` auf `"option4"` und `subcombo` auf `"opt1"` gesetzt ist. | FLOAT | Ja | - |
| `mask1` | Ein Maskeneingabefeld. Dieses Feld ist nur aktiv, wenn `combo` auf `"option4"` und `subcombo` auf `"opt2"` gesetzt ist. Es ist optional. | MASK | Nein | - |

**Parametereinschränkungen:**

* Der Parameter `combo` steuert die Sichtbarkeit und Erforderlichkeit aller anderen Eingabefelder. Nur die Eingaben, die der ausgewählten `combo`-Option zugeordnet sind, werden angezeigt und sind erforderlich (außer `mask1`, das optional ist).
* Wenn `combo` auf `"option4"` gesetzt ist, wird der Parameter `subcombo` erforderlich und steuert eine zweite Gruppe verschachtelter Eingaben (`float_x`/`float_y` oder `mask1`).
* Wenn `combo` einen Wert erhält, der nicht zu den vier aufgeführten Optionen gehört, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die Ausgabe hängt von der ausgewählten `combo`-Option ab. Sie kann ein STRING (`"option1"`), ein INT (`"option2"`), ein IMAGE (`"option3"`) oder eine String-Darstellung des `subcombo`-Werts (`"option4"`) sein. | ANYTYPE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/de.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
