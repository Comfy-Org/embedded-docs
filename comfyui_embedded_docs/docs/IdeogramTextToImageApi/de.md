# Ideogram 4.5 Text zu Bild

Erzeugen Sie Bilder aus einem Text-Prompt mit Ideogram 4.5. Der Prompt akzeptiert außerdem eine strukturierte JSON-Bildbeschriftung von Ideogram, zum Beispiel den `final_prompt`, der von einem früheren Durchlauf zurückgegeben wurde, wodurch Sie exakte Kontrolle über Textzeichenfolgen, Farben und Layout erhalten. Der Node gibt das/die generierte(n) Bild(er) zusammen mit der Bildbeschriftung zurück, aus der das Bild tatsächlich generiert wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. (Standard: `"ideogram-4.5"`) | DYNAMIC_COMBO | Ja | `"ideogram-4.5"` |
| `prompt` | Text-Prompt oder eine strukturierte JSON-Bildbeschriftung von Ideogram wie ein vorheriger `final_prompt`. (Standard: leerer String) | STRING | Ja | 1 bis 10000 Zeichen |
| `size` | Ausgabegröße. `"auto"` lässt das Modell eine Leinwand wählen, die zum Prompt passt. Eine Voreinstellung `(2K)` oder `(1K)` legt sowohl die Pixelgröße als auch das Seitenverhältnis fest. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger. (Standard: `"medium"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `magic_prompt` | Schreibt den Prompt vor der Generierung in eine detaillierte strukturierte Bildbeschriftung um; `"off"` behält Ihre Formulierung so wörtlich wie möglich bei. Die Beschriftung wird als `final_prompt` zurückgegeben. (Standard: `"auto"`) Dies ist eine erweiterte Einstellung. | COMBO | Ja | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Seed für die Generierung. Text-zu-Bild ist allein anhand des Seeds nicht reproduzierbar, da der Prompt bei jedem Durchlauf neu geschrieben wird; um ein Bild zu reproduzieren, verwenden Sie dessen `final_prompt` mit `magic_prompt` auf `"off"` und demselben Seed erneut. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Parametereinschränkungen

- **Prompt erforderlich:** Der Prompt muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist, und höchstens 10000 Zeichen. Setzen Sie `magic_prompt` auf `"off"`, wenn Sie Ihre eigene JSON-Bildbeschriftung oder eine exakte Formulierung angeben.
- **Größe:** `"auto"` lässt das Modell wählen. `(2K)`-Voreinstellungen umfassen etwa 3 bis 4 Megapixel und `(1K)`-Voreinstellungen etwa 1 Megapixel, daher beschreibt die Stufenbezeichnung das Pixelbudget statt einer festen langen Seite; das Seitenverhältnis der Voreinstellung wird beibehalten. Nur der Pixelgrößen-Teil der Voreinstellung wird an die API gesendet.
- **Reproduzierbarkeit:** Wenn `magic_prompt` auf `"auto"` oder `"on"` gesetzt ist, wird der Prompt bei jedem Durchlauf neu geschrieben, sodass derselbe Seed dennoch ein anderes Bild erzeugen kann. Um ein Bild zu reproduzieren, geben Sie dessen `final_prompt` mit `magic_prompt` auf `"off"` und demselben Seed erneut ein.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram die Generierung blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das/die generierte(n) Bild(er) als Batch. | IMAGE |
| `final_prompt` | Die strukturierte Bildbeschriftung, aus der das Bild generiert wurde. Geben Sie sie mit `magic_prompt` auf `"off"` und demselben Seed erneut ein, um das Bild zu reproduzieren. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/de.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
