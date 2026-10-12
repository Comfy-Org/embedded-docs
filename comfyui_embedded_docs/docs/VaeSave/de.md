# VaeSave

Der VAESave-Node dient zum Speichern von VAE-Modellen zusammen mit ihren Metadaten, einschließlich Prompts und zusätzlicher PNG-Informationen, in einem angegebenen Ausgabeverzeichnis. Er kapselt die Funktionalität, den Modellzustand und zugehörige Informationen in einer Datei zu serialisieren, was die Bewahrung und Weitergabe trainierter Modelle erleichtert.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `vae` | Das zu speichernde VAE-Modell. Dieser Parameter ist entscheidend, da er das Modell repräsentiert, dessen Zustand serialisiert und gespeichert werden soll. | VAE |
| `filename_prefix` | Ein Präfix für den Dateinamen, unter dem das Modell und seine Metadaten gespeichert werden. Dies ermöglicht eine organisierte Speicherung und ein einfaches Auffinden von Modellen. | STRING |

## Ausgaben

Der Node hat keine Ausgabetypen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeSave/de.md)
