# Hook-Modell als LoRA erstellen (MO)

Dieser Node erstellt einen Hook, der ein LoRA-Modell (Low-Rank Adaptation) anwendet, um ausschließlich die Modellkomponente eines neuronalen Netzwerks zu verändern. Er lädt eine Checkpoint-Datei und wendet sie mit einer angegebenen Stärke auf das Modell an, während die CLIP-Komponente unverändert bleibt. Dies ist ein experimenteller Node, der die Funktionalität der Basisklasse CreateHookModelAsLora erweitert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Die als LoRA-Modell zu ladende Checkpoint-Datei. Die verfügbaren Optionen hängen vom Inhalt des Checkpoint-Ordners ab. | STRING | Ja | Mehrere Optionen verfügbar |
| `strength_model` | Der Stärkemultiplikator für die Anwendung des LoRA auf die Modellkomponente (Standard: 1.0) | FLOAT | Ja | -20.0 bis 20.0 |
| `prev_hooks` | Optionale vorherige Hooks, die mit diesem Hook verkettet werden | HOOKS | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `hooks` | Die erstellte Hook-Gruppe, die die LoRA-Modelländerung enthält | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/de.md)

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
