# CreateHookLora

Der Node Create Hook LoRA erzeugt Hook-Objekte zum Anwenden von LoRA-Modifikationen (Low-Rank Adaptation) auf Modelle. Er lädt eine angegebene LoRA-Datei und erstellt Hooks, die die Modell- und CLIP-Stärken anpassen können, und kombiniert diese Hooks anschließend mit allen ihm übergebenen vorhandenen Hooks. Der Node verwaltet das Laden von LoRA effizient, indem er zuvor geladene LoRA-Dateien zwischenspeichert, um redundante Operationen zu vermeiden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `lora_name` | Der Name der aus dem loras-Verzeichnis zu ladenden LoRA-Datei | STRING | Ja | Mehrere Optionen verfügbar |
| `strength_model` | Der Stärke-Multiplikator für Modellanpassungen (Standard: 1.0) | FLOAT | Ja | -20.0 bis 20.0 |
| `strength_clip` | Der Stärke-Multiplikator für CLIP-Anpassungen (Standard: 1.0) | FLOAT | Ja | -20.0 bis 20.0 |
| `prev_hooks` | Optionale vorhandene Hook-Gruppe, die mit den neuen LoRA-Hooks kombiniert werden soll | HOOKS | Nein | N/A |

**Parametereinschränkungen:**

- Wenn sowohl `strength_model` als auch `strength_clip` auf 0 gesetzt sind, überspringt der Node das Erstellen neuer LoRA-Hooks und gibt die vorhandenen Hooks unverändert zurück
- Der Node speichert die zuletzt geladene LoRA-Datei im Cache, um die Leistung zu optimieren, wenn dasselbe LoRA wiederholt verwendet wird

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `HOOKS` | Eine Hook-Gruppe, die die kombinierten LoRA-Hooks und alle vorherigen Hooks enthält | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/de.md)

---
**Source fingerprint (SHA-256):** `42d5d776bfc9b239191952e2bce23513d183f904fc3c15039469381a547486f8`
