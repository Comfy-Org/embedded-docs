# Pad Image

Füllt ein Bild mit einer Volltonfarbe oder einer gespiegelten Kopie seiner Ränder auf. Das Auffüllen kann als exakte Pixelanzahl auf jeder Seite, als Größenmultiplikator oder als kleinste Menge festgelegt werden, die Breite und Höhe durch eine Zahl teilbar macht, was vor dem Speichern oder Kacheln praktisch ist. Das Originalbild behält seinen Platz: `left`- und `top`-Padding wird davor hinzugefügt, `right`- und `bottom`-Padding danach.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das aufzufüllende Bild. | IMAGE | Ja | - |
| `padding_type` | Wie viel Padding hinzugefügt wird: `"pad dimensions"` für exakte Pixelwerte pro Seite, `"pad by multiplier"` für eine Ausgabegröße relativ zur Eingabe oder `"pad to multiple"`, um das nächste Vielfache zu erreichen. Beim Auswählen einer Option werden ihre Parameter eingeblendet. | DYNAMIC_COMBO | Ja | `"pad dimensions"`<br>`"pad by multiplier"`<br>`"pad to multiple"` |
| `left` | Pixel, die links hinzugefügt werden. Verfügbar, wenn `padding_type` `"pad dimensions"` ist (Standard: 0). | INT | Ja | 0 bis 16384 |
| `top` | Pixel, die oben hinzugefügt werden. Verfügbar, wenn `padding_type` `"pad dimensions"` ist (Standard: 0). | INT | Ja | 0 bis 16384 |
| `right` | Pixel, die rechts hinzugefügt werden. Verfügbar, wenn `padding_type` `"pad dimensions"` ist (Standard: 0). | INT | Ja | 0 bis 16384 |
| `bottom` | Pixel, die unten hinzugefügt werden. Verfügbar, wenn `padding_type` `"pad dimensions"` ist (Standard: 0). | INT | Ja | 0 bis 16384 |
| `multiplier` | Ausgabegröße relativ zur Eingabe; beispielsweise fügt 1.5 auf jeder Seite 25 % hinzu. Das Padding wird gleichmäßig auf gegenüberliegende Seiten verteilt. Verfügbar, wenn `padding_type` `"pad by multiplier"` ist (Standard: 1.0). | FLOAT | Ja | 1.0 bis 8.0 (Schritt 0.01) |
| `multiple` | Füllt so auf, dass Breite und Höhe durch diese Zahl teilbar sind. Das Padding wird gleichmäßig auf gegenüberliegende Seiten verteilt, wobei das zusätzliche Pixel rechts und unten landet. Verfügbar, wenn `padding_type` `"pad to multiple"` ist (Standard: 32). | INT | Ja | 1 bis 16384 |
| `padding_style` | Womit der aufgefüllte Bereich gefüllt wird: `"color"` oder `"mirror image"`. Beim Auswählen einer Option werden ihre Parameter eingeblendet. | DYNAMIC_COMBO | Ja | `"color"`<br>`"mirror image"` |
| `color` | Füllfarbe für den aufgefüllten Bereich; Alpha wird ignoriert. Verfügbar, wenn `padding_style` `"color"` ist (Standard: `"#000000"`). | COLOR | Ja | - |
| `feathering` | So viele Pixel des Bildrandes auf den aufgefüllten Seiten mit der Füllfarbe verblenden. 0 hinterlässt eine harte Kante. Verfügbar, wenn `padding_style` `"color"` ist (Standard: 0). | INT | Ja | 0 bis 16384 |

`"mirror image"` spiegelt die Bildränder, anstatt sie mit einer Farbe zu füllen. Das Randpixel wird nicht wiederholt, und wenn das Padding breiter oder höher als das Bild selbst ist, wiederholt sich das gespiegelte Bild, um den Rest abzudecken. Wenn sich für jede Padding-Menge 0 ergibt, wird das Eingabebild unverändert zurückgegeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das aufgefüllte Bild mit der Batch-Dimension und Kanalanzahl der Eingabe. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PadImageNode/de.md)

---
**Source fingerprint (SHA-256):** `9373cd6aa287befba74374b9b2a6c38b20344b5715e9aaa4cf49282ae930c91d`
