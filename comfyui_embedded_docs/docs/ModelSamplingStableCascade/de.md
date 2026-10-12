# ModelSamplingStableCascade

Der Node ModelSamplingStableCascade wendet Stable-Cascade-Sampling-Einstellungen auf ein Modell an, indem er einen Shift-Wert auf die Sampling-Parameter anwendet. Er gibt eine gepatchte Kopie des Eingabemodells mit der benutzerdefinierten Stable-Cascade-Sampling-Konfiguration zurück, wobei das ursprüngliche Modell unverändert bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Eingabemodell, auf das Stable-Cascade-Sampling angewendet werden soll | MODEL | Ja | - |
| `shift` | Der Shift-Wert, der auf die Sampling-Parameter angewendet wird (Standard: 2.0) | FLOAT | Ja | 0.0 - 100.0 (Schritt 0.01) |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendetem Stable-Cascade-Sampling | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/de.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
