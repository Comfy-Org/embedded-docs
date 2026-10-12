# ShuffleImageTextDataset

Dieser Node mischt eine Liste von Bildern und eine Liste von Texten gemeinsam, wobei deren Paarungen intakt bleiben. Er verwendet einen Zufalls-Seed, um die Mischreihenfolge zu bestimmen, sodass dieselben Eingabelisten bei erneuter Verwendung des Seeds jedes Mal auf dieselbe Weise gemischt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Liste der zu mischenden Bilder. | IMAGE | Ja | - |
| `texts` | Liste der zu mischenden Texte. | STRING | Ja | - |
| `seed` | Zufalls-Seed. Die Mischreihenfolge wird durch diesen Wert bestimmt (Standard: 0). | INT | Nein | 0 bis 18446744073709551615 |

**Hinweis:** Die Eingaben `images` und `texts` müssen Listen derselben Länge sein. Der Node paart das erste Bild mit dem ersten Text, das zweite Bild mit dem zweiten Text und so weiter, bevor diese Paare gemeinsam gemischt werden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Die gemischte Liste der Bilder. | IMAGE |
| `texts` | Die gemischte Liste der Texte, wobei ihre ursprünglichen Paarungen mit den Bildern erhalten bleiben. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/de.md)

---
**Source fingerprint (SHA-256):** `77050e9f7255e64b07bd394908b679acef399d78ec9be7c1346d6f297c109968`
