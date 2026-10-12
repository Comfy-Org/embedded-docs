# Wan Bild zu Bild

Der Wan Image to Image-Node erzeugt ein Bild aus einem oder zwei Eingabebildern und einem Text-Prompt. Er transformiert Ihre Eingabebilder basierend auf der von Ihnen bereitgestellten Beschreibung und erstellt ein neues Bild, das das Seitenverhältnis Ihres ursprünglichen Eingabebilds beibehält. Das Ausgabebild ist unabhängig von der Eingabegröße fest auf 1,6 Megapixel eingestellt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell (Standard: "wan2.5-i2i-preview"). | COMBO | Ja | "wan2.5-i2i-preview" |
| `image` | Einzelbildbearbeitung oder Fusion mehrerer Bilder. Maximal 2 Bilder. | IMAGE | Ja | - |
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch (Standard: leer). | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll (Standard: leer). | STRING | Nein | - |
| `seed` | Für die Generierung zu verwendender Seed (Standard: 0). | INT | Nein | 0 bis 2147483647 |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: false). | BOOLEAN | Nein | - |

**Hinweis:** Dieser Node akzeptiert genau 1 oder 2 Eingabebilder. Wenn Sie mehr als 2 Bilder oder gar keine Bilder übergeben, gibt der Node einen Fehler zurück.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das generierte Bild basierend auf den Eingabebildern und Text-Prompts. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/de.md)

---
**Source fingerprint (SHA-256):** `e78e5fb43d92c839448d3449b89445fb5db081ee8c947e44edcc048b8740f45d`
