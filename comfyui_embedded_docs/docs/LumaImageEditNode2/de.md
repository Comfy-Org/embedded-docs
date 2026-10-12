# Luma UNI-1 Image Edit

Dieser Node bearbeitet ein vorhandenes Bild mithilfe eines Text-Prompts, unterstützt durch das Luma UNI-1-Modell. Er nimmt ein Quellbild und eine Beschreibung der gewünschten Änderung entgegen und erzeugt anschließend eine neue bearbeitete Version des Bildes. Sie können zwischen den Modellen `uni-1` und `uni-1-max` wählen, den Stil anpassen, die Websuche aktivieren und optional bis zu 8 Referenzbilder bereitstellen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das für die Bearbeitung verwendet wird. Bei Auswahl eines Modells werden die modellspezifischen Optionen unten eingeblendet. | DYNAMIC_COMBO | Ja | `"uni-1"`<br>`"uni-1-max"` |
| `source` | Quellbild, das bearbeitet werden soll. | IMAGE | Ja | - |
| `prompt` | Beschreibung der gewünschten Bearbeitung. 1–6000 Zeichen. Standard: "" (leere Zeichenkette; die Anfrage ist ungültig, bis mindestens ein Zeichen eingegeben wurde). | STRING | Ja | 1 bis 6000 Zeichen |
| `seed` | `seed` steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 0. | INT | Ja | 0 bis 2147483647 |

### uni-1 und uni-1-max Eingaben

Diese Optionen werden von beiden Modellen `uni-1` und `uni-1-max` gemeinsam verwendet.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `style` | Stilvoreinstellung. `"auto"` wählt anhand des Prompts aus; `"manga"` wendet eine Manga-/Anime-Ästhetik an und erfordert ein Hochformat (2:3, 9:16, 1:2, 1:3). Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"manga"` |
| `web_search` | Durchsucht vor der Generierung das Web nach visuellen Referenzen. Standard: false. | BOOLEAN | Ja | `true`<br>`false` |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image_ref` | Erweiterbarer Slot: Verbinden Sie bis zu 8 Referenzbilder (`image_1` bis `image_8`) zur Stil-/Inhaltssteuerung. Optional. | IMAGE | Nein | 0 bis 8 Bilder |

**Hinweise:**
- Der `prompt` muss zwischen 1 und 6000 Zeichen lang sein.
- Die Eingaben `style`, `web_search` und `image_ref` erscheinen, wenn `model` auf `"uni-1"` oder `"uni-1-max"` gesetzt ist.
- Beide Modelle unterstützen dieselben modellspezifischen Optionen, einschließlich bis zu 8 Referenzbildern.
- Der Stil `"manga"` erfordert ein Hochformat (2:3, 9:16, 1:2 oder 1:3).
- Das Verbinden von mehr als 8 Referenzbildern führt zu einem Fehler.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das vom Luma UNI-1-Modell generierte bearbeitete Bild, zurückgegeben im PNG-Format. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/de.md)

---
**Source fingerprint (SHA-256):** `66f62bb2807759edb405c2caeeefe32c341920924e267c32449a620190b9a7ab`
