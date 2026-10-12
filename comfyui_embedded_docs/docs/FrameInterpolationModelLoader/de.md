# FrameInterpolationModelLoader

Dieser Node lädt eine Datei eines Frame-Interpolationsmodells und bereitet sie für die Verwendung im Workflow vor. Er erkennt automatisch, ob es sich bei der Datei um ein FILM- oder RIFE-Modell handelt, und konfiguriert das Modell für die verfügbare Hardware.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model_name` | Wählen Sie ein zu ladendes Frame-Interpolationsmodell aus. Modelle müssen im Ordner `frame_interpolation` abgelegt werden. | COMBO | Ja | Liste der Modelldateien im Ordner `frame_interpolation` |

Hinweis: Der Node unterstützt die Modellformate FILM und RIFE. Wenn die ausgewählte Datei kein erkanntes Format hat, wird ein Fehler ausgelöst.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | Das geladene und konfigurierte Frame-Interpolationsmodell, bereit zur Verwendung in anderen Nodes. | INTERP_MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/de.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
