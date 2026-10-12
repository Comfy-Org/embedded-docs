# ImageScale

Der ImageScale-Node dient der Größenänderung von Bildern auf bestimmte Abmessungen. Er bietet eine Auswahl an Upscale-Methoden und die Möglichkeit, das skalierte Bild zuzuschneiden. Er abstrahiert die Komplexität von Bild-Upscaling und Zuschneiden und stellt eine unkomplizierte Schnittstelle bereit, um Bildabmessungen gemäß benutzerdefinierter Parameter zu ändern.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das Eingabebild, das hochskaliert werden soll. Dieser Parameter ist zentral für die Funktionsweise des Nodes und dient als primäre Datenquelle, auf die die Größenänderungstransformationen angewendet werden. Die Qualität und die Abmessungen des Ausgabebilds werden direkt von den Eigenschaften des Originalbilds beeinflusst. | `IMAGE` |
| `upscale_method` | Gibt die Methode an, die zum Hochskalieren des Bildes verwendet wird. Die Wahl der Methode kann die Qualität und die Eigenschaften des hochskalierten Bildes beeinflussen, was sich auf die visuelle Wiedergabetreue und mögliche Artefakte in der größenveränderten Ausgabe auswirkt. | COMBO[STRING] |
| `width` | Die Zielbreite für das hochskalierte Bild. Dieser Parameter beeinflusst direkt die Abmessungen des Ausgabebilds und bestimmt den horizontalen Maßstab der Größenänderung. | `INT` |
| `height` | Die Zielhöhe für das hochskalierte Bild. Dieser Parameter beeinflusst direkt die Abmessungen des Ausgabebilds und bestimmt den vertikalen Maßstab der Größenänderung. | `INT` |
| `crop` | Legt fest, ob und wie das hochskalierte Bild zugeschnitten werden soll, mit Optionen für deaktiviertes Zuschneiden oder mittiges Zuschneiden. Dies beeinflusst die endgültige Bildkomposition, indem möglicherweise Ränder entfernt werden, um die angegebenen Abmessungen einzuhalten. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das hochskalierte (und optional zugeschnittene) Bild, bereit für die weitere Verarbeitung oder Visualisierung. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/de.md)
