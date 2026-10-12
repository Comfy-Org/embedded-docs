# PikaScenesV2_2

Der PikaScenes v2.2-Node kombiniert mehrere Bilder, um ein Video zu erstellen, das Objekte aus allen Eingabebildern einbezieht. Sie können bis zu fünf verschiedene Bilder als Zutaten hochladen und ein hochwertiges Video generieren, das sie nahtlos miteinander vermischt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt_text` | Textbeschreibung dessen, was generiert werden soll | STRING | Ja | - |
| `negative_prompt` | Textbeschreibung dessen, was bei der Generierung vermieden werden soll | STRING | Ja | - |
| `seed` | Zufälliger Seed-Wert für die Generierung | INT | Ja | - |
| `resolution` | Ausgabauflösung für das Video | STRING | Ja | - |
| `duration` | Dauer des generierten Videos | INT | Ja | - |
| `ingredients_mode` | Modus zum Kombinieren der Zutaten (Standard: "creative") | STRING | Nein | "creative"<br>"precise" |
| `aspect_ratio` | Seitenverhältnis (Breite / Höhe) (Standard: 1.778) | FLOAT | Nein | 0.4 - 2.5 |
| `image_ingredient_1` | Bild, das als Zutat zur Erstellung eines Videos verwendet wird | IMAGE | Nein | - |
| `image_ingredient_2` | Bild, das als Zutat zur Erstellung eines Videos verwendet wird | IMAGE | Nein | - |
| `image_ingredient_3` | Bild, das als Zutat zur Erstellung eines Videos verwendet wird | IMAGE | Nein | - |
| `image_ingredient_4` | Bild, das als Zutat zur Erstellung eines Videos verwendet wird | IMAGE | Nein | - |
| `image_ingredient_5` | Bild, das als Zutat zur Erstellung eines Videos verwendet wird | IMAGE | Nein | - |

**Hinweis:** Sie können bis zu 5 Bildzutaten angeben, aber mindestens ein Bild ist erforderlich, um ein Video zu generieren. Der Node verwendet alle bereitgestellten Bilder, um die endgültige Videokomposition zu erstellen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das generierte Video, das alle Eingabebilder kombiniert | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/de.md)

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`
