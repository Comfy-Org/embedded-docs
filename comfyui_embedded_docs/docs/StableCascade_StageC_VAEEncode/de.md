# Stable Cascade Stage C VAE-Kodierung

Der Node StableCascade_StageC_VAEEncode verarbeitet ein Eingabebild durch einen VAE-Encoder, um latente Repräsentationen für das Stable-Cascade-Modell zu erzeugen. Zunächst wird die Größe des Bildes basierend auf einem Komprimierungsfaktor und dem Downscale-Verhältnis des VAE angepasst, anschließend wird das angepasste Bild codiert. Der Node gibt zwei latente Tensoren aus: einen für Stage C (das tatsächliche codierte Ergebnis) und einen für Stage B (einen mit Nullen gefüllten Platzhalter).

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, das in den latenten Raum codiert werden soll | IMAGE | Ja | - |
| `vae` | Das VAE-Modell, das zum Codieren des Bildes verwendet wird | VAE | Ja | - |
| `compression` | Der Komprimierungsfaktor, der vor der Codierung auf das Bild angewendet wird. Die Bildabmessungen werden durch diesen Wert geteilt und anschließend mit dem Downscale-Verhältnis des VAE multipliziert. Dies ist ein erweiterter Parameter. (Standard: 42) | INT | Ja | 4-128 (step: 1) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `stage_c` | Die codierte latente Repräsentation für Stage C des Stable-Cascade-Modells | LATENT |
| `stage_b` | Eine Platzhalter-latente Repräsentation für Stage B. Gibt derzeit einen mit Nullen gefüllten Tensor zurück, dessen Dimensionen aus der Größe des Eingabebilds berechnet werden. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/de.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
