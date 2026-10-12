# Krea 2 Bild

## Überblick

Der Krea 2 Image-Node generiert Bilder mit dem Krea 2 KI-Modell. Er unterstützt zwei Modellvarianten: Medium für ausdrucksstarke Illustrationen und Large für ausdrucksstarken Fotorealismus, mit einer zusätzlichen Medium-Turbo-Option für schnellere Generierung. Sie können optional ein Moodboard und bis zu 10 Bildstilreferenzen einbeziehen, um das generierte Bild zu beeinflussen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für das Bild. | STRING | Ja | N/A |
| `model` | Krea 2 Medium ist am besten für ausdrucksstarke Illustrationen geeignet; Krea 2 Large ist am besten für ausdrucksstarken Fotorealismus geeignet. | DICT | Ja | Siehe unten |
| `seed` | Zufälliger Seed für die Reproduzierbarkeit (Standard: 0). | INT | Ja | 0 bis 2147483647 |

Der Parameter `model` ist ein Dictionary mit den folgenden Unterparametern:

| Unterparameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|---------------|-------------|-----------|----------|-------|
| `model` | Wählt die Krea 2 Modellvariante aus. | STRING | Ja | `"krea 2 medium turbo"`<br>`"krea 2 medium"`<br>`"krea 2 large"` |
| `aspect_ratio` | Das Seitenverhältnis für das generierte Bild. | STRING | Ja | N/A |
| `resolution` | Die Auflösung für das generierte Bild. | STRING | Ja | N/A |
| `creativity` | Steuert die Kreativitätsstufe der Generierung. | FLOAT | Ja | N/A |
| `moodboard_id` | Die UUID eines Krea-Moodboards, um das Bild zu beeinflussen. Muss eine gültige UUID sein. | STRING | Nein | N/A |
| `moodboard_strength` | Die Stärke des Moodboard-Einflusses (Standard: 0.35). | FLOAT | Nein | N/A |
| `style_reference` | Eine Liste von Bildstilreferenzen. Jede Referenz muss eine `url` (STRING) und `strength` (FLOAT) haben. | LIST | Nein | 0 bis 10 Elemente |

**Einschränkungen:**
- `moodboard_id` muss eine gültige UUID sein (z. B. `"123e4567-e89b-12d3-a456-426614174000"`). Kopieren Sie sie von der Krea-Website.
- `style_reference` akzeptiert maximal 10 Bildstilreferenzen.
- Der `prompt` muss mindestens 1 Zeichen lang sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das generierte Bild als Tensor. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/de.md)

---
**Source fingerprint (SHA-256):** `645b404fe2c7653662803f1630125bdef912429c95d7b3a1268b0e0d7f533277`
