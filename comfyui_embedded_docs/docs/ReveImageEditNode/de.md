# Reve-Bildbearbeitung

Der Reve Image Edit-Node bearbeitet ein vorhandenes Bild basierend auf einer natürlichsprachigen Textanweisung. Er sendet das Eingabebild und Ihre Anweisung an die Reve-API, die ein neues Bild mit den angeforderten Änderungen zurückgibt.

## Eingaben

Die Auswahl `model` bestimmt, welche modellspezifischen Eingaben angezeigt werden. Die Auswahl `upscale` steuert, ob die Eingabe für den Hochskalierungsfaktor verfügbar ist.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu bearbeitende Bild. | IMAGE | Ja | - |
| `edit_instruction` | Textbeschreibung, wie das Bild bearbeitet werden soll. Maximal 2560 Zeichen. | STRING | Ja | - |
| `model` | Für die Bearbeitung zu verwendende Modellversion. | DYNAMIC_COMBO | Ja | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Das generierte Bild hochskalieren. Kann zusätzliche Kosten verursachen. (Standard: "disabled") | DYNAMIC_COMBO | Nein | `"disabled"`<br>`"enabled"` |
| `remove_background` | Den Hintergrund aus dem generierten Bild entfernen. Kann zusätzliche Kosten verursachen. (Standard: False) | BOOLEAN | Nein | `true`<br>`false` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Nein | 0 bis 2147483647 |

### Modelleingaben (gemeinsam genutzt von `reve-edit@20250915` und `reve-edit-fast@20251030`)

Beide Modellversionen stellen dieselben modellspezifischen Eingaben bereit.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model.aspect_ratio` | Seitenverhältnis des Ausgabebilds. Wenn auf "auto" gesetzt, wird das Seitenverhältnis automatisch bestimmt. | COMBO | Nein | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Erweiterte Option. Höhere Werte erzeugen bessere Bilder, kosten aber mehr Credits. (Standard: 1) | INT | Nein | 1 bis 5 |

### Upscale-Eingaben (wenn `upscale` auf "enabled" gesetzt ist)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | Hochskalierungsfaktor (2x, 3x oder 4x). (Standard: 2) | INT | Nein | 2 bis 4 |

**Hinweis:**

- `upscale.upscale_factor` gilt nur, wenn `upscale` auf "enabled" gesetzt ist. Hochskalierung und Hintergrundentfernung können zusammen oder unabhängig voneinander aktiviert werden.
- `edit_instruction` darf nicht leer sein und darf 2560 Zeichen nicht überschreiten.
- Wenn `model.aspect_ratio` auf "auto" gesetzt ist, wird kein festes Seitenverhältnis an die API gesendet und das Seitenverhältnis automatisch gewählt.
- `model.test_time_scaling` wird nur an die API gesendet, wenn sein Wert größer als 1 ist; der Standardwert 1 behält das Standardverhalten der API bei.
- Die Ergebnisse sind unabhängig vom Seed-Wert nicht deterministisch; der Seed steuert nur, ob der Node erneut ausgeführt wird.
- Dieser Node ist als veraltet gekennzeichnet.
- Ungefähre Kosten in USD (laut Preis-Badge des Nodes): `$0.01001` für `reve-edit-fast@20251030`; `$0.0572` für `reve-edit@20250915` ohne Hochskalierung; `$0.0686` mit 2x-Hochskalierung, `$0.0819` mit 3x-Hochskalierung und `$0.0991` mit 4x-Hochskalierung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das bearbeitete Bild, das basierend auf der Anweisung generiert wurde. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/de.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
