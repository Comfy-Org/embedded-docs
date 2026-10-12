# FreSca

Der FreSca-Node wendet während des Sampling-Prozesses eine frequenzabhängige Skalierung auf die Guidance an. Er trennt das Guidance-Signal mithilfe von Fourier-Filterung in niederfrequente und hochfrequente Komponenten und wendet dann unterschiedliche Skalierungsfaktoren auf jeden Frequenzbereich an, bevor diese wieder zusammengeführt werden. Dies ermöglicht eine differenziertere Steuerung dessen, wie sich die Guidance auf verschiedene Aspekte der generierten Ausgabe auswirkt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die Frequenzskalierung angewendet werden soll | MODEL | Ja | - |
| `scale_low` | Skalierungsfaktor für niederfrequente Komponenten (Standard: 1.0) | FLOAT | Nein | 0 - 10 |
| `scale_high` | Skalierungsfaktor für hochfrequente Komponenten (Standard: 1.25) | FLOAT | Nein | 0 - 10 |
| `freq_cutoff` | Anzahl der Frequenzindizes um die Mitte, die als niederfrequent betrachtet werden (Standard: 20) | INT | Nein | 1 - 10000 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell, auf dessen Guidance-Funktion eine frequenzabhängige Skalierung angewendet wurde | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/de.md)

---
**Source fingerprint (SHA-256):** `2ff3517619d856db68a9091ae7c87af8c56a23420fa2176b089bf9700475a7a9`
