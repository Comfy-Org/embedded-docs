# GligenTextBoxApply

Der Node `GLIGENTextBoxApply` ist darauf ausgelegt, textbasierte Konditionierung in die Eingabe eines generativen Modells zu integrieren, insbesondere durch Anwenden von Textfeldparametern und deren Kodierung mithilfe eines CLIP-Modells. Dieser Prozess reichert die Konditionierung mit räumlichen und textuellen Informationen an und ermöglicht eine präzisere und kontextbewusste Generierung.

## Eingaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning_to` | Gibt die anfängliche Konditionierungseingabe an, an die die Textfeldparameter und die kodierte Textinformation angehängt werden. Sie spielt eine entscheidende Rolle bei der Bestimmung der endgültigen Ausgabe, indem sie neue Konditionierungsdaten integriert. | `CONDITIONING` |
| `clip` | Das CLIP-Modell, das zum Kodieren des bereitgestellten Textes in ein Format verwendet wird, das vom generativen Modell genutzt werden kann. Es ist wesentlich, um textuelle Informationen in ein kompatibles Konditionierungsformat umzuwandeln. | `CLIP` |
| `gligen_textbox_model` | Repräsentiert die spezifische GLIGEN-Modellkonfiguration, die zum Generieren des Textfelds verwendet werden soll. Sie ist entscheidend, um sicherzustellen, dass das Textfeld gemäß den gewünschten Spezifikationen generiert wird. | `GLIGEN` |
| `text` | Der Textinhalt, der kodiert und in die Konditionierung integriert werden soll. Er liefert die semantische Information, die das generative Modell steuert. | `STRING` |
| `width` | Die Breite des Textfelds in Pixeln. Sie definiert die räumliche Dimension des Textfelds innerhalb des generierten Bildes. | `INT` |
| `height` | Die Höhe des Textfelds in Pixeln. Ähnlich wie die Breite definiert sie die räumliche Dimension des Textfelds innerhalb des generierten Bildes. | `INT` |
| `x` | Die x-Koordinate der oberen linken Ecke des Textfelds innerhalb des generierten Bildes. Sie gibt die Position des Textfelds horizontal an. | `INT` |
| `y` | Die y-Koordinate der oberen linken Ecke des Textfelds innerhalb des generierten Bildes. Sie gibt die Position des Textfelds vertikal an. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning` | Die angereicherte Konditionierungsausgabe, die die ursprünglichen Konditionierungsdaten zusammen mit den neu angehängten Textfeldparametern und der kodierten Textinformation enthält. Sie wird verwendet, um das generative Modell bei der Erzeugung kontextbewusster Ausgaben zu steuern. | `CONDITIONING` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/de.md)
