# CFG-Überschreibung

Der Node CFG Override überschreibt die CFG-Skala (Classifier-Free Guidance) über einen prozentualen (Sigma-)Bereich des Sampling-Prozesses mit einem festen Wert. Wenn mehrere CFG-Override-Nodes verwendet werden, gewinnt bei überlappenden Bereichen der Override, der dem Sampler am nächsten liegt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, auf das der CFG-Override angewendet werden soll. | MODEL | Ja | |
| `cfg` | Der feste CFG-Skalenwert, der während des Override-Bereichs verwendet wird. Standard: 1.0. | FLOAT | Ja | 0.0 bis 100.0 (Schritt: 0.1) |
| `start_percent` | Der Startpunkt des Override-Bereichs als Prozentsatz des Sampling-Prozesses. Standard: 0.0. | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.001) |
| `end_percent` | Der Endpunkt des Override-Bereichs als Prozentsatz des Sampling-Prozesses. Standard: 1.0. | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.001) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das Modell mit angewendetem CFG-Override-Wrapper. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/de.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
