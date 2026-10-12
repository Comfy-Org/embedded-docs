# CombineHooksEight

Der Node Combine Hooks [8] führt bis zu acht verschiedene Hook-Gruppen zu einer einzigen kombinierten Hook-Gruppe zusammen. Er nimmt mehrere Hook-Eingaben entgegen und kombiniert sie mithilfe der Hook-Kombinationsfunktionalität von ComfyUI. Dadurch können Sie mehrere Hook-Konfigurationen für eine optimierte Verarbeitung in erweiterten Workflows zusammenführen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Erste zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_B` | Zweite zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_C` | Dritte zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_D` | Vierte zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_E` | Fünfte zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_F` | Sechste zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_G` | Siebte zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |
| `hooks_H` | Achte zu kombinierende Hook-Gruppe | HOOKS | optional | None | - |

**Hinweis:** Alle Eingabeparameter sind optional. Der Node kombiniert nur die bereitgestellten Hook-Gruppen; leer gelassene werden ignoriert. Sie können eine bis acht Hook-Gruppen zur Kombination bereitstellen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `HOOKS` | Eine einzelne kombinierte Hook-Gruppe, die alle bereitgestellten Hook-Konfigurationen enthält | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/de.md)

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
