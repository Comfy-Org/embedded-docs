# LoadImageSetFromFolderNode

Der LoadImageSetFromFolderNode lädt mehrere Bilder aus einem angegebenen Ordnerverzeichnis für Trainingszwecke. Er erkennt automatisch gängige Bildformate und kann die Bilder optional mit verschiedenen Methoden skalieren, bevor er sie als Batch zurückgibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `folder` | Der Ordner, aus dem Bilder geladen werden. | STRING | Ja | Mehrere Optionen verfügbar |
| `resize_method` | Die Methode zum Ändern der Bildgröße (Standard: "None"). | STRING | Nein | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Der Batch der geladenen Bilder als einzelner Tensor. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/de.md)

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
