# LTXVContextWindows

Dieser Node legt Kontextfenster für LTXV-ähnliche Modelle während des Samplings fest. Er unterteilt die Generierung in überlappende Fenster, um den Speicherverbrauch zu verwalten und die zeitliche Kohärenz zu verbessern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, auf das während des Samplings Kontextfenster angewendet werden. | MODEL | Ja | - |
| `context_length` | Die Länge des Kontextfensters in realen Frames. Muss 8*n + 1 entsprechen. (Standard: 145) | INT | Ja | Minimum: 1<br>Maximum: nodes.MAX_RESOLUTION<br>Schrittweite: 8 |
| `context_overlap` | Die Überlappung des Kontextfensters in realen Frames. (Standard: 40) | INT | Ja | Minimum: 0<br>Schrittweite: 8 |
| `context_schedule` | Schrittabhängiger Planungsalgorithmus für Kontextfenster. (Standard: "UNIFORM_STANDARD") | COMBO | Ja | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | Die Schrittweite des Kontextfensters; nur für gleichmäßige Zeitpläne anwendbar. (Standard: 1) | INT | Ja | Minimum: 1 |
| `closed_loop` | Ob die Kontextfensterschleife geschlossen werden soll; nur für Schleifen-Zeitpläne anwendbar. (Standard: False) | BOOLEAN | Ja | True<br>False |
| `fuse_method` | Die Methode zum Zusammenführen der Kontextfenster. Verfügbare Optionen werden durch `ContextFuseMethods.LIST_STATIC` definiert. (Standard: "PYRAMID") | COMBO | Ja | Definiert durch `ContextFuseMethods.LIST_STATIC` |
| `freenoise` | Ob FreeNoise-Rausch-Shuffling angewendet werden soll; verbessert die Fensterüberblendung. (Standard: True) | BOOLEAN | Ja | True<br>False |
| `retain_first_frame` | Ob das erste latente Frame in jedem Kontextfenster beibehalten werden soll (kann helfen, die initiale Referenz beizubehalten). (Standard: False) | BOOLEAN | Ja | True<br>False |
| `split_conds_to_windows` | Ob mehrere Konditionierungen (erstellt durch ConditionCombine) basierend auf dem Regionsindex auf die einzelnen Fenster aufgeteilt werden sollen. (Standard: False) | BOOLEAN | Ja | True<br>False |

**Hinweis:** Der Wert `context_length` wird in realen Frames angegeben und intern mit der Formel `((context_length - 1) // 8) + 1` in latente Frames umgerechnet, mit einem Minimum von 1. Der Wert `context_overlap` wird ebenfalls in realen Frames angegeben und durch Ganzzahldivision durch 8 in latente Frames umgerechnet, mit einem Minimum von 0. Der Tooltip für `context_length` weist darauf hin, dass er dem Muster 8*n + 1 folgen muss.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das Modell mit angewendeten Kontextfenstern für das Sampling. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/de.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
