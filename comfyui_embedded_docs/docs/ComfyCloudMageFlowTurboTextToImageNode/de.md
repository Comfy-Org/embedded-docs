# ComfyCloudMageFlowTurboTextToImageNode

Dieser Comfy-Cloud-Node erzeugt ein Bild aus einem Text-Prompt unter Verwendung des Mage-Flow-Turbo-Workflows (`mage-flow-turbo/text-to-image`). Er führt eine destillierte Version des Mage-Flow-Modells aus, die das Bild in 4 Schritten bei einem cfg-Wert von 1 erzeugt und etwa ein Siebtel der GPU-Zeit eines vollständigen Mage-Flow-Durchlaufs benötigt, was ihn zur Variante für schnelle Iterationen macht.

## Eingaben

Die Node-Klasse selbst deklariert in der verfügbaren Quelle keine Eingabe-Widgets; ihr Eingabeschema wird von der gemeinsamen Basisklasse `_ComfyCloudMageFlowNode` geerbt, deren Definition nicht im Quell-Snapshot enthalten ist. Ausgehend von der Node-Zusammenfassung und dem Namen des Text-zu-Bild-Workflows erwartet der Node einen Text-Prompt, der das zu erzeugende Bild beschreibt.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Der Text-Prompt, der das zu erzeugende Bild beschreibt. Der genaue Parametername wird durch das geerbte Basisschema `_ComfyCloudMageFlowNode` festgelegt und kann von dieser Bezeichnung abweichen. | STRING | Ja | Freitext |

Hinweis: In der geerbten Basis-Node-Definition, die in der bereitgestellten Quelle nicht verfügbar ist, können zusätzliche Eingabeparameter vorhanden sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Das aus dem Text-Prompt erzeugte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/de.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`
