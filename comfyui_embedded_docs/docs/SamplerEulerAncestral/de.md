# SamplerEulerAncestral

Der Node SamplerEulerAncestral erstellt einen Euler-Ancestral-Sampler, der während der Bildgenerierung verwendet werden kann. Dieser Sampler kombiniert Euler-Integration mit ancestralem Sampling, wodurch bei jedem Schritt ein gewisses Maß an Zufälligkeit hinzugefügt wird, um variierende Ergebnisse zu erzeugen. Mit diesem Node können Sie über seine Einstellungen anpassen, wie viel Zufälligkeit angewendet wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `eta` | Steuert die Schrittgröße und die Stochastizität des Sampling-Prozesses (Standard: 1.0). Dies ist ein erweiterter Parameter. | FLOAT | Ja | 0.0 - 100.0 |
| `s_noise` | Steuert die Menge an Rauschen, die während des Samplings hinzugefügt wird (Standard: 1.0). Dies ist ein erweiterter Parameter. | FLOAT | Ja | 0.0 - 100.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Gibt einen konfigurierten Euler-Ancestral-Sampler zurück, der in der Sampling-Pipeline verwendet werden kann. | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/de.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
