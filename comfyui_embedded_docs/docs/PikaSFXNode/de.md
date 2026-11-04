# Pika SFX

Dieser Node erzeugt mit Pika einen Soundeffekt aus einer Textbeschreibung. Beschreiben Sie den Soundeffekt und wie lange er dauern soll, und der Node gibt einen Audioclip zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Welcher Soundeffekt erzeugt werden soll. Darf nicht leer sein. Standard: "" (leere Zeichenkette). | STRING | Ja | 1 bis 4000 Zeichen |
| `duration` | Länge des Soundeffekts in Sekunden. Standard: 5.0. | FLOAT | Ja | 1.0 bis 20.0 (Schritt: 0.1) |
| `seed` | Seed für das Sampling. Standard: 42. | INT | Ja | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Der erzeugte Soundeffekt. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSFXNode/de.md)

---
**Source fingerprint (SHA-256):** `a1dcd374d158009aceae2aecd87ed08f8105bff7db75160a99e8624be9459dfa`
