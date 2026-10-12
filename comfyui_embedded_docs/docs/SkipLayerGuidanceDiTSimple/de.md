# SkipLayerGuidanceDiTSimple

Einfache Version des SkipLayerGuidanceDiT-Nodes, die während des Denoising-Prozesses nur den unbedingten Durchlauf modifiziert. Dieser Node wendet Skip-Layer-Guidance auf bestimmte Transformer-Schichten in DiT-Modellen (Diffusion Transformer) an, indem er während des unbedingten Durchlaufs selektiv bestimmte Schichten basierend auf angegebenen Timing- und Schichtparametern überspringt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das Skip-Layer-Guidance angewendet werden soll | MODEL | Ja | - |
| `double_layers` | Durch Kommas getrennte Liste der Indizes von Double-Block-Schichten, die übersprungen werden sollen (Standard: "7, 8, 9") | STRING | Nein | - |
| `single_layers` | Durch Kommas getrennte Liste der Indizes von Single-Block-Schichten, die übersprungen werden sollen (Standard: "7, 8, 9") | STRING | Nein | - |
| `start_percent` | Der Startprozentsatz des Denoising-Prozesses, bei dem die Skip-Layer-Guidance beginnt (Standard: 0.0) | FLOAT | Nein | 0.0 - 1.0 |
| `end_percent` | Der Endprozentsatz des Denoising-Prozesses, bei dem die Skip-Layer-Guidance endet (Standard: 1.0) | FLOAT | Nein | 0.0 - 1.0 |

**Hinweis:** Skip-Layer-Guidance wird nur angewendet, wenn sowohl `double_layers` als auch `single_layers` gültige Schichtindizes enthalten. Wenn beide leer sind, gibt der Node das ursprüngliche Modell unverändert zurück. Die Skip-Layer-Guidance ist nur aktiv, wenn der Sigma-Wert des aktuellen Denoising-Schritts zwischen `start_percent` und `end_percent` liegt (intern in Sigma-Werte umgerechnet).

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell, bei dem Skip-Layer-Guidance auf die angegebenen Schichten angewendet wurde | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/de.md)

---
**Source fingerprint (SHA-256):** `f153348d75cf3b52d7d7d541f7467e51c797e1fe5844516591db7a191415cdb2`
