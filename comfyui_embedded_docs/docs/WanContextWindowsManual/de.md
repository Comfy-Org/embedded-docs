# Wan-Kontextfenster

Der Node WAN Context Windows (Manual) ermöglicht es Ihnen, Kontextfenster für Videomodelle im Wan-Stil manuell zu konfigurieren. Er wendet diese Einstellungen während des Samplings an und gibt Ihnen Kontrolle über die Fensterlänge, die Überlappung, die Zeitplanung und die Fusionsmethode, die verwendet werden, während das Modell das Video verarbeitet. Kontextlänge und Überlappung werden in echten Frames angegeben und intern für die 2D-Verarbeitung des Modells umgerechnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die Kontextfenster während des Samplings angewendet werden. | MODEL | Ja | - |
| `context_length` | Die Länge des Kontextfensters in echten Frames. Muss 4*n + 1 sein (Standard: 81). | INT | Ja | 1 bis 16384 (MAX_RESOLUTION), Schritt 4 |
| `context_overlap` | Die Überlappung des Kontextfensters in echten Frames (Standard: 30). | INT | Ja | 0 oder höher |
| `context_schedule` | Schrittabhängiger Zeitplanungsalgorithmus für Kontextfenster (Standard: "uniform_standard"). | COMBO | Ja | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | Die Schrittweite des Kontextfensters; gilt nur für uniforme Zeitpläne (Standard: 1). | INT | Ja | 1 oder höher |
| `closed_loop` | Ob die Kontextfenster-Schleife geschlossen werden soll; gilt nur für Schleifen-Zeitpläne (Standard: False). | BOOLEAN | Ja | - |
| `fuse_method` | Die Methode zum Fusionieren der Kontextfenster (Standard: "pyramid"). | COMBO | Ja | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Ob FreeNoise-Rauschmischung angewendet werden soll; verbessert die Fensterüberblendung (Standard: True). | BOOLEAN | Ja | - |
| `retain_first_frame` | Das erste I2V-Frame in jedem Kontextfenster beibehalten (kann helfen, die anfängliche Referenz beizubehalten) (Standard: False). | BOOLEAN | Ja | - |
| `split_conds_to_windows` | Ob mehrere Conditionings (erstellt durch ConditionCombine) basierend auf dem Region-Index auf die einzelnen Fenster aufgeteilt werden sollen (Standard: False). | BOOLEAN | Ja | - |

**Hinweis:** `context_stride` wirkt sich nur auf uniforme Zeitpläne aus, und `closed_loop` gilt nur für Schleifen-Zeitpläne. Kontextlänge und Überlappung werden in echten Frames angegeben und während der Verarbeitung automatisch umgerechnet und auf gültige Mindestwerte begrenzt (`context_length` wird zu ((length - 1) / 4) + 1, `context_overlap` wird zu overlap / 4). `context_length` muss die Form 4*n + 1 haben. `retain_first_frame` ist für die Verwendung mit Image-to-Video gedacht. `split_conds_to_windows` erwartet mehrere Conditionings, die durch den Node ConditionCombine erstellt wurden. Der Parameter `fuse_method` enthält neben "pyramid" noch mehrere Optionen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit der angewendeten Kontextfenster-Konfiguration. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/de.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
