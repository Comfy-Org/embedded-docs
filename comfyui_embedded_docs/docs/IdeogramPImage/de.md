# Ideogram & Pruna P-Image

Ideogram & Pruna P-Image erzeugt Bilder aus einem Textprompt mithilfe von Ideograms schnellem Text-zu-Bild-Modell, das für starke Typografie und Fotorealismus bekannt ist. Es unterstützt außerdem strukturierte JSON-Captions von Ideogram 4.0 für exakte Kontrolle über Textzeichenfolgen, Farben und Layout. Der Node gibt die generierten Bilder zusammen mit dem endgültigen Prompt zurück, aus dem das Bild tatsächlich generiert wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textprompt. Akzeptiert außerdem eine strukturierte JSON-Caption von Ideogram 4.0 (exakte Farben als #RRGGBB-Hex-Werte, exakte Textzeichenfolgen, Bounding-Box-Layout) – setzen Sie `prompt_upsampling` auf OFF, um sie wörtlich zu verwenden. Darf nicht leer sein. (Standard: "") | STRING | Ja | Beliebiger nicht leerer Text |
| `quality` | Geschwindigkeits-/Preis-/Qualitätsstufe. MEDIUM ist der alltägliche Standard; HIGH für komplexe Prompts, feine Details und schwierigen Text; VERY_LOW/LOW für Entwürfe in großem Umfang. Schwieriger Text wird unterhalb von MEDIUM schlecht dargestellt. (Standard: "MEDIUM") | COMBO | Ja | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Ausgabegrößenklasse (die exakten Pixel folgen dem Seitenverhältnis, z. B. ergibt 16:9 1280x720 bei 1K und 2560x1440 bei 2K). Bevorzugen Sie HIGH + 2K für gestochen scharfe Typografie. (Standard: "1K") | COMBO | Ja | "1K"<br>"2K" |
| `aspect_ratio` | Das Seitenverhältnis für die Bilderzeugung. (Standard: "1:1") | COMBO | Ja | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Erweitert kurze Prompts vor der Generierung zu einer detaillierten strukturierten Caption (der umgeschriebene Prompt wird als `final_prompt` zurückgegeben). Auf OFF setzen, wenn Sie Ihre eigene JSON-Caption oder exakten Wortlaut angeben. (Standard: "AUTO") | COMBO | Ja | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Seed für reproduzierbare Generierung. Mit `prompt_upsampling` OFF liefern derselbe Seed und dieselben Einstellungen dasselbe Bild; bei ON/AUTO variiert das Umschreiben des Prompts pro Lauf – reproduzieren Sie ein Ergebnis, indem Sie dessen `final_prompt`-Ausgabe mit `prompt_upsampling` OFF und demselben Seed wiederverwenden. (Standard: 42) | INT | Nein | 0 bis 2147483647 |

**Hinweis zu Einschränkungen:** Der Prompt muss mindestens ein Zeichen enthalten, das kein Leerraum ist, andernfalls schlägt der Node fehl. Setzen Sie `prompt_upsampling` auf OFF, wenn Sie Ihre eigene strukturierte JSON-Caption oder exakten Wortlaut angeben. Wenn `prompt_upsampling` ON oder AUTO ist, wird der Prompt vor der Generierung umgeschrieben, sodass derselbe Seed möglicherweise nicht dasselbe Bild reproduziert; um ein Bild zu reproduzieren, verwenden Sie dessen `final_prompt`-Ausgabe erneut mit `prompt_upsampling` OFF und demselben Seed.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das/die generierten Bild(er), zurückgegeben als Stapel von Bildern. Wenn Ideograms Inhaltssicherheitsfilter die Generierung blockiert, wird stattdessen ein Fehler ausgelöst. | IMAGE |
| `final_prompt` | Der Prompt, aus dem das Bild tatsächlich generiert wurde (die umgeschriebene strukturierte Caption, wenn `prompt_upsampling` ausgeführt wurde, andernfalls Ihr Prompt). Geben Sie ihn mit `prompt_upsampling` OFF und demselben Seed erneut ein, um dieses Bild zu reproduzieren. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/de.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`
