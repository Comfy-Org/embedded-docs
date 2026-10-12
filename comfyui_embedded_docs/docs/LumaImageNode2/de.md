# Luma UNI-1 Image

Dieser Node erzeugt Bilder aus Textbeschreibungen mithilfe des Luma UNI-1-Modells. Er nimmt einen Text-Prompt und optionale Einstellungen wie Seitenverhältnis und Stil entgegen und sendet dann die Anfrage an die Luma-API, um ein Bild zu erzeugen. Es sind zwei Modellvarianten verfügbar: `uni-1` und `uni-1-max`.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Textbeschreibung des gewünschten Bildes. 1–6000 Zeichen. (Standard: "") | STRING | Ja | 1 to 6000 characters |
| `model` | Das für die Generierung zu verwendende Modell. Die Auswahl eines Modells blendet zusätzliche Einstellungen für dieses Modell ein. (Standard: erste Option, `"uni-1"`) | DYNAMIC_COMBO | Ja | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 to 2147483647 |

### uni-1 und uni-1-max Eingaben

Gemeinsam genutzt von den Modelloptionen `uni-1` und `uni-1-max`. Diese Einstellungen werden angezeigt, wenn eines der beiden Modelle ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Seitenverhältnis des Ausgabebilds. `"auto"` lässt das Modell anhand des Prompts auswählen. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Stilvoreinstellung. `"auto"` wählt anhand des Prompts aus; `"manga"` wendet eine Manga-/Anime-Ästhetik an und erfordert ein Hochformat-Seitenverhältnis (2:3, 9:16, 1:2, 1:3). (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"manga"` |
| `web_search` | Durchsucht vor der Generierung das Web nach visuellen Referenzen. (Standard: False) | BOOLEAN | Ja | True / False |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image_ref` | Erweiterbarer Slot: Verbinden Sie 1 bis 9 Elemente (z. B. `image_1` bis `image_9`). Bis zu 9 Referenzbilder zur Stil-/Inhaltssteuerung. | IMAGE | Nein | Bis zu 9 Bilder |

**Hinweis:** Wenn `style` auf `"manga"` gesetzt ist, muss `aspect_ratio` entweder `"auto"` oder eines der Hochformat-Seitenverhältnisse `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"` sein. Die Verwendung eines anderen Seitenverhältnisses mit dem Stil `"manga"` verursacht einen Fehler. Die maximale Anzahl an Referenzbildern beträgt 9 sowohl für `uni-1` als auch für `uni-1-max`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das generierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/de.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`
