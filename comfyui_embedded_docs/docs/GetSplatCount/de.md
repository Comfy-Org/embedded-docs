# Splat-Anzahl abrufen

Der Node Get Splat Count gibt die Gesamtzahl der Splats (Gauß-Punkte) in einem Splat-Batch zurück, summiert über alle Elemente im Batch. Er leitet die ursprünglichen Splat-Daten unverändert weiter und stellt gleichzeitig eine Zählung bereit, wie viele einzelne Splats enthalten sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `splat` | Die Splat-Daten, in denen die Anzahl der Splats gezählt werden soll | SPLAT | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `splat` | Die ursprünglichen Splat-Daten, unverändert weitergeleitet | SPLAT |
| `count` | Die Gesamtzahl der Splats, über den Batch summiert | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetSplatCount/de.md)

---
**Source fingerprint (SHA-256):** `fbb913b70bbbe4701b91783b6f47969d9132737c464ae590243f9f38061a05dc`
