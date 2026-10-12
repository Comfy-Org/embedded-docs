# Nano Banana Pro (Google Gemini Image)

Bilder synchron über die Google Vertex AI Gemini API generieren oder bearbeiten. Sie geben einen Text-Prompt an und können optional Referenzbilder oder Gemini-Eingabedateien anhängen. Der Node gibt das generierte Bild und, abhängig vom ausgewählten Antwortmodus, eine Textantwort zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt, der das zu generierende Bild oder die anzuwendenden Bearbeitungen beschreibt. Fügen Sie alle Einschränkungen, Stile oder Details hinzu, die das Modell befolgen soll. Der Prompt muss nach Entfernen von Leerzeichen mindestens ein Zeichen enthalten. | STRING | Ja | N/A |
| `model` | Das Gemini-Modell, das für die Generierung verwendet werden soll. Die Option "Nano Banana 2 (Gemini 3.1 Flash Image)" wird als `gemini-3.1-flash-image` gesendet; "gemini-3-pro-image-preview" wird als `gemini-3-pro-image` gesendet. | COMBO | Ja | "gemini-3-pro-image-preview"<br>"Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Wenn der Seed auf einen bestimmten Wert festgelegt ist, bemüht sich das Modell, bei wiederholten Anfragen dieselbe Antwort zu liefern. Deterministische Ausgabe ist nicht garantiert. Außerdem können Änderungen am Modell oder an Parametereinstellungen wie der Temperatur selbst bei Verwendung desselben Seed-Werts Variationen in der Antwort verursachen. Standardmäßig wird ein zufälliger Seed-Wert verwendet. Standardwert: 42. | INT | Ja | 0 bis 18446744073709551615 |
| `aspect_ratio` | Wenn auf "auto" gesetzt, wird das Seitenverhältnis Ihres Eingabebilds übernommen; wenn kein Bild bereitgestellt wird, wird üblicherweise ein 16:9-Quadrat generiert. Standardwert: "auto". | COMBO | Ja | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Ziel-Ausgabeauflösung. Für 2K/4K wird der native Gemini-Upscaler verwendet. | COMBO | Ja | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Wählen Sie "IMAGE" für eine reine Bildausgabe oder "IMAGE+TEXT", um sowohl das generierte Bild als auch eine Textantwort zurückzugeben. Erweiterte Einstellung. | COMBO | Ja | "IMAGE+TEXT"<br>"IMAGE" |
| `images` | Optionale(s) Referenzbild(er). Um mehrere Bilder einzufügen, verwenden Sie den Batch Images-Node (bis zu 14). | IMAGE | Nein | N/A |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Nein | N/A |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten einer KI vorgeben. Standardwert: ein vordefinierter System-Prompt für die Bildgenerierung. Erweiterte Einstellung. | STRING | Nein | N/A |

**Einschränkungen:**

* Der `images`-Eingang unterstützt maximal 14 Bilder. Wenn mehr bereitgestellt werden, wird ein Fehler ausgelöst.
* Wenn mehr als 10 Bilder bereitgestellt werden, werden die ersten 10 als URL-Referenzen hochgeladen und die übrigen Bilder inline in der Anfrage gesendet.
* Der `files`-Eingang muss mit einem Node verbunden werden, der den Datentyp `GEMINI_INPUT_FILES` ausgibt.
* Wenn `response_modalities` auf `"IMAGE"` gesetzt ist, wird nur das Bild zurückgegeben und die Textausgabe ist leer.
* Der `prompt`-Eingang wird validiert und muss nach Entfernen von Leerzeichen mindestens ein Zeichen enthalten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das vom Gemini-Modell generierte oder bearbeitete Bild. | IMAGE |
| `string` | Die Textantwort des Modells. Diese Ausgabe ist leer, wenn `response_modalities` auf `"IMAGE"` gesetzt ist. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/de.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
