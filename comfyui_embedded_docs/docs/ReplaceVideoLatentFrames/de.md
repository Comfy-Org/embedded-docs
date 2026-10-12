# Video-Latent-Frames ersetzen

ReplaceVideoLatentFrames ersetzt eine Reihe von Frames in einem Ziel-Latent-Video durch Frames aus einem Quell-Latent-Video, beginnend bei einem angegebenen Frame-Index. Wenn kein Quell-Latent bereitgestellt wird, wird das Ziel-Latent unverändert zurückgegeben. Der Node unterstützt negative Indizes und protokolliert eine Warnung, wenn die Quell-Frames nicht in das Ziel passen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `destination` | Das Ziel-Latent, in dem Frames ersetzt werden. | LATENT | Ja | - |
| `source` | Das Quell-Latent, das Frames liefert, die in das Ziel-Latent eingefügt werden. Wenn es nicht bereitgestellt wird, wird das Ziel-Latent unverändert zurückgegeben. | LATENT | Nein | - |
| `index` | Der Start-Latent-Frame-Index im Ziel-Latent, an dem die Frames des Quell-Latents platziert werden. Negative Werte zählen vom Ende (Standard: 0; Schritt: 1). | INT | Ja | -MAX_RESOLUTION bis MAX_RESOLUTION |

**Einschränkungen:**

* Ein negativer `index` wird angepasst, indem er zur Frame-Anzahl des Ziels addiert wird, sodass er vom Ende des Ziel-Latents rückwärts zählt.
* Wenn `index` über die Frame-Anzahl des Ziels hinauszeigt oder wenn die Quell-Frames nicht in das Ziel ab `index` passen, wird eine Warnung protokolliert und das Ziel-Latent unverändert zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das resultierende Latent-Video nach der Frame-Ersetzungsoperation. Wenn die Ersetzung nicht durchgeführt werden kann, wird das Ziel-Latent unverändert zurückgegeben. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/de.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
