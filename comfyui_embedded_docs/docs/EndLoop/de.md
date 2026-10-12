# Schleife beenden

End Loop markiert das Ende eines Schleifenblocks. Er sammelt den Wert, der vom letzten Node im Schleifenkörper erzeugt wird, und gibt entweder nur die letzte Iteration oder jede Iteration zurück, abhängig von der Einstellung `accumulate`, während er außerdem einen Wert zurück an Start Loop übergibt, damit die nächste Iteration beginnen kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `output_value` | Von End Loop zurückgegebener Wert. Gibt je nach `accumulate` die letzte Iteration oder alle Iterationen zurück. | ANY | Nein | Beliebiger Wertetyp |
| `next_iteration_value` | Wert, der von End Loop für die nächste Iteration an Start Loop zurückgegeben wird. | ANY | Nein | Beliebiger Wertetyp |
| `accumulate` | Gibt bei Aktivierung `output_value` aus jeder Iteration zurück; andernfalls wird nur die letzte Iteration zurückgegeben. | BOOLEAN | Nein | `true`<br>`false` (Standard: `false`) |
| `terminations` | Verbinden Sie Ausgaben, die bei jeder Iteration ausgeführt werden müssen. Ihre Werte werden nicht zurückgegeben. Erweiterbare Slots mit den Namen `termination_1`, `termination_2` usw. | ANY | Nein | 0 bis 50 Slots |

Hinweis: `terminations` ist eine erweiterbare Liste von Slots mit einem Minimum von 0 und einem Maximum von 50 Verbindungen. Hier verbundene Werte erzwingen die Ausführung bei jeder Iteration, sind aber nicht Teil des zurückgegebenen Ergebnisses.

Hinweis: Dieser Node ist ein Eingabelisten-Node, daher empfangen seine Eingaben die gesammelten Werte aus jeder Schleifeniteration.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `outputs` | Der `output_value` der letzten Iteration oder die über Iterationen angesammelten Werte, wenn `accumulate` aktiviert ist. | ANY (list) |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/de.md)

---
**Source fingerprint (SHA-256):** `142840dca7f238eb00c72074d265478c548ad5c047e05744d0c3715e452f795a`
