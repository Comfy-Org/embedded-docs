# ConditioningAverage

Der Node `ConditioningAverage` wird verwendet, um zwei unterschiedliche Sätze von Conditioning (z. B. Text-Prompts) gemäß einem angegebenen Gewicht zu mischen und daraus einen neuen Conditioning-Vektor zu erzeugen, der zwischen beiden liegt. Durch Anpassen des Gewichtsparameters können Sie den Einfluss der jeweiligen Konditionierung auf das Endergebnis flexibel steuern. Dies eignet sich besonders für Prompt-Interpolation, Stilfusion und andere fortgeschrittene Anwendungsfälle.

Wie unten gezeigt, können Sie durch Anpassen der Stärke von `conditioning_to` ein Ergebnis zwischen den beiden Konditionierungen ausgeben.

![example](./asset/example.webp)

## Eingaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning_to` | Der Ziel-Conditioning-Vektor, der als Hauptbasis für den gewichteten Durchschnitt dient. | `CONDITIONING` |
| `conditioning_from` | Der Quell-Conditioning-Vektor, der gemäß einem bestimmten Gewicht in das Ziel eingemischt wird. | `CONDITIONING` |
| `conditioning_to_strength` | Die Stärke des Ziel-Conditionings, Bereich 0.0-1.0, Standard 1.0, Schritt 0.01. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning` | Der resultierende Conditioning-Vektor nach dem Mischen, der den gewichteten Durchschnitt widerspiegelt. | `CONDITIONING` |

## Typische Anwendungsfälle

- **Prompt-Interpolation:** Sanfter Übergang zwischen zwei verschiedenen Text-Prompts, um Inhalte mit dazwischenliegendem Stil oder dazwischenliegender Semantik zu erzeugen.
- **Stilfusion:** Kombinieren Sie verschiedene künstlerische Stile oder semantische Bedingungen, um neuartige Effekte zu erzeugen.
- **Stärkeanpassung:** Steuern Sie den Einfluss einer bestimmten Konditionierung auf das Ergebnis präzise, indem Sie das Gewicht anpassen.
- **Kreative Erkundung:** Erkunden Sie vielfältige generative Effekte, indem Sie verschiedene Prompts mischen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/de.md)
