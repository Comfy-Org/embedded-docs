# Konditionierung (Verketten)

Der Node ConditioningConcat ist dafür ausgelegt, Conditioning-Vektoren zu verketten, insbesondere den Vektor 'conditioning_from' in den Vektor 'conditioning_to' einzufügen. Diese Operation ist grundlegend in Szenarien, in denen die Conditioning-Informationen aus zwei Quellen zu einer einzigen, vereinheitlichten Repräsentation kombiniert werden müssen.

## Eingaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `conditioning_to` | Stellt den primären Satz von Conditioning-Vektoren dar, an die die Vektoren aus `conditioning_from` angehängt werden. Er dient als Basis für den Verkettungsprozess. | `CONDITIONING` |
| `conditioning_from` | Besteht aus Conditioning-Vektoren, die an die Vektoren aus `conditioning_to` angehängt werden sollen. Dieser Parameter ermöglicht es, zusätzliche Conditioning-Informationen in den vorhandenen Satz zu integrieren. | `CONDITIONING` |

## Ausgaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `conditioning` | Die Ausgabe ist ein vereinheitlichter Satz von Conditioning-Vektoren, der aus der Verkettung der Vektoren aus `conditioning_from` mit den Vektoren aus `conditioning_to` resultiert. | `CONDITIONING` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/de.md)
