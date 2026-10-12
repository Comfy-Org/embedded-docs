# LatentOperationTonemapReinhard

Dieser Node erstellt eine latente Operation, die Reinhard-Tonemapping auf latente Vektoren anwendet. Er normalisiert jeden latenten Vektor, misst die Gesamt-Magnitudenverteilung (Mittelwert und Standardabweichung) und komprimiert anschließend extreme Magnituden mithilfe der Reinhard-Kurve, wobei die Gesamtstärke über einen Multiplikator gesteuert wird. Der Node ist als experimentell gekennzeichnet (auch suchbar als „hdr latent“).

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `multiplier` | Steuert die Intensität des Tonemapping-Effekts (Standard: 1.0) | FLOAT | Ja | 0.0 bis 100.0 (Schritt 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `operation` | Gibt eine Tonemapping-Operation zurück, die auf latente Vektoren angewendet werden kann | LATENT_OPERATION |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/de.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
