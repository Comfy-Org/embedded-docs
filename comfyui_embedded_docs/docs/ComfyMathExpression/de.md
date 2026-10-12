# Mathematischer Ausdruck

Der Node `ComfyMathExpression` wertet eine mathematische Formel aus, die Sie als Text schreiben. Die Formel kann auf die Eingabewerte des Nodes über Buchstabennamen wie `a`, `b`, `c` verweisen, und Sie können über die erweiterbare Gruppe `values` beliebig viele Eingabewerte hinzufügen. Das Berechnungsergebnis wird gleichzeitig als Gleitkommazahl, Ganzzahl und boolescher Wert zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `expression` | Die mathematische Formel, die ausgewertet werden soll, geschrieben als Text (zum Beispiel `a + b`), wobei die Buchstabennamen der Eingabewerte als Variablen verwendet werden. Mehrzeilige Eingabe. (Standard: `a + b`) | STRING | Ja | N/A |
| `values` | Erweiterbare Gruppe von Eingabewerten, die die Variablen für den Ausdruck bereitstellt. Jeder Wert, der der Gruppe hinzugefügt wird, erhält automatisch den nächsten kleingeschriebenen Buchstabennamen beginnend bei `a` (`a`, `b`, `c`, ...), und dieser Name kann dann innerhalb von `expression` verwendet werden. Jedes Element akzeptiert eine Zahl (INT oder FLOAT) oder einen booleschen Wert (TRUE/FALSE). | FLOAT, INT, BOOLEAN | Ja | 1 bis 26 Werte, benannt `a` bis `z` |

### Hinweise und Einschränkungen

- `expression` darf nicht leer sein oder nur Leerzeichen enthalten.
- Der Ausdruck muss zu einem numerischen Ergebnis (INT oder FLOAT) oder einem booleschen Ergebnis (TRUE/FALSE) ausgewertet werden. Boolesche Ergebnisse werden als 1 für TRUE und 0 für FALSE behandelt. Wenn das Ergebnis einen anderen Typ hat, beispielsweise Text, löst der Node einen Fehler aus.
- Das numerische Ergebnis muss endlich und in einen Float konvertierbar sein. Ergebnisse, die zu groß oder nicht endlich sind, verursachen einen Fehler.
- Die gesamte Menge der Eingabewerte ist innerhalb des Ausdrucks auch unter dem Variablennamen `values` (als Liste) verfügbar, sodass Ausdrücke wie `sum(values)` möglich sind.
- Die folgenden mathematischen Funktionen sind innerhalb des Ausdrucks verfügbar: `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `FLOAT` | Das Ergebnis des Ausdrucks als Gleitkommazahl. | FLOAT |
| `INT` | Das Ergebnis des Ausdrucks als Ganzzahl konvertiert, wobei der Dezimalteil abgeschnitten wird. | INT |
| `BOOL` | Das Ergebnis als boolescher Wert konvertiert: TRUE, wenn das numerische Ergebnis nicht null ist, FALSE, wenn es null ist. | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/de.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
