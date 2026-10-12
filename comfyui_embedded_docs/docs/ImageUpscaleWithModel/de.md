# ImageUpscaleWithModel

Dieser Node ist für das Hochskalieren von Bildern unter Verwendung eines angegebenen Upscale-Modells konzipiert. Er verwaltet den Upscaling-Prozess effizient, indem er das Bild an das geeignete Gerät anpasst, die Speichernutzung optimiert und das Upscale-Modell in gekachelter Weise anwendet, um potenzielle Fehler aufgrund von Speichermangel zu vermeiden.

## Eingaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `upscale_model` | Das Upscale-Modell, das zum Hochskalieren des Bildes verwendet werden soll. Es ist entscheidend für die Definition des Hochskalierungsalgorithmus und seiner Parameter. | `UPSCALE_MODEL` |
| `image` | Das Bild, das hochskaliert werden soll. Diese Eingabe ist wesentlich für die Bestimmung des Quellinhalts, der dem Hochskalierungsprozess unterzogen wird. | `IMAGE` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das hochskalierte Bild, das vom Upscale-Modell verarbeitet wurde. Diese Ausgabe ist das Ergebnis der Hochskalierungsoperation und zeigt die verbesserte Auflösung oder Qualität. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/de.md)
