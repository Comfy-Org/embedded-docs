# AutogrowPrefixTestNode

Der AutogrowPrefixTestNode ist ein Logik-Node, der die Autogrow-Eingabefunktion testet. Er akzeptiert eine dynamische Anzahl von Float-Eingaben, wandelt jeden Wert in Text um, kombiniert sie zu einer kommagetrennten Zeichenkette und gibt diese Zeichenkette aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `autogrow` | Eine dynamische Eingabegruppe, die zwischen 1 und 10 Float-Werten akzeptiert. Jeder Wert ist eine Gleitkommazahl, und die generierten Eingaben werden mit dem Präfix `float` benannt. | AUTOGROW | Ja | 1 bis 10 Eingaben |

**Hinweis:** Die Eingabe `autogrow` ist eine spezielle dynamische Eingabe. Sie können dieser Gruppe mehrere Float-Eingaben hinzufügen, von mindestens 1 bis maximal 10. Der Node verarbeitet alle angegebenen Werte und bezieht jede verbundene Eingabe in die Ausgabezeichenkette ein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Eine einzelne Zeichenkette, die alle eingegebenen Float-Werte enthält, getrennt durch Kommas. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/de.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
