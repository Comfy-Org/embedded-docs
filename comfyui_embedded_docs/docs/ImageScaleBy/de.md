# Bild um Faktor hochskalieren

Der Node ImageScaleBy dient zum Hochskalieren von Bildern um einen angegebenen Skalierungsfaktor unter Verwendung verschiedener Interpolationsmethoden. Er ermöglicht eine flexible Anpassung der Bildgröße und deckt unterschiedliche Anforderungen beim Hochskalieren ab.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das Eingabebild, das hochskaliert werden soll. Dieser Parameter ist entscheidend, da er das Basisbild bereitstellt, das dem Hochskalierungsprozess unterzogen wird. | `IMAGE` |
| `upscale_method` | Gibt die Interpolationsmethode an, die für das Hochskalieren verwendet werden soll. Die Wahl der Methode kann die Qualität und die Eigenschaften des hochskalierten Bildes beeinflussen. | COMBO[STRING] |
| `scale_by` | Der Faktor, um den das Bild hochskaliert wird. Dies bestimmt die Größenänderung des Ausgabebilds im Verhältnis zum Eingabebild. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das hochskalierte Bild, das gemäß dem angegebenen Skalierungsfaktor und der Interpolationsmethode größer als das Eingabebild ist. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/de.md)
