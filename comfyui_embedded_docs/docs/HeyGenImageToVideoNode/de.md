# HeyGen Video 1.0 Bild zu Video

Animieren Sie ein Bild zu einem Video mit synchronisiertem Dialog und Ton mithilfe von HeyGen Video 1.0. Das verbundene Bild wird als erstes Einzelbild verwendet, und das generierte Video behält dessen Seitenverhältnis bei. Beschreiben Sie im Prompt, was passieren soll, einschließlich eventueller Sprechtexte. Der Node lädt das Bild hoch, erstellt den Video-Job, wartet auf dessen Abschluss und gibt das resultierende Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Für die Generierung verwendete Modellversion. (Standard: `"heygen-video-1"`) | DYNAMIC_COMBO | Ja | `"heygen-video-1"` |
| `image` | Erstes Einzelbild des Videos. Es ist genau ein Bild erforderlich; ein Batch wird abgelehnt. Schneiden Sie das Bild zu, um die Form des Videos zu ändern, da die Ausgabe das Seitenverhältnis dieses Bildes beibehält. | IMAGE | Ja | 1 Bild, Seitenverhältnis 1:4 bis 4:1 |
| `prompt` | Beschreibung dessen, was im Video passiert, einschließlich etwaiger Dialoge. (Standard: leerer String) | STRING | Ja | 1 bis 16000 Zeichen |
| `duration` | Dauer des Ausgabevideos in Sekunden. Wird ignoriert, wenn `auto_duration` `"enabled"` ist. (Standard: 5) | INT | Ja | 5 bis 30 |
| `resolution` | Ausgaberesolution. (Standard: `"768p"`) | COMBO | Ja | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `seed` | Seed für die Generierung. Ergebnisse können auch bei gleichem Seed zwischen den Läufen variieren. (Standard: 42) | INT | Ja | 0 bis 4294967295 |
| `auto_duration` | Wenn aktiviert, richtet sich die Videolänge nach dem in Anführungszeichen stehenden Dialog im Prompt (8 bis 30 Sekunden), und `duration` wird ignoriert. (Standard: `"disabled"`) | COMBO | Nein | `"disabled"`<br>`"enabled"` |

### Parameterbeschränkungen

- **Einzelbild:** `image` muss genau ein Bild enthalten. Das Verbinden eines Batches löst einen Fehler aus.
- **Bildseitenverhältnis:** Das Bild darf nicht breiter als das 4-fache seiner Höhe und nicht höher als das 4-fache seiner Breite sein (zwischen 1:4 und 4:1); andernfalls schlägt die Ausführung fehl.
- **Prompt erforderlich:** Der Prompt muss mindestens ein Zeichen, das kein Leerzeichen ist, und höchstens 16000 Zeichen enthalten.
- **Seed:** Der Seed entscheidet nur, ob der Node erneut ausgeführt wird; Ergebnisse sind mit demselben Seed nicht reproduzierbar.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `VIDEO` | Das generierte Video mit synchronisiertem Dialog und Ton, im Seitenverhältnis des Eingabebildes. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `e711d1d84c6c73a2ee177903f982042086a57b3e1afff8390c6e5b3bcd09c914`
