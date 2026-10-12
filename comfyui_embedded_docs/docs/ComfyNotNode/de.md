# ComfyNotNode

Der Not-Node führt eine logische NOT-Operation für jeden Eingabewert aus. Er gibt True zurück, wenn der Eingabewert als falsy gilt (z. B. 0, ein leerer String, None oder False), und gibt False zurück, wenn der Eingabewert truthy ist; dabei folgt er Pythons Standardregeln für Wahrheitswerte.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `value` | Der umzukehrende Eingabewert. Jeder Datentyp wird akzeptiert und anhand der Python-Regeln für Wahrheitswerte ausgewertet. | ANY | Ja | Any value |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die logische Umkehrung des Eingabewerts. Gibt True zurück, wenn die Eingabe falsy ist, und False, wenn die Eingabe truthy ist. | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/de.md)

---
**Source fingerprint (SHA-256):** `24bbe667a0800b187d991b24894794e2ce710256200a2667ff391c1e644963a5`
