# StabilityUpscaleConservativeNode

Bild mit minimalen Änderungen auf 4K-Auflösung hochskalieren. Dieser Node verwendet das konservative Upscaling von Stability AI, um die Bildauflösung zu erhöhen, während der ursprüngliche Inhalt erhalten bleibt und nur subtile Änderungen vorgenommen werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das hochskaliert werden soll | IMAGE | Ja | - |
| `prompt` | Was Sie im Ausgabebild sehen möchten. Ein starker, beschreibender Prompt, der Elemente, Farben und Motive klar definiert, führt zu besseren Ergebnissen. (Standard: leerer String) | STRING | Ja | - |
| `creativity` | Steuert die Wahrscheinlichkeit, zusätzliche Details zu erzeugen, die nicht stark durch das Initialbild konditioniert sind. (Standard: 0.35) | FLOAT | Ja | 0.2 - 0.5 |
| `seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird. (Standard: 0) | INT | Ja | 0 - 4294967294 |
| `negative_prompt` | Schlüsselwörter für das, was Sie im Ausgabebild nicht sehen möchten. Dies ist eine erweiterte Funktion. (Standard: leerer String) | STRING | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das hochskalierte Bild in 4K-Auflösung | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/de.md)

---
**Source fingerprint (SHA-256):** `e4faa795d5a197cdc85c6985b99e8a7229b2b64f929eea3fefff3aff32558c18`
