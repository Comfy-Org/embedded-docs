# Oder

Der Or-Node führt eine logische ODER-Operation für eine Gruppe von Eingabewerten aus. Er gibt `true` zurück, wenn mindestens einer der bereitgestellten Werte gemäß den standardmäßigen Truthiness-Regeln von Python als truthy gilt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `values` | Eine erweiterbare Sammlung von Werten, die auf ihren Truthiness-Wert geprüft werden. Jeder hinzugefügte Eingabe-Slot heißt `value_1`, `value_2` und so weiter. Der Node gibt `true` zurück, wenn mindestens einer dieser Werte truthy ist. | ANY | Ja | 1 oder mehr Werte |

**Hinweis:** Der Node akzeptiert mindestens 1 Eingabewert. Sie können nach Bedarf mithilfe der Autogrow-Funktion weitere Eingaben hinzufügen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `BOOLEAN` | Gibt `true` zurück, wenn mindestens einer der Eingabewerte truthy ist; gibt `false` zurück, wenn alle Eingabewerte falsy sind. | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/de.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
