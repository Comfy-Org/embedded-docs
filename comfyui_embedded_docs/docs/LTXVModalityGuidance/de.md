# LTXV Modalitätssteuerung (A/V-Kopplung)

Dieser Node wendet eine modalitätsübergreifende (Audio-Video-)Führung auf ein LTXV-AV-Modell an. Während des Samplings führt er pro Schritt einen zusätzlichen Forward-Pass aus, bei dem die Cross-Attention-Verbindungen von Audio zu Video und Video zu Audio deaktiviert sind, und treibt anschließend das Ergebnis in Richtung der gekoppelten Vorhersage, um die audio-visuelle Synchronisation, etwa Lip-Sync, zu verstärken. Der Referenzstandardwert für `modality_scale` ist 3.0; wird er auf 1.0 gesetzt, deaktiviert dies den zusätzlichen Pass, und er lässt sich mit dem Dual-CFG-Guider und STG kombinieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Basismodell, auf das die Modalitätsführung angewendet wird. Es wird intern geklont, wobei das ursprüngliche Modell unverändert bleibt. | MODEL | Ja | - |
| `modality_scale` | Stärke der Audio-Video-Kopplungsführung. Standard ist 3.0. Auf 1.0 setzen, um den zusätzlichen Forward-Pass zu deaktivieren. | FLOAT | Ja | 1.0 bis 100.0 (Standard: 3.0) |
| `start_percent` | Der Punkt im Sampling-Prozess, als Prozentsatz von 0.0 bis 1.0, an dem die Modalitätsführung beginnt. Dies ist ein erweiterter Parameter. Standard ist 0.0. | FLOAT | Ja | 0.0 bis 1.0 (Standard: 0.0) |
| `end_percent` | Der Punkt im Sampling-Prozess, als Prozentsatz von 0.0 bis 1.0, an dem die Modalitätsführung endet. Dies ist ein erweiterter Parameter. Standard ist 1.0. | FLOAT | Ja | 0.0 bis 1.0 (Standard: 1.0) |

Die Führung wird nur auf Sampling-Schritte angewendet, deren Sigma-Werte in den durch `start_percent` und `end_percent` definierten Bereich fallen. Außerhalb dieses Bereichs gibt der Node das entrauschte Ergebnis unverändert zurück. Ein `modality_scale` von 1.0 deaktiviert außerdem den zusätzlichen Forward-Pass vollständig.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model` | Das geklonte Modell mit einer angehängten Post-CFG-Führungsfunktion. Dieses modifizierte Modell wendet während des Samplings die Modalitätsführung an. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/de.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
