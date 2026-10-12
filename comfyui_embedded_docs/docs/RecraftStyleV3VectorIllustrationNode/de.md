# RecraftStyleV3VectorIllustrationNode

Dieser Node wählt einen Stil für die Recraft API aus, insbesondere die Stilkategorie Vektorillustration. Optional können Sie einen spezifischeren Unterstil innerhalb dieser Kategorie auswählen. Der Node gibt ein Stilkonfigurationsobjekt aus, das an andere Recraft-Nodes übergeben werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `substyle` | Ein spezifischerer Stil innerhalb der Kategorie Vektorillustration. Die verfügbaren Optionen sind die von der Recraft API für den Stil `vector_illustration` definierten Unterstile. Wenn kein Unterstil ausgewählt wird, wird der Basisstil `vector_illustration` verwendet. | COMBO | Ja | Mehrere Optionen verfügbar (dynamisch geladene Unterstil-Liste für den Stil `vector_illustration`) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `recraft_style` | Ein Recraft-Stilkonfigurationsobjekt, das den ausgewählten Vektorillustrationsstil und optionalen Unterstil enthält. Dieses kann mit anderen Recraft-Nodes verbunden werden. | STYLEV3 |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/de.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`
