# T5TokenizerOptions

## Überblick

Der Node T5TokenizerOptions konfiguriert Tokenizer-Einstellungen für verschiedene T5-Modelltypen. Er legt Parameter für minimales Padding und minimale Länge für mehrere T5-Modellvarianten fest, darunter t5xxl, pile_t5xl, t5base, mt5xl und umt5xxl. Der Node nimmt eine CLIP-Eingabe entgegen, wendet die Einstellungen auf eine Kopie davon an und gibt den modifizierten CLIP zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, für das Tokenizer-Optionen konfiguriert werden | CLIP | Ja | - |
| `min_padding` | Minimaler Padding-Wert, der für alle T5-Modelltypen festgelegt wird (Standard: 0) | INT | Ja | 0 to 10000 |
| `min_length` | Minimaler Längenwert, der für alle T5-Modelltypen festgelegt wird (Standard: 0) | INT | Ja | 0 to 10000 |

Hinweis: Dieser Node ist in ComfyUI als experimentell gekennzeichnet. Die Einstellungen werden gleichzeitig auf alle unterstützten T5-Varianten angewendet: t5xxl, pile_t5xl, t5base, mt5xl und umt5xxl. Die Eingabe `clip` wird vor der Änderung geklont, sodass der ursprüngliche CLIP nicht verändert wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das modifizierte CLIP-Modell mit aktualisierten Tokenizer-Optionen, die auf alle T5-Varianten angewendet wurden | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/de.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
