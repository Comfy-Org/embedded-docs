# ReferenceTimbreAudio

Dieser Node legt das Referenzaudio für den Prozess „ace step 1.5“ fest. Er nimmt eine Konditionierungseingabe und optional eine latente Repräsentation von Audio entgegen und hängt dann diese latenten Daten an die Konditionierung an, sodass spätere Nodes sie als Referenzaudio-Timbre-Latents verwenden können. Dieser Node ist als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Die Konditionierungsdaten, an die die Referenzaudioinformationen angehängt werden. | CONDITIONING | Ja |  |
| `latent` | Eine optionale latente Repräsentation des Referenzaudios (Standard: None). Wenn angegeben, werden ihre Samples als Referenzaudio-Timbre-Latents an die Konditionierung angehängt. | LATENT | Nein |  |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die geänderten Konditionierungsdaten, die nun die Referenzaudio-Timbre-Latents enthalten, sofern die optionale Eingabe `latent` bereitgestellt wurde. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/de.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
