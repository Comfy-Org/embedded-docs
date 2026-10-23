# Ideogram Vector Generate SVG

Dieser Node erzeugt mit Ideogram Vector aus einem Text-Prompt ein bearbeitbares SVG, optional geleitet von bis zu 5 Referenzbildern. Das Ergebnis ist Vektormarkup und kein Rasterbild, daher bleiben die Formen in einem Vektoreditor bearbeitbar.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. Standard: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Ja | `"ideogram-vector-1"` |
| `images` | Optionale Referenzbilder. Bild 1 ist die Hauptquelle, Bilder 2 bis 5 sind zusätzliche Referenzen; erwähnen Sie sie im Prompt als `@Image1`, `@Image2` und so weiter. Eine gebündelte Eingabe zählt pro Bild einmal. | AUTOGROW | Nein | 0 bis 5 Bilder |
| `prompt` | Beschreibung des SVG. Unterstützt Referenzen im Stil von `@Image1` auf die Eingabebilder. | STRING | Ja | 1 bis 9500 Zeichen |
| `aspect_ratio` | `"auto"` folgt Bild 1 oder dem Prompt, wenn kein Bild verbunden ist. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"1:3"`<br>`"1:2"`<br>`"9:16"`<br>`"10:16"`<br>`"2:3"`<br>`"3:4"`<br>`"4:5"`<br>`"1:1"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:10"`<br>`"16:9"`<br>`"2:1"`<br>`"3:1"` |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger. Standard: `"medium"`. | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed für die Generierung. Derselbe Prompt, dieselben Bilder, Einstellungen und derselbe Seed ergeben dasselbe SVG. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:**

* Der Prompt muss zwischen 1 und 9500 Zeichen lang sein.
* `images` akzeptiert höchstens 5 Bilder, gezählt pro Bild, wenn die Eingabe gebündelt ist, und jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben.
* Bilder, deren längste Seite über 2048 Pixel liegt, werden vor dem Hochladen herunterskaliert.
* Das Referenzieren eines nicht verbundenen Bildes, etwa `@Image4` bei nur zwei bereitgestellten Bildern, löst einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `SVG` | Das generierte SVG als bearbeitbares Vektor-Markup. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorGenerateApi/de.md)

---
**Source fingerprint (SHA-256):** `5bd24ad48d6c26daf43f84544a9c22a18961dea645799104591f3785a851f819`
