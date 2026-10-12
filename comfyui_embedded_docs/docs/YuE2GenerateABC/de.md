# YuE2 ABC generieren

Dieser Node erzeugt eine ABC-Notation für einen Song basierend auf einer Stilbeschreibung und Liedtexten unter Verwendung eines YuE2-Text-and-Lyrics-Modells. Die resultierende `abc`-Ausgabe kann mit dem YuE2 Generate Music Node verbunden werden, um Audio zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | Das YuE2-Modell, das zum Tokenisieren des Stils und der Liedtexte sowie zum Erzeugen der ABC-Notation verwendet wird. | CLIP | Ja | - |
| `style` | Text, der den musikalischen Stil des Songs beschreibt. Unterstützt mehrzeilige Eingabe und dynamische Prompts. | STRING | Ja | - |
| `lyrics` | Text, der den Liedtext des Songs enthält. Unterstützt mehrzeilige Eingabe und dynamische Prompts. | STRING | Ja | - |
| `seed` | Zufallsseed für die Generierung. Eine Änderung führt zu anderen Ergebnissen. Standard: 0. | INT | Ja | 0 to 18446744073709551615 |
| `mode` | full: erzeugt Melodie und Akkorde; melody: erzeugt nur die Melodie, empfohlen für Cover. | COMBO | Ja | "full"<br>"melody" |
| `max_abc_tokens` | Maximale Anzahl der für die ABC-Notation generierten Tokens. Standard: 8192. Erweiterte Einstellung. | INT | Ja | 1 to 20000 |
| `temperature` | Steuert die Zufälligkeit der generierten Tokens. Höhere Werte erzeugen vielfältigere Ausgaben. Standard: 0.7. Erweiterte Einstellung. | FLOAT | Ja | 0.0 to 5.0 |
| `top_p` | Schwellenwert für Nucleus-Sampling; nur Tokens innerhalb dieser kumulativen Wahrscheinlichkeit werden berücksichtigt. Standard: 0.9. Erweiterte Einstellung. | FLOAT | Ja | 0.01 to 1.0 |
| `top_k` | Begrenzt die Token-Auswahl auf die K wahrscheinlichsten Tokens. Standard: 30. Erweiterte Einstellung. | INT | Ja | 1 to 32768 |
| `repetition_penalty` | Strafe, die während der Generierung auf wiederholte Tokens angewendet wird. Standard: 1.005. Erweiterte Einstellung. | FLOAT | Ja | 0.01 to 10.0 |
| `penalty_window` | Anzahl der letzten ABC-Tokens, die zur Bestrafung von Wiederholungen verwendet werden. Standard: 100. Erweiterte Einstellung. | INT | Ja | 1 to 20000 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `abc` | Die generierte ABC-Notation des Songs, die mit dem YuE2 Generate Music Node verbunden werden kann. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/de.md)

---
**Source fingerprint (SHA-256):** `2c1bf0841a044724ff0477f920972d70bbd97de49b56fbe6213a9ac134797130`
