# Kling 3.0 Omni Image

Der Node Kling Omni Image (Pro) erstellt oder bearbeitet Bilder mit dem neuesten Kling AI-Modell. Er generiert Bilder basierend auf einer Textbeschreibung und kann optional Referenzbilder verwenden, um Stil oder Inhalt zu steuern. Der Node sendet eine Anfrage an eine externe API, die die Aufgabe verarbeitet und das/die finale(n) Bild(er) zurückgibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Das spezifische Kling AI-Modell, das für die Bilderzeugung verwendet werden soll. | COMBO | Ja | `"kling-v3-omni"`<br>`"kling-image-o1"` |
| `prompt` | Ein Text-Prompt, der den Bildinhalt beschreibt. Er kann sowohl positive als auch negative Beschreibungen enthalten. Der Text muss zwischen 1 und 2500 Zeichen lang sein. Sie können `@image`, `@image1`, `@image2` usw. oder `@video`, `@video1`, `@video2` usw. verwenden, um im Prompt auf hochgeladene Bilder oder Videos zu verweisen. | STRING | Ja | - |
| `resolution` | Die Zielauflösung für das generierte Bild. Hinweis: Die 4K-Auflösung wird für das Modell `kling-image-o1` nicht unterstützt. | COMBO | Ja | `"1K"`<br>`"2K"`<br>`"4K"` |
| `aspect_ratio` | Das gewünschte Seitenverhältnis (Breite zu Höhe) für das generierte Bild. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` |
| `series_amount` | Eine Bildserie generieren. Diese Funktion wird für das Modell `kling-image-o1` nicht unterstützt. (Standard: "disabled") | COMBO | Ja | `"disabled"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |
| `reference_images` | Bis zu 10 zusätzliche Referenzbilder. Jedes Bild muss mindestens 300 Pixel in Breite und Höhe haben, und sein Seitenverhältnis muss zwischen 1:2,5 und 2,5:1 liegen. | IMAGE | Nein | - |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Nein | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das/die finale(n) Bild(er), das/die vom Kling AI-Modell generiert oder bearbeitet wurde(n). Wenn eine Serie angefordert wurde, werden mehrere Bilder als Batch zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/de.md)

---
**Source fingerprint (SHA-256):** `923db96e956e0f11c9290478ceb105304893f28d35af9f0e13077ca0f88dff79`
