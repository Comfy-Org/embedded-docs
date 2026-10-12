# WanFunControlToVideo

Dieser Node wurde hinzugefügt, um das Alibaba Wan Fun Control-Modell für die Videogenerierung zu unterstützen, und wurde nach [diesem Commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82) hinzugefügt.

- **Zweck:** Bereitet die für die Videogenerierung benötigten Conditioning-Informationen vor, unter Verwendung des Wan 2.1 Fun Control-Modells.

Der Node WanFunControlToVideo ist eine ComfyUI-Erweiterung, die entwickelt wurde, um Wan Fun Control-Modelle für die Videogenerierung zu unterstützen, mit dem Ziel, WanFun-Control zur Videoerstellung zu nutzen.

Dieser Node dient als Vorbereitungspunkt für wesentliche Conditioning-Informationen und initialisiert den Mittelpunkt des latenten Raums, wodurch der nachfolgende Videogenerierungsprozess mit dem Wan 2.1 Fun-Modell gesteuert wird. Der Name des Nodes gibt seine Funktion klar an: Er akzeptiert verschiedene Eingaben und konvertiert sie in ein Format, das zur Steuerung der Videogenerierung innerhalb des WanFun-Frameworks geeignet ist.

Die Position des Nodes in der ComfyUI-Node-Hierarchie zeigt, dass er in den frühen Phasen der Videogenerierungs-Pipeline arbeitet und sich auf die Manipulation von Conditioning-Signalen konzentriert, bevor das eigentliche Sampling oder die Dekodierung der Videoframes erfolgt.

## Eingaben

| Parametername | Beschreibung | Erforderlich | Datentyp | Standardwert |
| --- | --- | --- | --- | --- |
| positive | Standardmäßige positive Conditioning-Daten von ComfyUI, typischerweise von einem „CLIP Text Encode“-Node. Der positive Prompt beschreibt Inhalt, Motiv und künstlerischen Stil, den der Benutzer für das generierte Video vorgibt. | Ja | CONDITIONING | N/A |
| negative | Standardmäßige negative Conditioning-Daten von ComfyUI, typischerweise erzeugt von einem „CLIP Text Encode“-Node. Der negative Prompt legt Elemente, Stile oder Artefakte fest, die im generierten Video vermieden werden sollen. | Ja | CONDITIONING | N/A |
| vae | Erfordert ein VAE-Modell (Variational Autoencoder), das mit der Wan 2.1 Fun-Modellfamilie kompatibel ist, verwendet zum Kodieren und Dekodieren von Bild-/Videodaten. | Ja | VAE | N/A |
| width | Die gewünschte Breite der Ausgabevideoframes in Pixeln; Standardwert 832, Mindestwert 16, Höchstwert durch nodes.MAX_RESOLUTION bestimmt, Schrittweite 16. | Ja | INT | 832 |
| height | Die gewünschte Höhe der Ausgabevideoframes in Pixeln; Standardwert 480, Mindestwert 16, Höchstwert durch nodes.MAX_RESOLUTION bestimmt, Schrittweite 16. | Ja | INT | 480 |
| length | Die Gesamtzahl der Frames im generierten Video; Standardwert 81, Mindestwert 1, Höchstwert durch nodes.MAX_RESOLUTION bestimmt, Schrittweite 4. | Ja | INT | 81 |
| batch_size | Die Anzahl der in einem einzelnen Batch generierten Videos; Standardwert 1, Mindestwert 1, Höchstwert 4096. | Ja | INT | 1 |
| clip_vision_output | (Optional) Von einem CLIP-Vision-Modell extrahierte visuelle Merkmale, die eine visuelle Stil- und Inhaltsführung ermöglichen. | Nein | CLIP_VISION_OUTPUT | None |
| start_image | (Optional) Ein Anfangsbild, das den Beginn des generierten Videos beeinflusst. | Nein | IMAGE | None |
| control_video | (Optional) Ermöglicht Benutzern, ein vorverarbeitetes ControlNet-Referenzvideo bereitzustellen, das die Bewegung und potenzielle Struktur des generierten Videos leitet. | Nein | IMAGE | None |

## Ausgaben

| Parametername | Beschreibung | Datentyp |
| --- | --- | --- |
| positive | Stellt erweiterte positive Conditioning-Daten bereit, einschließlich kodiertem start_image und control_video. | CONDITIONING |
| negative | Stellt ebenfalls erweiterte negative Conditioning-Daten bereit, die dasselbe concat_latent_image enthalten. | CONDITIONING |
| latent | Ein Dictionary, das einen leeren latenten Tensor mit dem Schlüssel „samples“ enthält. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/de.md)
