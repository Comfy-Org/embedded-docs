# InpaintModelConditioning

Der Node InpaintModelConditioning ist darauf ausgelegt, den Konditionierungsprozess für Inpainting-Modelle zu erleichtern. Er ermöglicht die Integration und Manipulation verschiedener Konditionierungseingaben, um die Inpainting-Ausgabe anzupassen. Er umfasst eine breite Palette von Funktionen – vom Laden spezifischer Modell-Checkpoints und der Anwendung von Stil- oder ControlNet-Modellen bis hin zum Kodieren und Kombinieren von Konditionierungselementen – und dient damit als umfassendes Werkzeug zur Anpassung von Inpainting-Aufgaben.

## Eingaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `positive` | Repräsentiert die positiven Konditionierungsinformationen oder -parameter, die auf das Inpainting-Modell angewendet werden sollen. Diese Eingabe ist entscheidend, um den Kontext oder die Einschränkungen zu definieren, unter denen die Inpainting-Operation ausgeführt werden soll, und beeinflusst die endgültige Ausgabe erheblich. | `CONDITIONING` |
| `negative` | Repräsentiert die negativen Konditionierungsinformationen oder -parameter, die auf das Inpainting-Modell angewendet werden sollen. Diese Eingabe ist wesentlich, um die Bedingungen oder Kontexte anzugeben, die während des Inpainting-Prozesses vermieden werden sollen, und beeinflusst dadurch die endgültige Ausgabe. | `CONDITIONING` |
| `vae` | Gibt das VAE-Modell an, das im Konditionierungsprozess verwendet werden soll. Diese Eingabe ist entscheidend, um die spezifische Architektur und die Parameter des VAE-Modells zu bestimmen, das genutzt wird. | `VAE` |
| `pixels` | Repräsentiert die Pixeldaten des Bildes, das per Inpainting bearbeitet werden soll. Diese Eingabe ist wesentlich, um den visuellen Kontext bereitzustellen, der für die Inpainting-Aufgabe erforderlich ist. | `IMAGE` |
| `mask` | Gibt die auf das Bild anzuwendende Maske an und kennzeichnet die Bereiche, die per Inpainting bearbeitet werden sollen. Diese Eingabe ist entscheidend, um die spezifischen Regionen innerhalb des Bildes zu definieren, die Inpainting erfordern. | `MASK` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die modifizierten positiven Konditionierungsinformationen nach der Verarbeitung, bereit zur Anwendung auf das Inpainting-Modell. Diese Ausgabe ist wesentlich, um den Inpainting-Prozess gemäß den angegebenen positiven Bedingungen zu steuern. | `CONDITIONING` |
| `negative` | Die modifizierten negativen Konditionierungsinformationen nach der Verarbeitung, bereit zur Anwendung auf das Inpainting-Modell. Diese Ausgabe ist wesentlich, um den Inpainting-Prozess gemäß den angegebenen negativen Bedingungen zu steuern. | `CONDITIONING` |
| `latent` | Die aus dem Konditionierungsprozess abgeleitete latente Repräsentation. Diese Ausgabe ist entscheidend, um die zugrunde liegenden Merkmale und Eigenschaften des Bildes zu verstehen, das per Inpainting bearbeitet wird. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/de.md)
