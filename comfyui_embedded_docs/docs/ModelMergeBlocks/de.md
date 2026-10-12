# ModelMergeBlocks

ModelMergeBlocks ist für fortgeschrittene Modell-Merging-Operationen konzipiert und ermöglicht die Integration zweier Modelle mit anpassbaren Mischungsverhältnissen für verschiedene Teile der Modelle. Dieser Node erleichtert die Erstellung hybrider Modelle, indem Komponenten aus zwei Quellmodellen basierend auf angegebenen Parametern selektiv zusammengeführt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt wird. Es dient als Basismodell, auf das Patches aus dem zweiten Modell angewendet werden. | `MODEL` |
| `model2` | Das zweite Modell, aus dem Patches extrahiert und basierend auf den angegebenen Mischungsverhältnissen auf das erste Modell angewendet werden. | `MODEL` |
| `input` | Gibt das Mischungsverhältnis für die Eingabeschicht der Modelle an. Es bestimmt, wie viel von der Eingabeschicht des zweiten Modells in das erste Modell eingefügt wird. | `FLOAT` |
| `middle` | Definiert das Mischungsverhältnis für die mittleren Schichten der Modelle. Dieser Parameter steuert den Integrationsgrad der mittleren Schichten der Modelle. | `FLOAT` |
| `out` | Bestimmt das Mischungsverhältnis für die Ausgabeschicht der Modelle. Es beeinflusst die endgültige Ausgabe, indem der Beitrag der Ausgabeschicht des zweiten Modells angepasst wird. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das resultierende zusammengeführte Modell, das ein Hybrid aus den beiden Eingabemodellen ist, wobei Patches gemäß den angegebenen Mischungsverhältnissen angewendet wurden. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/de.md)
