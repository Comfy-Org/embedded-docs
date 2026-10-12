# HeyGen Video 1.0 Bild zu Video

Animieren Sie ein Bild mit synchronisiertem Dialog und Ton mithilfe von HeyGen Video 1.0 in ein Video. Das verbundene Bild wird als erstes Einzelbild verwendet, und das generierte Video behält das Seitenverhältnis des Bildes bei. Beschreiben Sie im Prompt, was geschehen soll, einschließlich eventueller Dialogzeilen. Der Node lädt das Bild hoch, erstellt den Video-Job, wartet auf dessen Fertigstellung und gibt das resultierende Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Für die Generierung verwendete Modellversion. (Standard: `"heygen-video-1"`) | DYNAMIC_COMBO | Ja | `"heygen-video-1"` |
| `image` | Erstes Einzelbild des Videos. Es ist genau ein Bild erforderlich; ein Batch wird abgelehnt. Schneiden Sie das Bild zu, um die Form des Videos zu ändern, da die Ausgabe das Seitenverhältnis dieses Bildes beibehält. | IMAGE | Ja | 1 Bild, Seitenverhältnis 1:4 bis 4:1 |
| `prompt` | Beschreibung dessen, was im Video geschieht, einschließlich eventueller Dialoge. (Standard: leerer String) | STRING | Ja | 1 bis 32000 Zeichen |
| `duration` | Dauer des Ausgabevideos in Sekunden. (Standard: 5) | INT | Ja | 5 bis 15 |
| `resolution` | Ausgabeauflösung. (Standard: `"768p"`) | COMBO | Ja | `"768p"`<br>`"480p"`<br>`"2k"` |
| `seed` | Seed für die Generierung. Ergebnisse können bei gleichem Seed zwischen Durchläufen dennoch variieren. (Standard: 42) | INT | Ja | 0 bis 4294967295 |

### Parametereinschränkungen

- **Einzelnes Bild:** `image` muss genau ein Bild enthalten. Das Verbinden eines Batches löst einen Fehler aus.
- **Bildseitenverhältnis:** Das Bild darf nicht breiter als das 4-Fache seiner Höhe und nicht höher als das 4-Fache seiner Breite sein (zwischen 1:4 und 4:1); andernfalls schlägt der Lauf fehl.
- **Prompt erforderlich:** Der Prompt muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist, und darf höchstens 32000 Zeichen lang sein.
- **Seed:** Der Seed entscheidet nur, ob der Node erneut ausgeführt wird; Ergebnisse sind mit demselben Seed nicht reproduzierbar.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit synchronisiertem Dialog und Ton, im Seitenverhältnis des Eingabebildes. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `e15def8ce378572247be7dd197ac469fb655bcecf76521c8e9495bbad34e0284`
