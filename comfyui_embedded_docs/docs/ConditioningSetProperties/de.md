# ConditioningSetProperties

Der Node ConditioningSetProperties ändert die Eigenschaften von Conditioning-Daten, indem er die Stärke, Bereichseinstellungen anpasst und optionale Masken, Hooks oder Zeitschrittbereiche anwendet. Er ermöglicht Ihnen zu steuern, wie Conditioning den Generierungsprozess beeinflusst, indem Sie spezifische Parameter festlegen, die die Anwendung von Conditioning-Daten während der Bilderzeugung beeinflussen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `cond_NEW` | Die Conditioning-Daten, die geändert werden sollen | CONDITIONING | Erforderlich | - | - |
| `strength` | Steuert die Intensität des Conditioning-Effekts | FLOAT | Erforderlich | 1.0 | 0.0 - 10.0 (Schritt: 0.01) |
| `set_cond_area` | Bestimmt, wie der Conditioning-Bereich angewendet wird. Wählen Sie "default" für das Standardverhalten oder "mask bounds", um die Anwendung auf den Maskenbereich zu beschränken | STRING | Erforderlich | default | ["default", "mask bounds"] |
| `mask` | Optionale Maske, um einzuschränken, wo Conditioning angewendet wird | MASK | Optional | - | - |
| `hooks` | Optionale Hook-Funktionen für benutzerdefinierte Verarbeitung | HOOKS | Optional | - | - |
| `timesteps` | Optionaler Zeitschrittbereich, um einzuschränken, wann Conditioning aktiv ist | TIMESTEPS_RANGE | Optional | - | - |

**Hinweis:** Wenn eine `mask` bereitgestellt wird, kann der Parameter `set_cond_area` auf "mask bounds" gesetzt werden, um die Conditioning-Anwendung ausschließlich auf den maskierten Bereich zu beschränken. Der Parameter `hooks` ermöglicht benutzerdefinierte Verarbeitung über Hook-Funktionen, und `timesteps` begrenzt den Conditioning-Effekt auf einen bestimmten Zeitschrittbereich während der Generierung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die geänderten Conditioning-Daten mit aktualisierten Eigenschaften | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/de.md)

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
