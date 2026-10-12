# KSamplerSelect

Der KSamplerSelect-Node dient dazu, einen bestimmten Sampler anhand des angegebenen Sampler-Namens auszuwählen. Er abstrahiert die Komplexität der Sampler-Auswahl und ermöglicht es Benutzern, für ihre Aufgaben einfach zwischen verschiedenen Sampling-Strategien zu wechseln.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler_name` | Gibt den Namen des auszuwählenden Samplers an. Dieser Parameter bestimmt, welche Sampling-Strategie verwendet wird, und beeinflusst das allgemeine Sampling-Verhalten sowie die Ergebnisse. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Gibt das ausgewählte Sampler-Objekt zurück, das für Sampling-Aufgaben verwendet werden kann. | `SAMPLER` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/de.md)
