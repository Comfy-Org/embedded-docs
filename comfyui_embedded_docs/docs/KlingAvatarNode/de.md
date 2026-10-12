# Kling Avatar 2.0

Der Kling Avatar 2.0-Node erzeugt Digital-Human-Videos im Broadcast-Stil aus einem einzelnen Referenzfoto und einer Audiodatei. Er erstellt ein sprechendes Avatar-Video mit einem optionalen Text-Prompt, um die Aktionen, Emotionen und Kamerabewegungen des Avatars festzulegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Referenzbild des Avatars. Breite und Höhe müssen mindestens 300 px betragen. Das Seitenverhältnis muss zwischen 1:2,5 und 2,5:1 liegen. | IMAGE | Ja | - |
| `sound_file` | Audio-Eingabe. Muss eine Dauer zwischen 2 und 300 Sekunden haben. | AUDIO | Ja | - |
| `mode` | Der zu verwendende Generierungsmodus. | COMBO | Ja | `"std"`<br>`"pro"` |
| `prompt` | Optionaler Prompt zur Definition von Avatar-Aktionen, Emotionen und Kamerabewegungen. (Standard: leerer String) | STRING | Nein | - |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Die Eingaben `image` und `sound_file` unterliegen spezifischen Validierungsanforderungen. Das Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2,5 und 2,5:1 aufweisen. Die Audiodatei muss zwischen 2 und 300 Sekunden lang sein.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das generierte Digital-Human-Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/de.md)

---
**Source fingerprint (SHA-256):** `34f64d168d6c407d9ab474e2637513c172090a0f0c219675d32f8e70ff84f2ae`
