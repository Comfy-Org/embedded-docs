# Bildvorschau

Der PreviewImage-Node ist für die Erstellung temporärer Vorschaubilder konzipiert. Er generiert automatisch einen eindeutigen temporären Dateinamen für jedes Bild, komprimiert das Bild auf einen angegebenen Grad und speichert es in einem temporären Verzeichnis. Diese Funktionalität ist besonders nützlich, um während der Verarbeitung Vorschaubilder von Bildern zu erzeugen, ohne die Originaldateien zu beeinflussen.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Die Eingabe `images` gibt die Bilder an, die verarbeitet und als temporäre Vorschaubilder gespeichert werden sollen. Dies ist die primäre Eingabe für den Node und bestimmt, welche Bilder den Prozess der Vorschaubilderzeugung durchlaufen. | `IMAGE` |

## Ausgaben

Der Node hat keine Ausgabetypen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewImage/de.md)
