# Krea 3 Image

Krea 3 Image bearbeitet Bilder mit Krea 3 oder generiert ein neues Bild aus einem Text-Prompt, wenn kein Bild verbunden ist. Verbinden Sie bis zu 8 Bilder und beschreiben Sie, was geändert werden soll und was erhalten bleiben soll, wobei Sie im Prompt als @Image1, @Image2 usw. auf sie verweisen. Das Seitenverhältnis und die Auflösung legen die Ausgabegröße fest, und der Denkmodus opfert Geschwindigkeit für einen detaillierteren Plan.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zu verwendende Krea 3-Modell. Die Auswahl eines Modells zeigt die Parameter an, die es akzeptiert. | DYNAMIC_COMBO | Ja | `"Krea 3"` |

### Krea 3 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `Krea 3` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.images` | Die zu bearbeitenden Bilder, nummeriert in Verbindungsreihenfolge. Jedes verbundene Bild zählt zum Limit von 8. Leer lassen, um nur aus Text zu generieren. | IMAGE | Nein | 0 bis 8 Bilder |
| `model.prompt` | Was geändert werden soll und was erhalten bleiben soll. Verweisen Sie auf die Bilder als `@Image1`, `@Image2` usw. oder als Bild 1, Bild 2, ... Der Prompt darf nicht leer sein. | STRING | Ja | - |
| `model.aspect_ratio` | Das Seitenverhältnis des Ergebnisses. `"auto"` folgt dem ersten Bild oder dem Prompt, wenn kein Bild verbunden ist. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `model.resolution` | Die Ausgabeauflösung. `"2K"` dauert länger und erzeugt ein größeres Bild als `"1K"`. (Standard: `"2K"`) | COMBO | Ja | `"1K"`<br>`"2K"` |
| `model.thinking_mode` | Wie viel Arbeit Krea 3 in die Planung der Bearbeitung investiert. `"fast"` wird empfohlen, während `"high"` komplexe Bearbeitungen detaillierter plant und länger dauert. `"ultra"` erzeugt mehrere Kandidaten und liefert den besten; es braucht mindestens ein Bild, gibt immer 2K aus und unterstützt `precise_edit` nicht. (Standard: `"fast"`) | COMBO | Ja | `"fast"`<br>`"high"`<br>`"ultra"` |
| `model.precise_edit` | Alles außerhalb des bearbeiteten Bereichs unverändert lassen. Erfordert mindestens ein verbundenes Bild. (Standard: False) | BOOLEAN | Ja | false<br>true |
| `model.seed` | Der Seed für die Anfrage (Standard: 42). Krea schreibt den Prompt vor der Generierung um, daher führt derselbe Seed nicht zum selben Bild. | INT | Ja | 0 bis 2147483647 |

Eine Referenz wie `@Image3` wird nur akzeptiert, wenn mindestens drei Bilder verbunden sind, andernfalls löst der Node einen Fehler aus. Referenzbilder werden hochgeladen, bevor die Anfrage gesendet wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das generierte oder bearbeitete Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea3ImageNode/de.md)

---
**Source fingerprint (SHA-256):** `9e8d036f1ebca81b85e6ef42a015e7e2925bf467fa32e82180ee1b76dcc91c0b`
