# FreeU

Der FreeU-Node wendet Modifikationen im Frequenzbereich auf die Ausgabeblöcke eines Modells an, um die Qualität der Bilderzeugung zu verbessern. Er funktioniert, indem verschiedene Kanalgruppen skaliert und Fourier-Filterung auf bestimmte Feature-Maps angewendet wird, wodurch eine fein abgestimmte Kontrolle über das Verhalten des Modells während des Generierungsprozesses ermöglicht wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das FreeU-Modifikationen angewendet werden | MODEL | Ja | - |
| `b1` | Backbone-Skalierungsfaktor, angewendet auf Feature-Maps mit model_channels × 4 Kanälen (Standard: 1.1). Als erweiterte Einstellung markiert. | FLOAT | Ja | 0.0 - 10.0 |
| `b2` | Backbone-Skalierungsfaktor, angewendet auf Feature-Maps mit model_channels × 2 Kanälen (Standard: 1.2). Als erweiterte Einstellung markiert. | FLOAT | Ja | 0.0 - 10.0 |
| `s1` | Skalierungsfaktor für Skip-Verbindungen, angewendet auf Feature-Maps mit model_channels × 4 Kanälen (Standard: 0.9). Als erweiterte Einstellung markiert. | FLOAT | Ja | 0.0 - 10.0 |
| `s2` | Skalierungsfaktor für Skip-Verbindungen, angewendet auf Feature-Maps mit model_channels × 2 Kanälen (Standard: 0.2). Als erweiterte Einstellung markiert. | FLOAT | Ja | 0.0 - 10.0 |

Hinweis: FreeU-Anpassungen werden nur auf Feature-Maps angewendet, deren Kanalanzahl model_channels × 4 entspricht (unter Verwendung von `b1` und `s1`) oder model_channels × 2 (unter Verwendung von `b2` und `s2`). Der Fourier-Filter skaliert nur den zentralen Niederfrequenzbereich (Schwellenwert 1) der Feature-Maps der Skip-Verbindungen; alle anderen Frequenzkomponenten bleiben unverändert. Alle vier Skalierungsparameter akzeptieren Werte zwischen 0.0 und 10.0 in Schritten von 0.01.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeten FreeU-Patches | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/de.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
