# Konditionierung (Kombinieren)

Dieser Node kombiniert zwei Conditioning-Eingaben zu einer einzigen Ausgabe und führt deren Informationen effektiv zusammen. Die beiden Bedingungen werden mittels Listenverkettung kombiniert.

## Eingaben

| Parametername | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning_1` | Die erste zu kombinierende Conditioning-Eingabe. Sie hat im Kombinationsprozess die gleiche Wichtigkeit wie `conditioning_2`. | `CONDITIONING` |
| `conditioning_2` | Die zweite zu kombinierende Conditioning-Eingabe. Sie hat im Kombinationsprozess die gleiche Wichtigkeit wie `conditioning_1`. | `CONDITIONING` |

## Ausgaben

| Parametername | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Das Ergebnis der Kombination von `conditioning_1` und `conditioning_2`, das die zusammengeführten Informationen kapselt. | `CONDITIONING` |

## Verwendungsszenarien

Vergleichen Sie die beiden untenstehenden Gruppen: Die linke Seite verwendet den Node ConditioningCombine, während die rechte Seite die normale Ausgabe zeigt.

![Vergleich](./asset/compare.jpg)

In diesem Beispiel haben die beiden in `Conditioning Combine` verwendeten Bedingungen die gleiche Wichtigkeit. Daher können Sie unterschiedliche Textkodierungen für Bildstil, Motivmerkmale usw. verwenden, wodurch die Prompt-Merkmale vollständiger ausgegeben werden können. Der zweite Prompt verwendet den kombinierten vollständigen Prompt, doch das semantische Verständnis kann völlig andere Bedingungen kodieren.

Mit diesem Node können Sie Folgendes erreichen:

- Grundlegende Textzusammenführung: Verbinden Sie die Ausgaben zweier Nodes vom Typ `CLIP Text Encode` mit den beiden Eingabeports von `Conditioning Combine`
- Komplexe Prompt-Kombination: Kombinieren Sie positive und negative Prompts, oder kodieren Sie Hauptbeschreibungen und Stilbeschreibungen getrennt und führen Sie sie anschließend zusammen
- Bedingungsketten-Kombination: Mehrere `Conditioning Combine`-Nodes können in Reihe verwendet werden, um eine schrittweise Kombination mehrerer Bedingungen zu erreichen

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/de.md)
