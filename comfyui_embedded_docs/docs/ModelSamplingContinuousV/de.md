# ModelSamplingContinuousV

Der Node ModelSamplingContinuousV passt das Sampling-Verhalten eines Modells an, indem kontinuierliches V-Prediction-Sampling angewendet wird. Er erstellt einen Klon des Eingabemodells und konfiguriert ihn mit benutzerdefinierten minimalen und maximalen Sigma-Werten für eine feinere Kontrolle über den Sampling-Prozess.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Eingabemodell, das mit kontinuierlichem V-Prediction-Sampling geändert werden soll | MODEL | Ja | - |
| `sampling` | Die anzuwendende Sampling-Methode; derzeit ist V-Prediction die einzige verfügbare Option (Standard: `"v_prediction"`) | COMBO | Ja | `"v_prediction"` |
| `sigma_max` | Der maximale Sigma-Wert für das Sampling (erweiterter Parameter, Standard: 500.0, Schritt: 0.001) | FLOAT | Ja | 0.0 - 1000.0 |
| `sigma_min` | Der minimale Sigma-Wert für das Sampling (erweiterter Parameter, Standard: 0.03, Schritt: 0.001) | FLOAT | Ja | 0.0 - 1000.0 |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-----------|-----------|
| `model` | Das geänderte Modell mit angewendetem kontinuierlichem V-Prediction-Sampling | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/de.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
