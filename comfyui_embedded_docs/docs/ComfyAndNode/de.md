# ComfyAndNode

Der And-Node führt eine logische UND-Operation auf einer Gruppe von Eingabewerten aus. Er gibt nur dann `true` zurück, wenn jeder verbundene Wert gemäß den Truthiness-Regeln von Python als wahr gilt. Dadurch eignet er sich, um zu prüfen, ob mehrere Bedingungen gleichzeitig erfüllt sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `values` | Eine erweiterbare Gruppe von Werten, die ausgewertet werden sollen. Der Node beginnt mit einem Slot, und Sie können weitere hinzufügen, indem Sie auf die Schaltfläche „+“ am Node klicken. Akzeptiert jeden Datentyp. | ANY | Ja | Mindestens 1 (kein Maximum) |

**Hinweis:** Diese Eingabe ist eine erweiterbare Slot-Gruppe. Slots werden einzeln hinzugefügt (zum Beispiel `value_1`, `value_2` usw.), und mindestens ein Slot muss vorhanden sein.

**Hinweis:** Der Node verwendet die Truthiness-Regeln von Python, um zu entscheiden, ob ein Wert `true` oder `false` ist. Zum Beispiel werden eine leere Zeichenkette, die Zahl 0, eine leere Liste und `None` alle als `false` behandelt. Alle anderen Werte werden als `true` behandelt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `BOOLEAN` | Gibt `true` zurück, wenn alle Eingabewerte als wahr gelten, andernfalls wird `false` zurückgegeben. | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/de.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
