# Mirelo Text to SFX

Erzeugen Sie mit Mirelo SFX einen Soundeffekt aus einer Textbeschreibung. Beschreiben Sie den Klang selbst, nicht das Bild, zu dem er gehört; der Node gibt dann eine einzelne Audiospur in der angeforderten Länge zurück. Verwenden Sie ihn für Foley, Atmosphäre, Aufprallgeräusche und kurze musikalische Texturen, ohne ein Video zu drehen oder hochzuladen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Modell. Bei Auswahl eines Modells werden die spezifischen Parameter eingeblendet: `prompt`, `negative_prompt`, `duration` und `seed`. | DYNAMIC_COMBO | Ja | `"sfx-2.0"` |
| `prompt` | Beschreiben Sie den Klang, nicht das Bild. 1 bis 2000 Zeichen. | STRING | Ja | 1 bis 2000 Zeichen |
| `negative_prompt` | Zu vermeidende Klänge als kurze, durch Kommas getrennte Liste. Kann leer bleiben (Standard: leer). Maximal 1000 Zeichen. | STRING | Ja | Bis zu 1000 Zeichen |
| `duration` | Länge des Klangs in Sekunden. (Standard: 5.0) | FLOAT | Ja | 0.1 bis 600.0 (Schritt 0.1) |
| `seed` | Der Seed für die Anfrage. Die Ergebnisse sind nicht deterministisch, daher erzeugt derselbe Seed nicht erneut denselben Klang. (Standard: 42) | INT | Ja | 0 bis 4294967295 |

Der Node bricht mit einem Fehler ab, wenn `prompt` leer oder länger als 2000 Zeichen ist und wenn `negative_prompt` länger als 1000 Zeichen ist.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `AUDIO` | Der erzeugte Soundeffekt in der Länge von `duration`. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloTextToSFX/de.md)

---
**Source fingerprint (SHA-256):** `b09a9562cea636702acd9fc50feb38b272a558f8b8509da21f5fada2abd9fd48`
