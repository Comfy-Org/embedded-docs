# DifferentialDiffusion

Der Node „Differential Diffusion“ modifiziert den Denoising-Prozess, indem er eine binäre Maske auf Basis von Zeitschritt-Schwellenwerten anwendet. Er erzeugt eine Maske, die zwischen der ursprünglichen Denoise-Maske und einer schwellenwertbasierten binären Maske überblendet, wodurch eine kontrollierte Anpassung der Stärke des Diffusionsprozesses ermöglicht wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zu ändernde Diffusionsmodell | MODEL | Ja | - |
| `strength` | Steuert die Stärke der Überblendung zwischen der ursprünglichen Denoise-Maske und der binären Schwellenwertmaske (Standard: 1.0) | FLOAT | Nein | 0.0 - 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geänderte Diffusionsmodell mit aktualisierter Denoise-Maskenfunktion | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/de.md)

---
**Source fingerprint (SHA-256):** `26387c3e6c7ead5415b36cfc9b9eef73448527e70646ab253984ff9627f69a25`
