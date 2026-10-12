# CombineHooksFour

Der Node Combine Hooks [4] führt bis zu vier separate Hook-Gruppen zu einer einzigen kombinierten Hook-Gruppe zusammen. Er akzeptiert jede beliebige Kombination der vier verfügbaren Hook-Eingaben und kombiniert sie mithilfe des Hook-Kombinationssystems von ComfyUI. So können Sie mehrere Hook-Konfigurationen für eine optimierte Verarbeitung in fortgeschrittenen Workflows zusammenfassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Erste zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_B` | Zweite zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_C` | Dritte zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_D` | Vierte zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |

**Hinweis:** Alle vier Hook-Eingaben sind optional. Der Node kombiniert nur die bereitgestellten Hook-Gruppen und gibt eine leere Hook-Gruppe zurück, wenn keine Eingaben verbunden sind.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `HOOKS` | Kombinierte Hook-Gruppe, die alle bereitgestellten Hook-Konfigurationen enthält | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/de.md)

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
