# StableCascade_SuperResolutionControlnet

Dieser Node ist Teil der experimentellen Stable-Cascade-Gruppe. Er bereitet Eingaben für die Super-Resolution-Verarbeitung von Stable Cascade vor, indem er ein Eingabebild mit einem VAE kodiert, um eine ControlNet-Eingabe zu erstellen, und indem er leere (mit Nullen gefüllte) Latent-Platzhalter für Stage C und Stage B der Stable-Cascade-Pipeline generiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, das für die Super-Resolution verarbeitet werden soll. Nur die ersten 3 Farbkanäle (RGB) des Bildes werden zur Kodierung verwendet. | IMAGE | Ja | - |
| `vae` | Das VAE-Modell, das zur Kodierung des Eingabebilds verwendet wird | VAE | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `controlnet_input` | Die VAE-kodierte Bildrepräsentation, die als ControlNet-Eingabe geeignet ist | IMAGE |
| `stage_c` | Platzhalter-Latent-Repräsentation (mit Nullen gefüllt) für Stage C der Stable-Cascade-Verarbeitung, mit 16 Kanälen und Abmessungen basierend auf der Größe des Eingabebilds geteilt durch 16 | LATENT |
| `stage_b` | Platzhalter-Latent-Repräsentation (mit Nullen gefüllt) für Stage B der Stable-Cascade-Verarbeitung, mit 4 Kanälen und Abmessungen basierend auf der Größe des Eingabebilds geteilt durch 2 | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/de.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
