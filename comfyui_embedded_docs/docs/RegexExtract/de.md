# Text extrahieren

Der RegexExtract-Node sucht mithilfe regulärer Ausdrücke nach Mustern in Text. Er kann den ersten Treffer, alle Treffer, bestimmte Gruppen aus Treffern oder alle Gruppen über mehrere Treffer hinweg finden. Der Node unterstützt verschiedene Regex-Flags für Groß-/Kleinschreibung, mehrzeiliges Matching und Dotall-Verhalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Der Eingabetext, in dem nach Mustern gesucht wird | STRING | Ja | - |
| `regex_pattern` | Das reguläre Ausdrucksmuster, nach dem gesucht wird | STRING | Ja | - |
| `mode` | Der Extraktionsmodus bestimmt, welche Teile von Treffern zurückgegeben werden (Standard: "First Match") | COMBO | Ja | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" |
| `case_insensitive` | Ob die Groß-/Kleinschreibung beim Abgleichen ignoriert werden soll (Standard: True) | BOOLEAN | Nein | - |
| `multiline` | Ob die Zeichenkette als mehrere Zeilen behandelt werden soll (Standard: False) | BOOLEAN | Nein | - |
| `dotall` | Ob der Punkt (.) mit Zeilenumbrüchen übereinstimmt (Standard: False) | BOOLEAN | Nein | - |
| `group_index` | Der Index der Capture-Gruppe, die bei Verwendung der Gruppenmodi extrahiert werden soll (Standard: 1) | INT | Nein | 0-100 |

**Hinweis:** Bei Verwendung der Modi "First Group" oder "All Groups" gibt der Parameter `group_index` an, welche Capture-Gruppe extrahiert werden soll. Gruppe 0 repräsentiert den gesamten Treffer, während Gruppen 1+ die nummerierten Capture-Gruppen in Ihrem Regex-Muster repräsentieren.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Der extrahierte Text basierend auf dem ausgewählten Modus und den Parametern | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/de.md)

---
**Source fingerprint (SHA-256):** `a879e4fd7429edfada44b2f5778bb71e537a000be6c25d3f67359b9ee802812f`
