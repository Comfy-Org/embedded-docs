# Fun ControlNet anwenden

ZImageFunControlnet wendet einen ControlNet-Patch auf ein Basismodell an, damit es den Bildgenerierungs- oder Bildbearbeitungsprozess steuern kann. Der Node kombiniert ein Modell, einen Modell-Patch und einen VAE und ermöglicht es Ihnen, zu steuern, wie stark der ControlNet-Effekt das Ergebnis beeinflusst. Optionale Eingaben für Bild, Inpainting-Bild und Maske ermöglichen gezieltere Bearbeitungen. Der Node funktioniert mit Z-Image-ControlNet-Patches und mit Qwen Image 2.1 Fun ControlNet-Patches, die über den Node „Load Model Patch“ geladen werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Basismodell, das für den Generierungsprozess verwendet wird. | MODEL | Ja | - |
| `model_patch` | Ein spezialisiertes Patch-Modell, das die Steuerung des ControlNet anwendet. | MODEL_PATCH | Ja | - |
| `vae` | Der Variational Autoencoder, der zum Kodieren und Dekodieren von Bildern verwendet wird. | VAE | Ja | - |
| `strength` | Die Stärke des ControlNet-Einflusses. Positive Werte wenden den Effekt an, während negative Werte ihn invertieren können (Standard: 1.0). | FLOAT | Ja | -10.0 bis 10.0 (Schritt 0.01) |
| `image` | Ein optionales Basisbild, um den Generierungsprozess zu steuern. | IMAGE | Nein | - |
| `inpaint_image` | Ein optionales Bild, das speziell für Inpainting-Bereiche verwendet wird, die durch eine Maske definiert sind. | IMAGE | Nein | - |
| `mask` | Eine optionale Maske, die definiert, welche Bereiche eines Bildes bearbeitet oder per Inpainting gefüllt werden sollen. | MASK | Nein | - |
| `start_percent` | Der Punkt im Denoising-Prozess, als Bruchteil der gesamten Sampling-Schritte, an dem das ControlNet zu wirken beginnt (Standard: 0.0). | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.001) |
| `end_percent` | Der Punkt im Denoising-Prozess, an dem das ControlNet aufhört zu wirken (Standard: 1.0). | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.001) |

**Hinweis:** Der Parameter `inpaint_image` wird typischerweise zusammen mit einer `mask` verwendet, um den Inhalt für das Inpainting festzulegen. Das Verhalten des Nodes kann sich je nach den bereitgestellten optionalen Eingaben ändern (z. B. Verwendung von `image` zur Steuerung oder Verwendung von `image`, `mask` und `inpaint_image` für Inpainting). Die Werte `start_percent` und `end_percent` beschränken das ControlNet auf ein Fenster des Denoising-Prozesses; außerhalb dieses Fensters wird das Modell ohne den Patch gesampelt. Wenn `strength` 0 ist oder wenn keines von `image`, `inpaint_image` und `mask` verbunden ist, gibt der Node das Basismodell unverändert zurück. Bei Z-Image Control-Patches wird eine bereitgestellte Maske vor der Verwendung invertiert (1.0 - mask), während ein Qwen Image 2.1 Fun ControlNet-Patch die Maske unverändert verwendet. Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit angewendetem ControlNet-Patch, einsatzbereit für eine Sampling-Pipeline. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/de.md)

---
**Source fingerprint (SHA-256):** `9673b8b6e091713bcc93fe5fd1cfed12e6941571d1017e10ac94c19e1afd4ca1`
