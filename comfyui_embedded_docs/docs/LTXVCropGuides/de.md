# LTXVCropGuides

Der Node LTXVCropGuides entfernt Keyframe-Guidance-Daten aus einem Video-Generierungsworkflow. Er zählt die in der positiven Konditionierung aufgezeichneten Keyframes, schneidet entsprechend viele Frames vom Ende der Latent-Samples und der Noise-Maske ab und löscht die Keyframe-Indizes sowie Guide-Attention-Einträge aus beiden Konditionierungseingaben. Werden keine Keyframes gefunden, werden die Konditionierungseingaben unverändert zurückgegeben, und das Latent wird mit einem geklonten Sample-Tensor und seiner Noise-Maske durchgereicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierungseingabe mit Guidance-Informationen für die Generierung. Die Anzahl der darin enthaltenen Keyframes bestimmt, wie viele Frames vom Latent abgeschnitten werden. | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierungseingabe mit Guidance-Informationen darüber, was bei der Generierung vermieden werden soll. Ihre Keyframe-Daten werden zusammen mit der positiven Konditionierung gelöscht. | CONDITIONING | Ja | - |
| `latent` | Die Latent-Repräsentation mit Bild-Samples und Daten der Noise-Maske. Wenn Keyframes vorhanden sind, werden die letzten Keyframe-Frames sowohl aus den Samples als auch aus der Noise-Maske entfernt. | LATENT | Ja | - |

Hinweis: Ein Zuschneiden erfolgt nur, wenn Keyframe-Indizes in der positiven Konditionierung erkannt werden. Werden keine Keyframes erkannt, werden die positive und negative Konditionierung unverändert zurückgegeben, während das Latent weiterhin mit einem geklonten Sample-Tensor und einer expliziten Noise-Maske zurückgegeben wird (eine Maske aus lauter Einsen wird erstellt, wenn das Eingabe-Latent keine besitzt).

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die verarbeitete positive Konditionierung mit gelöschten Keyframe-Indizes und Guide-Attention-Einträgen | CONDITIONING |
| `negative` | Die verarbeitete negative Konditionierung mit gelöschten Keyframe-Indizes und Guide-Attention-Einträgen | CONDITIONING |
| `latent` | Die zugeschnittene Latent-Repräsentation mit angepassten Samples und Noise-Maske, bei der Keyframe-Abschnitte entfernt wurden | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/de.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
