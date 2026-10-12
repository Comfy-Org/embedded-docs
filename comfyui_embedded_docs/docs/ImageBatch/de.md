# Bilder stapeln (VERALTET)

Der Node `ImageBatch` ist darauf ausgelegt, zwei Bilder zu einem einzigen Batch zusammenzufassen. Wenn die Abmessungen der Bilder nicht übereinstimmen, skaliert er das zweite Bild automatisch auf die Abmessungen des ersten Bildes, bevor er sie zusammenfügt.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image1` | Das erste Bild, das in den Batch aufgenommen werden soll. Es dient als Referenz für die Abmessungen, an die das zweite Bild bei Bedarf angepasst wird. | `IMAGE` |
| `image2` | Das zweite Bild, das in den Batch aufgenommen werden soll. Es wird automatisch auf die Abmessungen des ersten Bildes skaliert, falls diese abweichen. | `IMAGE` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der kombinierte Batch aus Bildern, wobei das zweite Bild bei Bedarf auf die Abmessungen des ersten Bildes skaliert wurde. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/de.md)
