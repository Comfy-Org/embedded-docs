# SUPIRApply

Der SUPIRApply-Node wendet einen SUPIR-Modell-Patch auf ein Diffusionsmodell an. Er verwendet den Patch, um das Verhalten des Modells zu ändern, sodass es während des Sampling-Prozesses Guidance von einem Eingabebild einbeziehen kann. Der Node bietet außerdem Steuerelemente zum Anpassen der Stärke dieser Guidance über die Zeit und enthält eine optionale Funktion, die dabei hilft, die Treue zur ursprünglichen Eingabe zu wahren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Basis-Diffusionsmodell, auf das der SUPIR-Patch angewendet wird. | MODEL | Ja | - |
| `model_patch` | Der SUPIR-Modell-Patch mit den Gewichten und der Konfiguration zum Ändern des Modells. | MODEL_PATCH | Ja | - |
| `vae` | Der VAE (Variational Autoencoder), der verwendet wird, um das Eingabebild in eine latente Repräsentation zu kodieren. | VAE | Ja | - |
| `image` | Das Eingabebild, das zur Steuerung des Generierungsprozesses verwendet wird. Nur die ersten drei Farbkanäle (RGB) werden verwendet. | IMAGE | Ja | - |
| `strength_start` | Steuerstärke zu Beginn des Samplings (hohes Sigma). Der Einfluss der Bild-Guidance beginnt bei diesem Wert. (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |
| `strength_end` | Steuerstärke am Ende des Samplings (niedriges Sigma). Wird linear vom Startwert interpoliert. Der Einfluss der Bild-Guidance endet bei diesem Wert. (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |
| `restore_cfg` | Zieht die entrauschte Ausgabe zum Eingabe-Latent. Höher = stärkere Treue zur Eingabe. 0 zum Deaktivieren. (Standard: 4.0, erweiterte Einstellung) | FLOAT | Ja | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Sigma-Schwellenwert, unterhalb dessen `restore_cfg` deaktiviert ist. (Standard: 0.05, erweiterte Einstellung) | FLOAT | Ja | 0.0 - 1.0 |

*Hinweis:* Die Eingabe `image` wird verarbeitet, um nur die RGB-Kanäle zu extrahieren. Wenn ein Bild mit einem Alpha-Kanal bereitgestellt wird, wird der Alpha-Kanal ignoriert.

*Hinweis:* Wenn der SUPIR-Modell-Patch Denoise-Encoder-Gewichte bereitstellt, wird das Eingabebild mit diesen Gewichten anstelle des regulären VAE-Encoders kodiert.

*Hinweis:* `restore_cfg` wird nur wirksam, wenn es auf einen Wert größer als 0 gesetzt ist. Wenn es auf 0 gesetzt wird, wird die Restore-Nachverarbeitung vollständig deaktiviert. Wenn es aktiv ist, wird die Korrektur nur angewendet, solange der aktuelle Sigma-Wert über `restore_cfg_s_tmin` liegt.

*Hinweis:* Dieser Node ist in ComfyUI als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Eine geklonte Kopie des Eingabemodells mit angewendetem SUPIR-Patch und allen zusätzlich konfigurierten Post-CFG-Funktionen. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/de.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
