# MiniMax H3 Context Windows

Teilt das Sampling in überlappende Kontextfenster auf, sodass ein MiniMax H3-Video länger als das Single-Pass-Fenster des Modells sein kann. Die Fenster werden auf den 17-Frame-Chunks des Modells platziert, wodurch das erzeugte Video und Audio über Fenstergrenzen hinweg ausgerichtet bleiben. Verbinden Sie das zurückgegebene Modell anstelle des ursprünglichen Modells mit dem Sampler.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das während des Samplings Kontextfenster angewendet werden. | MODEL | Ja | - |
| `context_length` | Die Länge des Kontextfensters in echten Frames. Muss 17*n + 5 sein (Standard: 124). | INT | Ja | 22 bis 16384 (MAX_RESOLUTION), Schritt 17 |
| `context_overlap` | Die Überlappung des Kontextfensters in echten Frames. Muss 17*n + 5 sein (Standard: 39). | INT | Ja | 5 oder höher, Schritt 17 |
| `fuse_method` | Die Methode zum Zusammenführen der Kontextfenster (Standard: `"pyramid"`). | COMBO | Ja | `"pyramid"`<br>`"relative"`<br>`"flat"`<br>`"overlap-linear"` |
| `freenoise` | Ob FreeNoise-Rausch-Shuffling angewendet werden soll, was die Fensterüberblendung verbessert (Standard: True, erweiterter Parameter). | BOOLEAN | Ja | true<br>false |
| `split_conds_to_windows` | Ob mehrere Conditionings (erstellt von ConditionCombine) basierend auf dem Region-Index auf die einzelnen Fenster aufgeteilt werden (Standard: False, erweiterter Parameter). | BOOLEAN | Ja | true<br>false |

Beide Längen werden in echten Frames angegeben und vor dem Sampling in Latents umgewandelt: `context_length` wird bei 5 Frames oder weniger zu 2 Latents, andernfalls zu `((frames - 5) / 17) * 5 + 2`. `context_overlap` wird auf die gleiche Weise umgewandelt und dann auf `context_length` minus 5 begrenzt, sodass die Überlappung immer einen vollständigen Chunk zum Vorrücken übrig lässt. Der Node verwendet immer den statischen Zeitplan mit einer Schrittweite von 1, wendet die Fenster auf die latente Zeitdimension an und fügt kein kausales Korrektur-Frame hinzu, da jedes Fenster an einer Chunk-Grenze beginnt. `split_conds_to_windows` erwartet mehrere Conditionings, die vom ConditionCombine-Node erstellt wurden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit der angewendeten Kontextfensterkonfiguration. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ContextWindows/de.md)

---
**Source fingerprint (SHA-256):** `e9e019d0bc870abfe226ef1aafb2607f55c0cc1b297884db35fe98c465cc0d91`
