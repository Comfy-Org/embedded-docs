# StringSubstring

Der StringSubstring-Node extrahiert einen Teil eines Textes aus einer größeren Zeichenkette. Er verwendet eine Startposition und eine Endposition, um den Abschnitt zu definieren, den Sie extrahieren möchten, und gibt anschließend den Text zwischen diesen beiden Positionen zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Die Eingabezeichenkette, aus der extrahiert werden soll. Unterstützt mehrzeiligen Text. | STRING | Ja | - |
| `start` | Der Index der Startposition für den Teilstring. Das erste Zeichen befindet sich bei Index 0. | INT | Ja | - |
| `end` | Der Index der Endposition für den Teilstring. Das Zeichen an diesem Index wird nicht in das Ergebnis einbezogen. | INT | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Der extrahierte Teilstring aus dem Eingabetext, der alle Zeichen von der Position `start` bis ausschließlich Position `end` enthält. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/de.md)

---
**Source fingerprint (SHA-256):** `fd3ec23bbfe3a51f5481f1b0fe8b77f66e08469bb2a4bd3e266a7607f014e544`
