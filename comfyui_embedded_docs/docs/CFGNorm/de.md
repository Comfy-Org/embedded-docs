# CFGNorm

CFGNorm passt an, wie Classifier-Free Guidance (CFG) in Diffusionsmodellen angewendet wird, indem die Größe (Norm) der bedingten Vorhersage mit der gelenkten Vorhersage verglichen und das Ergebnis neu skaliert wird. Ein `strength`-Wert steuert, wie stark diese Anpassung angewendet wird. Standardmäßig dämpft die Skalierung nur die Guidance-Ausgabe, während das Aktivieren von `pre_cfg` das kombinierte Rauschen vor der CFG-Kombination des Samplers ohne Clamping neu skaliert, was das Ergebnis verstärken kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das die CFG-Normalisierung angewendet werden soll | MODEL | Ja | - |
| `strength` | Steuert die Intensität des Normalisierungseffekts, der auf die CFG-Skalierung angewendet wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 100.0 (Schrittweite 0.01) |
| `pre_cfg` | Wenn true, wird das kombinierte Rauschen VOR der CFG-Kombination des Samplers ohne Clamping neu skaliert (kann verstärken). Entspricht der norm-skalierten CFG, die von Modellen wie Lens verwendet wird. Der Standardwert false behält das ursprüngliche Verhalten nach der CFG im x0-Raum bei, das ausschließlich dämpft. (Standard: False) | BOOLEAN | Nein | true / false |

Hinweis: Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `patched_model` | Gibt das geänderte Modell zurück, bei dem die CFG-Normalisierung auf seinen Sampling-Prozess angewendet wurde | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/de.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
