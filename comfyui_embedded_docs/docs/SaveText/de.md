# Text speichern

Der Node „Save Text“ schreibt Textinhalt in eine Datei im Ausgabeverzeichnis. Er unterstützt das Speichern im Format .txt, .csv, .md oder .json und übernimmt automatisch die JSON-Formatierung, wenn gültiges JSON bereitgestellt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `text` | Der Textinhalt, der in einer Datei gespeichert werden soll. Diese Eingabe muss von einem anderen Node verbunden werden. | STRING | Ja | - |
| `filename_prefix` | Präfix für den Ausgabedateinamen. Ein 5-stelliger Zähler wird angehängt, um das Überschreiben vorhandener Dateien zu verhindern (Standard: "ComfyUI"). | STRING | Nein | - |
| `format` | Das Dateiformat, in dem der Text gespeichert werden soll (Standard: "txt"). Wenn "json" ausgewählt ist, wird gültiger JSON-Text mit einer Einrückung von 2 Leerzeichen formatiert; andernfalls wird der Text unverändert gespeichert. | COMBO | Nein | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

### Hinweise

- `text` ist eine erzwungene Eingabe und muss mit einem anderen Node verbunden werden; sie kann nicht direkt eingegeben werden.
- Die gespeicherte Datei heißt `<filename_prefix>_<5-digit counter>.<extension>` und wird in das ComfyUI-Ausgabeverzeichnis geschrieben (in einen Unterordner, der vom Präfix abgeleitet wird).
- Wenn das Format `"json"` ausgewählt wird, wird versucht, den Text als JSON zu parsen. Wenn das Parsen erfolgreich ist, wird der Inhalt mit einer Einrückung von 2 Leerzeichen formatiert geschrieben; wenn das Parsen fehlschlägt, wird der unveränderte Text geschrieben.
- Der Node meldet die gespeicherte Datei an die Oberfläche zurück, sodass sie zusammen mit den anderen generierten Ausgabedateien angezeigt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `text` | Der ursprüngliche Textinhalt, der in der Datei gespeichert wurde | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/de.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
