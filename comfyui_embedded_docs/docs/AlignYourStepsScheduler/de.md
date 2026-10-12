# AlignYourStepsScheduler

Der Node AlignYourStepsScheduler erzeugt Sigma-Werte (Rauschpegel) für den Denoising-Prozess basierend auf verschiedenen Modelltypen. Er berechnet geeignete Rauschpegel für jeden Schritt des Sampling-Prozesses und passt die Gesamtzahl der Schritte gemäß dem `denoise`-Parameter an, wodurch die Sampling-Schritte besser an die spezifischen Anforderungen verschiedener Diffusionsmodelle angepasst werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model_type` | Gibt den Modelltyp an, der für die Sigma-Berechnung verwendet werden soll (Standard: `"SD1"`) | COMBO | Ja | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | Die Gesamtzahl der zu generierenden Sampling-Schritte (Standard: 10) | INT | Ja | 1 bis 10000 |
| `denoise` | Steuert, wie stark das Bild entrauscht wird, wobei 1.0 alle Schritte verwendet und niedrigere Werte weniger Schritte verwenden (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

Hinweis: Jeder Modelltyp verfügt über einen integrierten Rauschpegel-Zeitplan mit 11 Sigma-Werten (für 10 Schritte). Wenn `denoise` 0.0 ist, gibt der Node einen leeren Sigma-Tensor zurück. Wenn `denoise` zwischen 0.0 und 1.0 liegt, wird die effektive Anzahl der Schritte als `round(steps × denoise)` berechnet, und nur der entsprechende letzte Abschnitt des Sigma-Zeitplans wird verwendet. Wenn der angeforderte Wert für `steps` nicht mit der Länge des integrierten Zeitplans übereinstimmt, werden die Rauschpegel logarithmisch-linear interpoliert, um der angeforderten Schrittzahl zu entsprechen. Der endgültige Sigma-Wert wird immer auf 0 gesetzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Gibt die berechneten Sigma-Werte für den Denoising-Prozess zurück | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/de.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
