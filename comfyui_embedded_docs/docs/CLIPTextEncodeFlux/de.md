# ClipTextEncodeFlux

`CLIPTextEncodeFlux` ist ein Textkodierungsknoten, der für die Flux-Architektur entwickelt wurde. Er verarbeitet zwei separate Texteingaben durch unterschiedliche Encoder – CLIP-L und T5XXL – und kombiniert sie mit einer Guidance-Skala, um eine vereinheitlichte Konditionierungsausgabe für die Bildgenerierung zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Ein CLIP-Modell, das die Flux-Architektur unterstützt, einschließlich der Encoder CLIP-L und T5XXL. | CLIP | Ja | - |
| `clip_l` | Texteingabe, die vom CLIP-L-Encoder verarbeitet wird. Geeignet für prägnante Stichwortbeschreibungen, z. B. Stil oder Thema. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | - |
| `t5xxl` | Texteingabe, die vom T5XXL-Encoder verarbeitet wird. Geeignet für detaillierte Beschreibungen in natürlicher Sprache, die komplexe Szenen und Details ausdrücken. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | - |
| `guidance` | Steuert den Einfluss der Textkonditionen auf den Generierungsprozess. Höhere Werte bedeuten eine strengere Befolgung des Textes. Standard: 3.5. In Schritten von 0,1 einstellbar. | FLOAT | Ja | 0.0 - 100.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Enthält die fusionierten Embeddings aus beiden Encodern und den Parameter `guidance`, die für die konditionierte Bildgenerierung verwendet werden. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/de.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
