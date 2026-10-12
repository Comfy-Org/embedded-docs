# PairConditioningSetProperties

Der **PairConditioningSetProperties**-Node ermöglicht es Ihnen, Eigenschaften sowohl von positiven als auch negativen Conditioning-Paaren gleichzeitig zu ändern. Er wendet Stärkeanpassungen, Einstellungen für den Conditioning-Bereich sowie optionale Maskierungs- oder Timing-Steuerungen auf beide Conditioning-Eingaben an und gibt die geänderten positiven und negativen Conditioning-Daten zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive_NEW` | Die zu ändernde positive Conditioning-Eingabe | CONDITIONING | Ja | - |
| `negative_NEW` | Die zu ändernde negative Conditioning-Eingabe | CONDITIONING | Ja | - |
| `strength` | Der auf das Conditioning angewendete Stärkemultiplikator (Standard: 1.0) | FLOAT | Ja | 0.0 bis 10.0 |
| `set_cond_area` | Bestimmt, wie der Conditioning-Bereich berechnet wird (Standard: "default") | STRING | Ja | "default"<br>"mask bounds" |
| `mask` | Optionale Maske, um den Conditioning-Bereich einzuschränken | MASK | Nein | - |
| `hooks` | Optionale Hook-Gruppe für erweiterte Conditioning-Änderungen | HOOKS | Nein | - |
| `timesteps` | Optionaler Timestep-Bereich, um einzuschränken, wann das Conditioning angewendet wird | TIMESTEPS_RANGE | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Das geänderte positive Conditioning mit angewendeten Eigenschaften | CONDITIONING |
| `negative` | Das geänderte negative Conditioning mit angewendeten Eigenschaften | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/de.md)

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
