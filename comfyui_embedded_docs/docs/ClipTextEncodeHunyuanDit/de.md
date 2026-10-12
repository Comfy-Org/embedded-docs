# ClipTextEncodeHunyuanDit

Der Node `CLIPTextEncodeHunyuanDiT` wandelt Textbeschreibungen in ein Format um, das das HunyuanDiT-Modell verstehen kann. Er ist ein erweiterter Conditioning-Node, der für die duale Text-Encoder-Architektur von HunyuanDiT entwickelt wurde. Er verarbeitet zwei separate Texteingaben durch unterschiedliche Tokenizer und kombiniert deren Ergebnisse zu einer einzelnen Conditioning-Ausgabe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Eine CLIP-Modellinstanz, die zur Text-Tokenisierung und -Kodierung verwendet wird und zentral für die Erzeugung von Konditionierungen ist. | CLIP | Ja | - |
| `bert` | Texteingabe zur Kodierung über den BERT-Tokenizer. Bevorzugt Phrasen und Schlüsselwörter. Unterstützt mehrzeilige und dynamische Prompts. | STRING | Ja | - |
| `mt5xl` | Texteingabe zur Kodierung über den mT5-XL-Tokenizer. Unterstützt mehrzeilige und dynamische Prompts (mehrsprachig). Kann vollständige Sätze und komplexe Beschreibungen verwenden. | STRING | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die kodierte Conditioning-Ausgabe, die sowohl BERT- als auch mT5-XL-tokenisierten Text kombiniert und für die weitere Verarbeitung in Generierungsaufgaben verwendet wird. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeHunyuanDit/de.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
