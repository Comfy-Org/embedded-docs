# CombineHooks

Der Node Combine Hooks [2] führt zwei Hook-Gruppen zu einer einzelnen kombinierten Hook-Gruppe zusammen. Er akzeptiert zwei optionale Hook-Eingaben und kombiniert sie mithilfe der Hook-Kombinationsfunktionalität von ComfyUI. Dies ermöglicht es Ihnen, mehrere Hook-Konfigurationen für eine optimierte Verarbeitung zusammenzuführen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `hooks_A` | Erste zu kombinierende Hook-Gruppe | HOOKS | Nein | - |
| `hooks_B` | Zweite zu kombinierende Hook-Gruppe | HOOKS | Nein | - |

**Hinweis:** Beide Eingaben sind optional, aber mindestens eine Hook-Gruppe muss bereitgestellt werden, damit der Node funktioniert. Wenn nur eine Hook-Gruppe bereitgestellt wird, wird sie unverändert zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `hooks` | Kombinierte Hook-Gruppe, die alle Hooks aus beiden Eingabegruppen enthält | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/de.md)

---
**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`
