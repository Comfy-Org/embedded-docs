# MetaMuseImageEditApi

Bearbeitet oder kombiniert bis zu 10 Referenzbilder mithilfe eines Text-Prompts und Metas Muse Image-Modell. Beschreiben Sie die gewünschte Bearbeitung im Prompt und verweisen Sie bei Bedarf auf die Referenzbilder als `@Image1`, `@Image2` usw. Der Node lädt die Referenzbilder hoch, ruft die Meta Muse Image API auf und gibt das bearbeitete Ergebnis als Bild zurück.

## Eingaben

Der Node wird über einen `model`-Selektor gesteuert. Die unten beschriebenen modellspezifischen Eingaben erscheinen, wenn ein Modell ausgewählt wird, und die von Ihnen verbundenen Referenzbilder können nach Bedarf erweitert oder verkürzt werden.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das verwendet werden soll. | DYNAMIC_COMBO | Ja | "muse-image-1.0" |

### muse-image-1.0 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Bearbeitungsanweisungen. Unterstützt `@Image1`-style Referenzen auf die Eingabebilder. Standard: leerer String. Der Prompt muss mindestens ein Zeichen enthalten. | STRING | Ja | Beliebiger Text mit einer Mindestlänge von 1 Zeichen |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. Bilder werden mit etwa 2,5 Megapixeln gerendert (1:1 ist 1600x1600, 16:9 ist 2048x1152); "auto" behält das Seitenverhältnis der Eingabe bei. | COMBO | Ja | "auto"<br>"1:1"<br>"3:2"<br>"2:3"<br>"4:3"<br>"3:4"<br>"5:4"<br>"4:5"<br>"16:9"<br>"9:16"<br>"21:9"<br>"9:21"<br>"2:1"<br>"1:2" |
| `reasoning_strength` | Wie stark das Modell nachdenkt, plant und sich vor dem Rendern selbst verfeinert. | COMBO | Ja | "high"<br>"low" |
| `enable_web_search` | Ermöglicht dem Modell, während der Bildplanung im Web nach Fakten und aktuellen Informationen zu suchen. Standard: true. | BOOLEAN | Ja | true oder false (Standard: true) |
| `enable_image_search` | Ermöglicht dem Modell, während der Bildplanung nach Referenzbildern zu suchen. Standard: true. | BOOLEAN | Ja | true oder false (Standard: true) |
| `enable_shell` | Ermöglicht dem Modell, während der Planung Code auszuführen, z. B. für präzise Layouts, Diagramme und Schaubilder; wenn deaktiviert, werden Mengen und Ausrichtung angenähert. Standard: true. | BOOLEAN | Ja | true oder false (Standard: true) |
| `seed` | Seed, um zu bestimmen, ob der Node erneut ausgeführt werden soll; die API hat keinen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 (Schritt 1) |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Erweiterbarer Slot: Verbinden Sie 1 bis 10 Referenzbilder (`image_1` bis `image_10`) zum Bearbeiten oder Kombinieren. Verweisen Sie im Prompt als `@Image1`, `@Image2`, ..., nummeriert in Eingabereihenfolge, darauf; eine gebündelte Eingabe zählt pro Bild einmal. | IMAGE | Ja | 1 bis 10 Referenzbilder |

Hinweis: Der Prompt darf nicht leer sein, und jede darin enthaltene `@ImageN`-Referenz muss mit einem der verbundenen Bilder in Eingabereihenfolge übereinstimmen (zum Beispiel ist `@Image1` das erste verbundene Referenzbild). Wenn der Prompt auf eine Bildnummer verweist, die nicht verbunden ist, oder wenn mehr als 10 Referenzbilder verbunden sind, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das vom Muse Image-Modell zurückgegebene bearbeitete oder kombinierte Bild. Wenn die API mehrere Bilder zurückgibt, werden sie als Batch zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageEditApi/de.md)

---
**Source fingerprint (SHA-256):** `5c009ca45199f9c70465f12d48a46b685abebd0194c3d437121b9df0636dbea7`
