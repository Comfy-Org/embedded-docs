# RandomNoise

Der RandomNoise-Node erstellt einen Rauschgenerator basierend auf einem Seed-Wert, der während des Sampling-Prozesses verwendet wird. Derselbe Seed erzeugt immer dasselbe Rauschmuster, was konsistente, reproduzierbare Ergebnisse über mehrere Durchläufe hinweg ermöglicht. Sampler verwenden das erzeugte Rauschen bei der Verarbeitung latenter Bilder.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `noise_seed` | Der Seed-Wert, der zum Erzeugen des zufälligen Rauschmusters verwendet wird (Standard: 0). Derselbe Seed erzeugt immer dieselbe Rauschausgabe. Dieser Eingang enthält eine Option zur Steuerung nach der Generierung, um den Seed nach jeder Generierung automatisch zu aktualisieren. | INT | Ja | 0 bis 18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `noise` | Ein Rauschen-Objekt, das basierend auf dem angegebenen Seed-Wert zufälliges Rauschen für latente Samples erzeugt. Wird von Samplern während des Sampling-Prozesses verwendet. | NOISE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/de.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
