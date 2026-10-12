# Nano Banana 2

Der Node Nano Banana 2 erzeugt oder bearbeitet Bilder synchron über die Google Vertex API unter Verwendung des Modells Gemini 3.1 Flash Image. Er sendet einen Text-Prompt zusammen mit optionalen Referenzbildern oder Dateien und gibt das generierte Bild, etwaigen begleitenden Text und optional ein Bild aus dem Denkprozess des Modells zurück. Dieser Node ist als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt, der das zu generierende Bild oder die anzuwendenden Bearbeitungen beschreibt. Geben Sie alle Einschränkungen, Stile oder Details an, die das Modell befolgen soll. Darf nicht leer sein oder nur aus Leerzeichen bestehen. (Standard: leer) | STRING | Ja | N/A |
| `model` | Das Gemini-Modell, das für die Bilderzeugung verwendet werden soll. | COMBO | Ja | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Wenn der Seed auf einen bestimmten Wert festgelegt ist, bemüht sich das Modell nach besten Kräften, bei wiederholten Anfragen die gleiche Antwort zu liefern. Eine deterministische Ausgabe ist nicht garantiert. Außerdem können Änderungen am Modell oder an Parametereinstellungen wie der Temperatur selbst bei Verwendung desselben Seed-Werts zu Abweichungen in der Antwort führen. Standardmäßig wird ein zufälliger Seed-Wert verwendet. (Standard: 42) | INT | Ja | 0 bis 18446744073709551615 |
| `aspect_ratio` | Wenn auf 'auto' gesetzt, wird das Seitenverhältnis Ihres Eingabebilds übernommen; wenn kein Bild bereitgestellt wird, wird üblicherweise ein Bild im Format 16:9 erzeugt. (Standard: "auto") | COMBO | Ja | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Zielauflösung der Ausgabe. Für 2K/4K wird der native Gemini-Upscaler verwendet. | COMBO | Ja | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Bestimmt die Art des Inhalts, den das Modell zurückgibt: "IMAGE" gibt nur ein Bild zurück, "IMAGE+TEXT" gibt zusätzlich Text zurück. (erweitert) | COMBO | Ja | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | Steuert die Tiefe des Denkprozesses des Modells. | COMBO | Ja | "MINIMAL"<br>"HIGH" |
| `images` | Optionale Referenzbilder. Um mehrere Bilder einzubinden, verwenden Sie den Node Batch Images (bis zu 14). | IMAGE | Nein | 1 bis 14 Bilder |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node Gemini Generate Content Input Files. | CUSTOM | Nein | N/A |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten einer KI bestimmen. (Standard: ein voreingestellter Prompt, der das Modell anweist, immer ein Bild zu erzeugen) (erweitert) | STRING | Nein | N/A |

**Hinweis:** Die Eingabe `images` unterstützt maximal 14 Bilder. Wenn mehr bereitgestellt werden, löst der Node einen Fehler aus. Die Eingabe `prompt` darf nicht leer sein oder nur aus Leerzeichen bestehen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das primäre Bild, das vom Modell generiert oder bearbeitet wurde. | IMAGE |
| `string` | Jeglicher Textinhalt, der vom Modell zurückgegeben wird. | STRING |
| `thought_image` | Erstes Bild aus dem Denkprozess des Modells. Nur verfügbar, wenn `thinking_level` auf HIGH gesetzt ist und die Modalität IMAGE+TEXT verwendet wird. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/de.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
