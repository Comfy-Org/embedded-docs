# CreateHookModelAsLora

Dieser Node erstellt ein Hook-Modell als LoRA (Low-Rank Adaptation), indem er Checkpoint-Gewichte lädt und Stärkeanpassungen sowohl auf die Modell- als auch auf die CLIP-Komponenten anwendet. Er ermöglicht LoRA-ähnliche Modifikationen an vorhandenen Modellen über einen Hook-basierten Ansatz, wodurch Feinabstimmung und Anpassung ohne dauerhafte Modelländerungen möglich sind. Der Node kann mit vorherigen Hooks kombiniert werden und speichert geladene Gewichte zwischen, um Effizienz zu steigern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Die Checkpoint-Datei, aus der Gewichte geladen werden (Auswahl aus verfügbaren Checkpoints) | STRING | Ja | Mehrere Optionen verfügbar |
| `strength_model` | Der Stärke-Multiplikator, der auf die Modellgewichte angewendet wird (Standard: 1.0) | FLOAT | Ja | -20.0 bis 20.0 |
| `strength_clip` | Der Stärke-Multiplikator, der auf die CLIP-Gewichte angewendet wird (Standard: 1.0) | FLOAT | Ja | -20.0 bis 20.0 |
| `prev_hooks` | Optionale vorherige Hooks, die mit den neu erstellten LoRA-Hooks kombiniert werden | HOOKS | Nein | - |

**Parametereinschränkungen:**

- Der Parameter `ckpt_name` lädt Checkpoints aus dem Ordner der verfügbaren Checkpoints
- Beide Stärkeparameter akzeptieren Werte von -20.0 bis 20.0 mit Schrittweiten von 0.01
- Wenn `prev_hooks` nicht angegeben wird, erstellt der Node eine neue Hook-Gruppe
- Der Node speichert geladene Gewichte zwischen, um zu vermeiden, dass derselbe Checkpoint mehrfach geladen wird

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `HOOKS` | Die erstellten LoRA-Hooks, kombiniert mit allen vorherigen Hooks, falls angegeben | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/de.md)

---
**Source fingerprint (SHA-256):** `8c0dd6b2e8e99e1d7dbc864aa802c0713842fb0d4ee018ea5cbedfb7896a770d`
