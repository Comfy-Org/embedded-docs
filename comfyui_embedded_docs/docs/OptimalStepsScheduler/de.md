# OptimalStepsScheduler

Der Node OptimalStepsScheduler erstellt einen Rauschplan (eine Sequenz von Sigma-Werten) für die Verwendung während des Diffusions-Samplings. Er wählt die Basis-Rauschpegel anhand des ausgewählten Modelltyps, passt den Plan an, wenn Denoising nur teilweise angewendet wird, und interpoliert die Pegel, sodass die zurückgegebenen Sigmas mit der angeforderten Schrittanzahl übereinstimmen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model_type` | Der Typ des Diffusionsmodells, der für die Berechnung der Rauschpegel verwendet wird. Jede Option verwendet ihre eigene vordefinierte Tabelle mit Rauschpegeln. | COMBO | Ja | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | Die Gesamtzahl der zu berechnenden Sampling-Schritte (Standard: 20). | INT | Ja | 3 bis 1000 |
| `denoise` | Steuert die Denoising-Stärke, wodurch die effektive Anzahl der Schritte angepasst wird (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

**Hinweis:** Die Basis-Rauschpegel-Tabelle für den ausgewählten `model_type` wird mit log-linearer Interpolation neu abgetastet, wenn ihre Länge nicht gleich `steps + 1` ist, sodass die Ausgabe immer mit der angeforderten Schrittanzahl übereinstimmt.

**Hinweis:** Wenn `denoise` kleiner als 1.0 ist, verwendet der Node `round(steps * denoise)` als Gesamtzahl der effektiven Schritte und behält nur den passenden Endabschnitt des Plans bei. Wenn `denoise` 0.0 oder kleiner ist, gibt der Node einen leeren Tensor zurück.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Eine Sequenz von Sigma-Werten, die den Rauschplan für das Diffusions-Sampling darstellt. Der letzte Wert in der Sequenz wird immer auf 0 gesetzt. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/de.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
