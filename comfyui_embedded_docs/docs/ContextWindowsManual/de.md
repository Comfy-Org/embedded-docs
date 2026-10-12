# ContextWindowsManual

Der Node Context Windows (Manual) ermöglicht es Ihnen, Kontextfenster für ein Modell während des Samplings manuell zu konfigurieren. Dabei werden überlappende Kontextsegmente mit einer angegebenen Länge, Überlappung und einem Scheduling-Muster erzeugt, sodass Daten in handhabbaren Blöcken verarbeitet werden und gleichzeitig die Kontinuität zwischen den Segmenten erhalten bleibt. Er bietet erweiterte Optionen zur Steuerung, wie Kontextfenster angewendet werden, einschließlich Noise-Shuffling, Beibehaltung von Conditioning und Korrekturen für kausale Fenster. Dieser Node ist experimentell.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das während des Samplings Kontextfenster angewendet werden. | MODEL | Ja | - |
| `context_length` | Die Länge des Kontextfensters (Standard: 16). | INT | Ja | 1+ |
| `context_overlap` | Die Überlappung des Kontextfensters (Standard: 4). | INT | Ja | 0+ |
| `context_schedule` | Schrittabhängiger Scheduling-Algorithmus für Kontextfenster (Standard: STATIC_STANDARD). | COMBO | Ja | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | Die Schrittweite des Kontextfensters; nur für uniforme Schedules anwendbar (Standard: 1). | INT | Ja | 1+ |
| `closed_loop` | Ob die Kontextfensterschleife geschlossen werden soll; nur für geloopte Schedules anwendbar (Standard: False). | BOOLEAN | Ja | - |
| `fuse_method` | Die Methode zum Fusionieren der Kontextfenster (Standard: PYRAMID). | COMBO | Ja | Statische Fuse-Methoden (siehe `ContextFuseMethods.LIST_STATIC`) |
| `dim` | Die Dimension, auf die die Kontextfenster angewendet werden (Standard: 0). | INT | Ja | 0-5 |
| `freenoise` | Ob FreeNoise-Noise-Shuffling angewendet werden soll; verbessert die Fenstermischung (Standard: False). | BOOLEAN | Ja | - |
| `cond_retain_index_list` | Liste von Latent-Indizes, die in den Conditioning-Tensoren für jedes Fenster beibehalten werden sollen. Für Concat-Style-I2V-Modelle (z. B. Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD) befindet sich das kodierte Startbild in den c_concat-Conditioning-Kanälen; wenn dies auf '0' gesetzt wird, bleibt dieser Startbildinhalt an Sub-Pos 0 jedes Fensters erhalten (Standard: ""). | STRING | Nein | - |
| `split_conds_to_windows` | Ob mehrere Conditionings (erstellt durch ConditionCombine) auf jedes Fenster basierend auf dem Regionsindex aufgeteilt werden sollen (Standard: False). | BOOLEAN | Nein | - |
| `latent_retain_index_list` | Liste von Latent-Indizes, die im Noise-Latent selbst für jedes Fenster beibehalten werden sollen. Verwenden Sie dies für Workflows, bei denen Referenzinhalte (z. B. ein Startbild) direkt im Noise-Latent statt in separaten Conditioning-Kanälen liegen (z. B. Inplace-Style-I2V wie LTXV, AnimateDiff). Unabhängig von `cond_retain_index_list` (Standard: ""). | STRING | Nein | - |
| `causal_window_fix` | Ob ein kausales Korrekturframe zu Kontextfenstern mit einem anderen Index als 0 hinzugefügt werden soll (Standard: True). | BOOLEAN | Nein | - |

**Parametereinschränkungen:**

- `context_stride` wird nur verwendet, wenn ein uniformer Schedule ausgewählt ist (`UNIFORM_STANDARD` oder `UNIFORM_LOOPED`).
- `closed_loop` ist nur auf geloopte Schedules anwendbar (`UNIFORM_LOOPED`).
- `dim` muss zwischen 0 und 5 (einschließlich) liegen.
- `cond_retain_index_list` und `latent_retain_index_list` erwarten eine durch Kommas getrennte Liste ganzzahliger Indizes als String (z. B. "0,1,2").
- `latent_retain_index_list` ist unabhängig von `cond_retain_index_list`.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit während des Samplings angewendeten Kontextfenstern. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/de.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
