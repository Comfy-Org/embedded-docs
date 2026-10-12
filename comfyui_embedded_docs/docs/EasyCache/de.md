# EasyCache

Der EasyCache-Node fügt einem Diffusionsmodell ein natives Caching-System hinzu, das die Sampling-Geschwindigkeit erhöht, indem Ergebnisse bereits berechneter Schritte wiederverwendet werden, anstatt jeden Schritt neu zu berechnen. Es wird nur zwischen einem konfigurierbaren Start- und Endpunkt des Sampling-Prozesses aktiviert und überspringt Schritte, wenn die geschätzte Änderung der Ausgabe unter einem benutzerdefinierten Schwellenwert bleibt. Dies ist ein experimenteller Node, der für fortgeschrittenes Debugging gedacht ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, dem EasyCache hinzugefügt werden soll. | MODEL | Ja | - |
| `reuse_threshold` | Der Schwellenwert für die Wiederverwendung zwischengespeicherter Schritte (Standard: 0.2). | FLOAT | Ja | 0.0 - 3.0 |
| `start_percent` | Der relative Sampling-Schritt, bei dem die Verwendung von EasyCache beginnt (Standard: 0.15). | FLOAT | Ja | 0.0 - 1.0 |
| `end_percent` | Der relative Sampling-Schritt, bei dem die Verwendung von EasyCache endet (Standard: 0.95). | FLOAT | Ja | 0.0 - 1.0 |
| `verbose` | Ob ausführliche Informationen protokolliert werden sollen (Standard: False). | BOOLEAN | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit hinzugefügter EasyCache-Funktionalität. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/de.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
