# Seed

Der Seed-Node stellt einen Ganzzahlwert bereit, der als Seed verwendet werden kann, um die Reproduzierbarkeit von Zufallsoperationen in anderen Nodes zu steuern. Durch die Bereitstellung eines konstanten Startwerts trägt er dazu bei, generierte Ergebnisse bei Bedarf wiederholbar zu halten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `seed` | Der zu verwendende Seed-Wert. Die Option zur Steuerung nach dem Generieren bestimmt, ob der Wert fest bleibt oder sich nach jeder Generierung ändert; in diesem Node ist sie auf fixed gesetzt. | INT | Ja | 0 bis 9223372036854775807 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `seed` | Der generierte Seed-Wert. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/de.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`
