# LTXVSpatioTemporalGuidance

Dieser Node verbessert die räumlichen Details und die Bewegungskohärenz der LTXV-Videogenerierung, indem bei jedem Sampling-Schritt ein zusätzlicher Durchlauf ausgeführt wird. Während dieses Durchlaufs wird die Self-Attention der ausgewählten Transformer-Blöcke zu einem Value-Passthrough degradiert, und die Generierung wird von diesem degradierten Ergebnis weg gelenkt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Basismodell, auf das die raum-zeitliche Guidance angewendet werden soll. Das Modell wird geklont und an den Klon wird eine Post-CFG-Guidance-Funktion angehängt. | MODEL | Ja | — |
| `scale` | Die Stärke der Guidance, die auf das entrauschte Ergebnis angewendet wird. Bei Einstellung auf 0 hat die Guidance keine Wirkung. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 100.0 (Schritt 0.01) |
| `blocks` | Kommagetrennte Indizes der Transformer-Blöcke, die gestört werden sollen. Es werden nur numerische Werte verwendet; alle anderen Zeichen werden ignoriert. (Standard: "29") | STRING | Ja | — |
| `start_percent` | Der Anteil des Sampling-Prozesses, bei dem die Guidance beginnt. Dies ist ein erweiterter Parameter. (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.001) |
| `end_percent` | Der Anteil des Sampling-Prozesses, bei dem die Guidance endet. Dies ist ein erweiterter Parameter. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.001) |

Hinweis: Die Guidance wird nur während des Sampling-Intervalls zwischen `start_percent` und `end_percent` angewendet. Außerhalb dieses Intervalls wird das ursprüngliche entrauschte Ergebnis unverändert zurückgegeben. Wenn `scale` 0 ist oder `blocks` keine numerischen Werte enthält, hat der geführte Durchlauf keine Wirkung auf den Sampling-Prozess.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das geklonte Modell mit angehängter raum-zeitlicher Guidance-Funktion. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/de.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
