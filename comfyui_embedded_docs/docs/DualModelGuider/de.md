# DualModelGuider

Dieser Node ermöglicht die Verwendung von zwei unterschiedlichen Modellen während des geführten CFG-Sampling-Prozesses: ein Modell für den positiven (bedingten) Durchlauf und ein separates Modell für den negativen (unbedingten) Durchlauf. Wenn kein negatives Modell angegeben wird, verhält er sich wie ein Standard-CFG-Guider, der ein einzelnes Modell verwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Modell, das für den positiven (bedingten) Durchlauf verwendet wird. | MODEL | Ja | |
| `model_negative` | Modell, das für den negativen (unbedingten) Durchlauf verwendet wird. Verwenden Sie dasselbe Modell für gewöhnliches CFG. | MODEL | Nein | |
| `positive` | Die positive Konditionierungseingabe. | CONDITIONING | Ja | |
| `cfg` | Der CFG-Skalenwert (Standard: 4.0). | FLOAT | Ja | 0.0 bis 100.0 (Schritt: 0.1) |
| `negative` | Negative Konditionierung, die auf dem negativen Modell ausgeführt wird. Lassen Sie sie unverbunden für einen textfreien (nur Bild) unbedingten Durchlauf. | CONDITIONING | Nein | |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `GUIDER` | Ein Guider-Objekt, das mit den angegebenen Modellen und Konditionierungen für die Verwendung beim Sampling konfiguriert ist. | GUIDER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualModelGuider/de.md)

---
**Source fingerprint (SHA-256):** `a60803156e98d2ffe975d39922dfbeacafd1a2155d88dd2e285ac1426a1e7a33`
