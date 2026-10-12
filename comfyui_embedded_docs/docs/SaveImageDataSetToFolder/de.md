# SaveImageDataSetToFolder

Dieser Node speichert eine Liste von Bildern in einem angegebenen Ordner innerhalb des Ausgabeverzeichnisses von ComfyUI. Er schreibt jedes Bild als PNG-Datei auf die Festplatte und verwendet dabei ein konfigurierbares Dateinamenpräfix. Dieser Node ist veraltet und wird durch vorhandene Save-Image-Nodes ersetzt, bei denen der Zielordner im Dateinamenpräfix angegeben werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Wertebereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Liste der zu speichernden Bilder. | IMAGE | Ja | N/A |
| `folder_name` | Name des Ordners, in dem die Bilder gespeichert werden sollen (innerhalb des Ausgabeverzeichnisses). Standard: "dataset". | STRING | Nein | N/A |
| `filename_prefix` | Präfix für die Dateinamen der gespeicherten Bilder. Standard: "image". Erweiterter Parameter. | STRING | Nein | N/A |
| `mode` | Ob vorhandene Dateien überschrieben oder Dateinamen hochgezählt werden sollen, um ein Überschreiben zu vermeiden. Standard: "overwrite". | COMBO | Nein | "overwrite"<br>"increment" |

**Hinweise:**

- Die Eingabe `images` ist eine Liste, daher können mehrere Bilder in einem einzigen Durchlauf gespeichert werden.
- Die Parameter `folder_name`, `filename_prefix` und `mode` sind Skalarwerte; wenn eine Liste verbunden wird, wird nur der erste Wert aus dieser Liste verwendet.
- Der `folder_name` muss zu einem Ort innerhalb des Ausgabeverzeichnisses von ComfyUI aufgelöst werden. Werte, die aus dem Ausgabeverzeichnis herausführen (zum Beispiel Pfade, die `..` enthalten, oder absolute Pfade, Laufwerksbuchstaben oder Symlink-Ausbrüche), werden mit einem Fehler abgelehnt.
- Im Modus "overwrite" werden Dateien als `{prefix}_00000.png`, `{prefix}_00001.png` usw. gespeichert, wobei vorhandene Dateien ersetzt werden. Im Modus "increment" wird ein Zähler in den Dateinamen eingefügt, sodass vorhandene Dateien nicht überschrieben werden.
- Es wird nur die Ausgabe als PNG unterstützt.

## Ausgaben

Dieser Node hat keine Ausgaben. Er ist ein Ausgabe-Node, der einen Speichervorgang auf dem Dateisystem ausführt.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/de.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
