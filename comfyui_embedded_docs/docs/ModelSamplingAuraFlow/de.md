# ModelSamplingAuraFlow

Der Node ModelSamplingAuraFlow wendet eine spezialisierte Sampling-Konfiguration auf Diffusionsmodelle an, die speziell für AuraFlow-Modellarchitekturen entwickelt wurde. Er ändert das Sampling-Verhalten des Modells, indem er einen Shift-Wert anwendet, der die Sampling-Verteilung anpasst. Dieser Node erbt vom SD3-Modellsampling-Framework und ermöglicht eine feine Steuerung des Sampling-Prozesses.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das die AuraFlow-Sampling-Konfiguration angewendet werden soll | MODEL | Ja | - |
| `shift` | Der auf die Sampling-Verteilung anzuwendende Shift-Wert (Standard: 1.73, Schritt: 0.01) | FLOAT | Ja | 0.0 - 100.0 |
| `sampling` | Der beim Patchen des Modells verwendete Sampling-Modus (Standard: "flow"). Als erweiterte Option gekennzeichnet. | COMBO | Nein | "flow"<br>"img_to_img_velocity" |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeter AuraFlow-Sampling-Konfiguration | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/de.md)

---
**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`
