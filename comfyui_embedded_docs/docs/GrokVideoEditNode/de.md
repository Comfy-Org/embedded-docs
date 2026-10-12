# GrokVideoEditNode

Dieser Node verwendet die Grok-API, um ein vorhandenes Video anhand eines Text-Prompts zu bearbeiten. Er lädt Ihr Video hoch, sendet eine Anfrage an das KI-Modell, um es gemäß Ihrer Beschreibung zu ändern, und gibt das neu generierte Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Videobearbeitung zu verwendende KI-Modell (Standard: "grok-imagine-video"). | COMBO | Ja | "grok-imagine-video" |
| `prompt` | Textbeschreibung des gewünschten Videos. | STRING | Ja | N/A |
| `video` | Das zu bearbeitende Eingabevideo. Die maximal unterstützte Dauer beträgt 8,7 Sekunden und die Dateigröße 50 MB. | VIDEO | Ja | N/A |
| `seed` | Seed, um zu bestimmen, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Nein | 0 bis 2147483647 |

**Einschränkungen:**

* `prompt` darf nicht leer sein.
* Das Eingabe-`video` muss eine Dauer zwischen 1 und 8,7 Sekunden haben.
* Die Dateigröße des Eingabe-`video` darf 50 MB nicht überschreiten.

**Hinweis:** Dieser Node ist ein API-Node und erfordert ein Comfy.org-Konto und einen API-Schlüssel, um ausgeführt zu werden. Die Nutzung wird mit etwa 0,06 $ pro Videosekunde abgerechnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das vom KI-Modell generierte bearbeitete Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/de.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`
