# SetFirstSigma

Der SetFirstSigma-Node ändert eine Sigma-Sequenz, indem nur ihr erster Wert durch einen benutzerdefinierten Sigma-Wert ersetzt wird. Er nimmt eine vorhandene Sigma-Sequenz und einen neuen Sigma-Wert entgegen und gibt eine neue Sigma-Sequenz zurück, in der alle Werte außer dem ersten unverändert bleiben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `sigmas` | Die Eingabesequenz der zu ändernden Sigma-Werte | SIGMAS | Ja | - |
| `sigma` | Der neue Sigma-Wert, der als erstes Element in der Sequenz festgelegt werden soll (Standard: 136.0) | FLOAT | Ja | 0.0 to 20000.0 (step: 0.001) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Die geänderte Sigma-Sequenz, bei der das erste Element durch den benutzerdefinierten Sigma-Wert ersetzt wurde | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/de.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
