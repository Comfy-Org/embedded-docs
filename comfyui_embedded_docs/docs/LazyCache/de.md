# LazyCache

LazyCache ist eine experimentelle Eigenbauversion von EasyCache, die während des Samplings Caching hinzufügt, um den Rechenaufwand zu reduzieren. Sie wurde für universelle Kompatibilität mit Modellen in ComfyUI entwickelt, obwohl sie im Allgemeinen schlechter abschneidet als EasyCache und möglicherweise nur in seltenen Fällen besser funktioniert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, dem LazyCache hinzugefügt wird. | MODEL | Ja | - |
| `reuse_threshold` | Der Schwellenwert für die Wiederverwendung zwischengespeicherter Schritte. Standard: 0.2. | FLOAT | Ja | 0.0 - 3.0 (step 0.01) |
| `start_percent` | Der relative Sampling-Schritt, bei dem die Verwendung von LazyCache beginnt. Standard: 0.15. | FLOAT | Ja | 0.0 - 1.0 (step 0.01) |
| `end_percent` | Der relative Sampling-Schritt, bei dem die Verwendung von LazyCache endet. Standard: 0.95. | FLOAT | Ja | 0.0 - 1.0 (step 0.01) |
| `verbose` | Ob ausführliche Informationen protokolliert werden sollen. Standard: False. | BOOLEAN | Ja | - |

Hinweis: `reuse_threshold`, `start_percent`, `end_percent` und `verbose` sind als erweiterte Eingaben gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit hinzugefügter LazyCache-Funktionalität. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/de.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
