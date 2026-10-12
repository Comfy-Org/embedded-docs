# ModelSamplingLTXV

Der ModelSamplingLTXV-Node wendet erweiterte Sampling-Parameter basierend auf der Token-Anzahl auf ein Modell an. Er berechnet einen Shift-Wert durch lineare Interpolation zwischen `base_shift` und `max_shift` über einen Token-Bereich und versieht das Eingabemodell mit einer spezialisierten Sampling-Konfiguration. Wenn ein `latent` bereitgestellt wird, bestimmen dessen Dimensionen die Token-Anzahl; andernfalls werden 4096 Token verwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Eingabemodell, auf das die Sampling-Parameter angewendet werden. | MODEL | Ja | - |
| `max_shift` | Der maximale Shift-Wert, der in der linearen Interpolationsberechnung verwendet wird (Standard: 2.05). | FLOAT | Ja | 0.0 bis 100.0 (Schritt: 0.01) |
| `base_shift` | Der Basis-Shift-Wert, der in der linearen Interpolationsberechnung verwendet wird (Standard: 0.95). | FLOAT | Ja | 0.0 bis 100.0 (Schritt: 0.01) |
| `latent` | Optionaler Latent-Eingang, der zur Bestimmung der Token-Anzahl für die Shift-Berechnung verwendet wird. Wenn nicht angegeben, wird eine Standard-Token-Anzahl von 4096 verwendet. | LATENT | Nein | - |

Der Shift-Wert wird berechnet, indem zwischen `base_shift` bei 1024 Token und `max_shift` bei 4096 Token interpoliert wird. Wenn `latent` bereitgestellt wird, ist die Token-Anzahl das Produkt aller Dimensionen nach den ersten beiden in den Latent-Samples (die räumlichen/zeitlichen Dimensionen). Wenn kein `latent` bereitgestellt wird, beträgt die Token-Anzahl standardmäßig 4096.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geänderte Modell mit den angewendeten Sampling-Parametern. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/de.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
