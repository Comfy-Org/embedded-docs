# ControlnetApply

Die Verwendung von ControlNet erfordert eine Vorverarbeitung der Eingabebilder. Da die standardmäßig in ComfyUI enthaltenen Nodes keine Preprocessoren und ControlNet-Modelle mitbringen, installieren Sie bitte zunächst ControlNet-Preprocessoren [Preprocessoren hier herunterladen](https://github.com/Fannovel16/comfy_controlnet_preprocessors) sowie die entsprechenden ControlNet-Modelle.

## Eingaben

| Parameter | Datentyp | Funktion |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Positive Konditionierungsdaten, vom CLIP-Text-Encoder oder anderen Konditionierungseingaben |
| `negative` | `CONDITIONING` | Negative Konditionierungsdaten, vom CLIP-Text-Encoder oder anderen Konditionierungseingaben |
| `control_net` | `CONTROL_NET` | Das anzuwendende ControlNet-Modell, üblicherweise eine Eingabe vom ControlNet Loader |
| `image` | `IMAGE` | Bild für die ControlNet-Anwendung; muss von einem Preprocessor verarbeitet werden |
| `vae` | `VAE` | VAE-Modell-Eingabe |
| `strength` | `FLOAT` | Steuert die Stärke der Netzwerkanpassungen, Wertebereich 0~10. Empfohlene Werte im Bereich 0.5~1.5 sind sinnvoll. Niedrigere Werte erlauben dem Modell mehr Freiheit, höhere Werte erzwingen strengere Vorgaben. Zu hohe Werte können zu seltsamen Bildern führen. Sie können diesen Wert testen und anpassen, um den Einfluss des ControlNet fein abzustimmen. |
| `start_percent` | `FLOAT` | Wert 0.000~1.000; legt fest, wann die Anwendung von ControlNet als Prozentsatz beginnt. Beispiel: 0.2 bedeutet, dass die ControlNet-Steuerung die Bildgenerierung ab 20 % des Diffusionsprozesses beeinflusst. |
| `end_percent` | `FLOAT` | Wert 0.000~1.000; legt fest, wann die Anwendung von ControlNet als Prozentsatz endet. Beispiel: 0.8 bedeutet, dass die ControlNet-Steuerung die Bildgenerierung ab 80 % des Diffusionsprozesses nicht mehr beeinflusst. |

### Ausgaben

| Parameter | Datentyp | Funktion |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Durch ControlNet verarbeitete positive Konditionierungsdaten; können an nachfolgende ControlNet- oder K-Sampler-Nodes ausgegeben werden |
| `negative` | `CONDITIONING` | Durch ControlNet verarbeitete negative Konditionierungsdaten; können an nachfolgende ControlNet- oder K-Sampler-Nodes ausgegeben werden |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/de.md)
