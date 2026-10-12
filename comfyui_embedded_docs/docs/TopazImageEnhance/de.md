# Topaz-Bildverbesserung (Legacy)

Der Node **Topaz Image Enhance** bietet Upscaling und Bildverbesserung nach Industriestandard. Er verarbeitet ein einzelnes Eingabebild mithilfe eines cloudbasierten KI-Modells, um Qualität, Details und Auflösung zu verbessern. Der Node bietet eine fein abgestufte Kontrolle über den Verbesserungsprozess, einschließlich Optionen für kreative Steuerung, Motivfokus und Gesichtserhalt.

Dieser Node ist eine Legacy-Version und in der Oberfläche als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Bildverbesserung zu verwendende KI-Modell. | COMBO | Ja | `"Reimagine"` |
| `image` | Das Eingabebild, das verbessert werden soll. Es wird nur ein Bild unterstützt. | IMAGE | Ja | - |
| `prompt` | Optionaler Text-Prompt als Anleitung für kreatives Upscaling (Standard: leer). | STRING | Nein | - |
| `subject_detection` | Steuert, auf welchen Teil des Bildes die Verbesserung ausgerichtet wird (Standard: "All"). | COMBO | Nein | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Gesichter (falls vorhanden) während der Verarbeitung verbessern (Standard: True). | BOOLEAN | Nein | - |
| `face_enhancement_creativity` | Legt die Kreativitätsstufe für die Gesichtsverbesserung fest (Standard: 0.0). | FLOAT | Nein | 0.0 - 1.0 |
| `face_enhancement_strength` | Steuert, wie scharf verbesserte Gesichter im Verhältnis zum Hintergrund sind (Standard: 1.0). | FLOAT | Nein | 0.0 - 1.0 |
| `crop_to_fill` | Standardmäßig wird das Bild mit Letterbox-Rändern versehen, wenn das Ausgabeseitenverhältnis abweicht. Aktivieren, um das Bild so zuzuschneiden, dass es die Ausgabeabmessungen ausfüllt (Standard: False). | BOOLEAN | Nein | - |
| `output_width` | Der Wert 0 bedeutet, automatisch zu berechnen (normalerweise entspricht dies der Originalgröße oder `output_height`, falls angegeben) (Standard: 0). | INT | Nein | 0 - 32000 |
| `output_height` | Der Wert 0 bedeutet, mit derselben Höhe wie das Original oder die Ausgabebreite auszugeben (Standard: 0). | INT | Nein | 0 - 32000 |
| `creativity` | Steuert die allgemeine Kreativitätsstufe der Verbesserung (Standard: 3). | INT | Nein | 1 - 9 |
| `face_preservation` | Bewahrt die Gesichtsidentität der abgebildeten Personen (Standard: True). | BOOLEAN | Nein | - |
| `color_preservation` | Bewahrt die Originalfarben (Standard: True). | BOOLEAN | Nein | - |

**Hinweis:** Dieser Node kann nur ein einzelnes Eingabebild verarbeiten. Die Übergabe eines Batches mit mehreren Bildern führt zu einem Fehler.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das verbesserte Ausgabebild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/de.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
