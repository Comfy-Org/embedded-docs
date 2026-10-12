# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet wendet einen Diffusionssynthese-Kontrollnetzwerk-Patch auf ein Basismodell an. Es verwendet ein Eingabebild und eine optionale Maske, um den Generierungsprozess des Modells mit einstellbarer Stärke zu steuern, und erzeugt ein gepatchtes Modell, das den Einfluss des Kontrollnetzwerks für eine kontrolliertere Bildsynthese integriert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Basismodell, das mit dem Kontrollnetzwerk gepatcht werden soll | MODEL | Ja | - |
| `model_patch` | Das Kontrollnetzwerk-Patchmodell, das auf das Basismodell angewendet werden soll | MODEL_PATCH | Ja | - |
| `vae` | Der im Diffusionsprozess verwendete VAE (Variational Autoencoder) | VAE | Ja | - |
| `image` | Das Eingabebild, das zur Steuerung des Kontrollnetzwerks verwendet wird. Nur die ersten drei Farbkanäle (RGB) werden verwendet; zusätzliche Kanäle werden verworfen | IMAGE | Ja | - |
| `strength` | Die Stärke des Einflusses des Kontrollnetzwerks (Standard: 1.0) | FLOAT | Ja | -10.0 bis 10.0 (Schrittweite 0.01) |
| `mask` | Optionale Maske, die Bereiche definiert, in denen das Kontrollnetzwerk angewendet werden soll. Bei DiffSynth- und Z-Image-Patches wird die Maske vor der Verwendung intern invertiert | MASK | Nein | - |
| `start_percent` | Der Punkt im Entrauschungsprozess, als Bruchteil der gesamten Sampling-Schritte, an dem das Kontrollnetzwerk zu wirken beginnt (Standard: 0.0) | FLOAT | Nein | 0.0 bis 1.0 (Schrittweite 0.001) |
| `end_percent` | Der Punkt im Entrauschungsprozess, an dem das Kontrollnetzwerk aufhört zu wirken (Standard: 1.0) | FLOAT | Nein | 0.0 bis 1.0 (Schrittweite 0.001) |

**Hinweis:** Die Werte `start_percent` und `end_percent` beschränken das Kontrollnetzwerk auf ein Fenster des Entrauschungsprozesses; außerhalb dieses Fensters wird das Modell ohne den Patch gesampelt. Wenn `strength` auf 0 gesetzt ist, gibt der Node das Basismodell unverändert zurück. Wenn eine Maske bereitgestellt wird, wird sie invertiert (1.0 - mask) und für den Z-Image Control- und den standardmäßigen DiffSynth-Pfad umgeformt, während ein Qwen Image 2.1 Fun ControlNet-Patch die Maske unverändert verwendet. Der Node wählt seine interne Patch-Implementierung anhand des geladenen Modell-Patches aus, daher verhalten sich dieselben Eingaben für Z-Image Control, Qwen Image 2.1 Fun ControlNet und standardmäßige DiffSynth-Checkpoints etwas unterschiedlich. Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendetem Diffusionssynthese-Kontrollnetzwerk-Patch | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/de.md)

---
**Source fingerprint (SHA-256):** `7be42c001c2937af7ca5c2d45aa8a529574aa9117b4740c62da822910041d231`
