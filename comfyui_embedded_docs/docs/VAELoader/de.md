# VaeLoader

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/vae` und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie möglicherweise **die ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Der VAELoader-Node dient zum Laden von Variational-Autoencoder-(VAE-)Modellen und ist speziell darauf ausgelegt, sowohl Standard- als auch approximierte VAEs zu verarbeiten. Er unterstützt das Laden von VAEs anhand des Namens, einschließlich spezieller Behandlung für die Modelle 'taesd' und 'taesdxl', und passt sich dynamisch an die spezifische Konfiguration der VAE an.

## Eingaben

| Feld | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `vae_name` | Gibt den Namen der zu ladenden VAE an, bestimmt, welches VAE-Modell abgerufen und geladen wird, und unterstützt eine Reihe vordefinierter VAE-Namen, einschließlich 'taesd' und 'taesdxl'. | `COMBO[STRING]` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `vae` | Gibt das geladene VAE-Modell zurück, bereit für weitere Operationen wie Kodieren oder Dekodieren. Die Ausgabe ist ein Modellobjekt, das den Zustand des geladenen Modells kapselt. | `VAE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/de.md)
