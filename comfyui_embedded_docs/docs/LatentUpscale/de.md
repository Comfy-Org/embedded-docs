# LatentUpscale

Der LatentUpscale-Node ist für die Hochskalierung latenter Repräsentationen von Bildern konzipiert. Er ermöglicht die Anpassung der Abmessungen des Ausgabebilds und der Methode zur Hochskalierung, was Flexibilität bei der Verbesserung der Auflösung latenter Bilder bietet.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Die latente Repräsentation eines Bildes, das hochskaliert werden soll. Dieser Parameter ist entscheidend, um den Ausgangspunkt des Hochskalierungsprozesses zu bestimmen. | `LATENT` |
| `upscale_method` | Gibt die Methode an, die für die Hochskalierung des latenten Bildes verwendet wird. Unterschiedliche Methoden können die Qualität und Eigenschaften des hochskalierten Bildes beeinflussen. | COMBO[STRING] |
| `width` | Die gewünschte Breite des hochskalierten Bildes. Wenn auf 0 gesetzt, wird sie basierend auf der Höhe berechnet, um das Seitenverhältnis beizubehalten. | `INT` |
| `height` | Die gewünschte Höhe des hochskalierten Bildes. Wenn auf 0 gesetzt, wird sie basierend auf der Breite berechnet, um das Seitenverhältnis beizubehalten. | `INT` |
| `crop` | Bestimmt, wie das hochskalierte Bild zugeschnitten werden soll, was das endgültige Erscheinungsbild und die Abmessungen der Ausgabe beeinflusst. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die hochskalierte latente Repräsentation des Bildes, bereit für die weitere Verarbeitung oder Generierung. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/de.md)
