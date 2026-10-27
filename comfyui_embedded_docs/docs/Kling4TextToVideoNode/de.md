# Kling 4.0 Text to Video

Erzeugt ein Video aus einem Text-Prompt mit dem Kling 4.0-Modell, inklusive Audio. Dieser Node sendet den Prompt und die Generierungseinstellungen an die Kling API, wartet auf den Abschluss der Aufgabe und gibt das fertige Video zurück. Verwenden Sie ihn, wenn ein Clip allein aus einer Beschreibung erstellt werden soll, ohne Referenzmedien.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellauswahl. Nur `"kling-4.0"` ist verfügbar; die Auswahl blendet die unten aufgeführten Eingaben ein. | DYNAMIC_COMBO | Ja | `"kling-4.0"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung des zu generierenden Videos. Muss zwischen 1 und 26000 Zeichen lang sein. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. Standard: `"16:9"`. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 30 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, das nach Abschluss der Aufgabe vom Anbieter heruntergeladen wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `3835dcb7d83d843ea7f6c5dc691b48759d9c3e7a7baeead3d0f92817e73d6079`
