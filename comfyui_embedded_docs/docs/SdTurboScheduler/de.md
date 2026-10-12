# SdTurboScheduler

SDTurboScheduler dient dazu, eine Sequenz von Sigma-Werten für das Bild-Sampling zu erzeugen und die Sequenz abhängig vom Denoise-Level und der angegebenen Anzahl von Schritten anzupassen. Er nutzt die Sampling-Fähigkeiten eines bestimmten Modells, um diese Sigma-Werte zu erzeugen, die entscheidend für die Steuerung des Denoising-Prozesses während der Bilderzeugung sind.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Der Parameter `model` gibt das generative Modell an, das zur Erzeugung der Sigma-Werte verwendet werden soll. Er ist entscheidend für das spezifische Sampling-Verhalten und die Fähigkeiten des Schedulers. | `MODEL` |
| `steps` | Der Parameter `steps` bestimmt die Länge der zu erzeugenden Sigma-Sequenz und beeinflusst direkt die Granularität des Denoising-Prozesses. | `INT` |
| `denoise` | Der Parameter `denoise` passt den Startpunkt der Sigma-Sequenz an und ermöglicht eine feinere Steuerung des Denoising-Levels, das während der Bilderzeugung angewendet wird. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Eine Sequenz von Sigma-Werten, die basierend auf dem angegebenen Modell, den Schritten und dem Denoise-Level erzeugt wird. Diese Werte sind wesentlich für die Steuerung des Denoising-Prozesses bei der Bilderzeugung. | `SIGMAS` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SdTurboScheduler/de.md)
