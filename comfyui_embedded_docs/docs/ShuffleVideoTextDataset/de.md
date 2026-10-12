# ShuffleVideoTextDataset

Dieser Node mischt die Reihenfolge von Paaren aus Video und Text in einer Liste zufällig, wobei jedes Video mit seinem zugehörigen Text gepaart bleibt. Er nimmt zwei Listen gleicher Länge und wendet dieselbe zufällige Permutation auf beide an, sodass die ursprünglichen Paarungen nach dem Mischen erhalten bleiben. Ein Seed-Wert steuert die Mischreihenfolge, sodass Ergebnisse reproduziert werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `videos` | Liste der zu mischenden Videos. | VIDEO | Ja | Liste von Videoelementen |
| `texts` | Liste der zu mischenden Texte (die den Videos zugeordneten Beschriftungen). | STRING | Ja | Liste von Textzeichenfolgen |
| `seed` | Zufälliger Seed, der die Mischreihenfolge bestimmt (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |

Hinweis: `videos` und `texts` müssen dieselbe Länge haben, da der Node jedes Video mit dem Text an derselben Position paart und diese Paarungen beim Mischen beibehält. Intern wird der `seed`-Wert vor der Generierung der zufälligen Reihenfolge mithilfe von Modulo 4294967295 (2^32 - 1) reduziert, sodass sehr große Seed-Werte dieselbe Mischung wie kleinere erzeugen können.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `videos` | Gemischte Videos in der neuen zufälligen Reihenfolge. | VIDEO |
| `texts` | Gemischte Texte in derselben neuen Reihenfolge wie die Videos. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/de.md)

---
**Source fingerprint (SHA-256):** `834305718cd53a86211363750e887ffccdb54bc3b628dc17f049e546c234f9cb`
