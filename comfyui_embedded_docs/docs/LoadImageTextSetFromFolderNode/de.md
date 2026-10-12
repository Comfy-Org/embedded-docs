# LoadImageTextSetFromFolderNode

Lädt einen Batch von Bildern und die zugehörigen Textbeschriftungen aus einem angegebenen Verzeichnis für Trainingszwecke. Der Node sucht automatisch nach Bilddateien und den dazugehörigen Beschriftungs-Textdateien, verarbeitet die Bilder gemäß den angegebenen Größenänderungseinstellungen und kodiert die Beschriftungen mit dem bereitgestellten CLIP-Modell.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `folder` | Der Ordner, aus dem die Bilder geladen werden. | STRING | Ja | - |
| `clip` | Das CLIP-Modell, das zum Kodieren des Textes verwendet wird. | CLIP | Ja | - |
| `resize_method` | Die Methode zum Ändern der Bildgröße (Standard: "None"). | COMBO | Nein | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |
| `width` | Die Breite, auf die die Bilder skaliert werden. -1 bedeutet, die ursprüngliche Breite zu verwenden (Standard: -1). | INT | Nein | -1 to 10000 |
| `height` | Die Höhe, auf die die Bilder skaliert werden. -1 bedeutet, die ursprüngliche Höhe zu verwenden (Standard: -1). | INT | Nein | -1 to 10000 |

**Hinweis:** Die CLIP-Eingabe muss gültig sein und darf nicht None sein. Wenn das CLIP-Modell von einem Checkpoint-Loader-Node stammt, stellen Sie sicher, dass der Checkpoint ein gültiges CLIP- oder Textencoder-Modell enthält.

**Hinweis zur Ordnerstruktur:** Der Node unterstützt die Ordnerstruktur von kohya-ss/sd-scripts. Wenn der Name eines Unterordners mit einer Zahl gefolgt von einem Unterstrich beginnt (z. B. `5_myclass`), wird diese Zahl als Wiederholungsanzahl verwendet, und die Bilder in diesem Unterordner werden entsprechend oft geladen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Der Batch der geladenen und verarbeiteten Bilder. | IMAGE |
| `CONDITIONING` | Die kodierten Conditioning-Daten aus den Textbeschriftungen. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/de.md)

---
**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`
