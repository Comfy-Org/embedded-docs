# Text aus JSON extrahieren

Der Node JsonExtractString durchsucht eine Textzeichenkette nach dem ersten gültigen JSON-Objekt und extrahiert den Wert, der einem bestimmten Schlüssel zugeordnet ist, als Zeichenkette. Beliebiger Text vor oder nach dem JSON-Objekt wird ignoriert, sodass der Node auch mit Markdown-Codeblöcken und Modellantworten funktioniert, die das JSON in zusätzlichen Fließtext einbetten. Wenn kein gültiges JSON-Objekt gefunden wird, der Schlüssel nicht gefunden wird oder der Wert null ist, gibt der Node eine leere Zeichenkette zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `json_string` | Der Text, in dem nach einem JSON-Objekt gesucht wird. Dieses Feld unterstützt mehrzeilige Eingaben und kann umgebenden Fließtext oder Markdown-Codezäune enthalten. | STRING | Ja | N/A |
| `key` | Der bestimmte Schlüssel, dessen Wert aus dem JSON-Objekt extrahiert werden soll. Dieses Feld unterstützt nur einzeilige Eingaben. | STRING | Ja | N/A |

**Hinweis:** Der Node extrahiert Werte nur aus JSON-Objekten (Dictionaries). Er probiert jedes `{` in der Eingabe der Reihe nach aus und dekodiert ab der ersten Position, die ein gültiges JSON-Objekt ergibt, sodass vorangestellter oder nachfolgender Text übersprungen wird. Wenn kein JSON-Objekt dekodiert werden kann oder der angegebene Schlüssel darin nicht existiert, ist die Ausgabe eine leere Zeichenkette. Wenn der dem Schlüssel zugeordnete Wert `null` ist, gibt der Node ebenfalls eine leere Zeichenkette zurück. Werte, die keine Zeichenketten sind, werden als ihre Zeichenkettendarstellung zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Der aus dem JSON für den angegebenen Schlüssel extrahierte Zeichenkettenwert oder eine leere Zeichenkette, wenn die Extraktion fehlschlägt. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/de.md)

---
**Source fingerprint (SHA-256):** `ca697fd3bd2d4de764372470ad1102b345d9d60f6df1c151fa0573e85fab2382`
