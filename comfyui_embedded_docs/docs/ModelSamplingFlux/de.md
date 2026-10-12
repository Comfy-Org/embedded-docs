# ModelSamplingFlux

Der Node ModelSamplingFlux wendet Flux-Modell-Sampling auf ein gegebenes Modell an, indem er anhand der Bildabmessungen einen Shift-Parameter berechnet. Er erstellt eine spezialisierte Sampling-Konfiguration, die das Verhalten des Modells entsprechend den angegebenen Parametern für Breite, Höhe und Shift anpasst, und gibt anschließend das geänderte Modell mit den neuen Sampling-Einstellungen zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das Flux-Sampling angewendet werden soll | MODEL | Ja | - |
| `max_shift` | Maximaler Shift-Wert für die Sampling-Berechnung (Standard: 1.15) | FLOAT | Ja | 0.0 - 100.0 (step 0.01) |
| `base_shift` | Basis-Shift-Wert für die Sampling-Berechnung (Standard: 0.5) | FLOAT | Ja | 0.0 - 100.0 (step 0.01) |
| `width` | Breite des Zielbildes in Pixeln (Standard: 1024) | INT | Ja | 16 - MAX_RESOLUTION (step 8) |
| `height` | Höhe des Zielbildes in Pixeln (Standard: 1024) | INT | Ja | 16 - MAX_RESOLUTION (step 8) |

`max_shift` und `base_shift` sind erweiterte Parameter. Der auf die Sampling-Konfiguration angewendete Shift wird aus den Bildabmessungen berechnet: Die latente Auflösung wird als `width × height / 256` berechnet, und der Shift-Wert wird zwischen `base_shift` bei einer latenten Auflösung von 256 und `max_shift` bei einer latenten Auflösung von 4096 interpoliert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geänderte Modell mit angewendeter Flux-Sampling-Konfiguration | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/de.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
