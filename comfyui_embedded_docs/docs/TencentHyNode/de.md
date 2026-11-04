# Tencent HY

Dieser Node erzeugt Textantworten mit Tencent's Hy4-Modell. Er sendet einen Text-Prompt sowie optional ein oder mehrere Bilder als Kontext und gibt die Antwort des Modells als Text zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, das zur Erzeugung der Antwort verwendet wird. Bei Auswahl werden die zugehörigen Eingaben unten eingeblendet. Standard: `"Hy4"`. | DYNAMIC_COMBO | Ja | `"Hy4"` |

### Hy4 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"Hy4"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Die Nachricht, die an das Modell gesendet wird. Darf nicht leer sein. Standard: "" (leere Zeichenkette). | STRING | Ja | Mindestens 1 Zeichen |
| `images` | Bis zu 20 Bilder. Jedes Bild in einem Batch zählt. Standard: keine Bilder. | AUTOGROW | Nein | 0 bis 20 Bilder |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells bestimmen. Standard: "" (leere Zeichenkette). | STRING | Nein | - |
| `reasoning` | Das Modell denkt vor der Antwort nach. Antworten dauern länger und verbrauchen mehr Tokens, und sehr schwierige Aufgaben können in einen Timeout laufen. Standard: False. | BOOLEAN | Ja | true<br>false |
| `temperature` | Steuert die Zufälligkeit. Die Ergebnisse variieren auch bei 0. Standard: 1.0. | FLOAT | Ja | 0.0 bis 1.4 (Schritt: 0.01) |
| `max_tokens` | Maximale Anzahl zu generierender Tokens, einschließlich Reasoning-Tokens, wenn `reasoning` aktiviert ist. Sehr lange Antworten können in einen Timeout laufen. Standard: 32000. | INT | Ja | 1 bis 64000 |

**Einschränkungen:**

* Pro Anfrage werden höchstens 20 Bilder akzeptiert, wobei jedes Bild eines Batches zählt.
* Tencent's Inhaltsfilter kann eine Anfrage blockieren, was einen Fehler auslöst.
* Wenn `max_tokens` aufgebraucht ist, bevor die Antwort abgeschlossen ist, löst der Node einen Fehler aus: Erhöhen Sie `max_tokens` oder deaktivieren Sie `reasoning`.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `STRING` | Die Textantwort des Hy4-Modells. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentHyNode/de.md)

---
**Source fingerprint (SHA-256):** `c7c1d2908d2fba8172fa279b7d273f5f3f96cf10b531f81650824fc8e0176f21`
