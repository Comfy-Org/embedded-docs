# ByteDanceSeedNode

Generieren Sie Textantworten mit den Seed 2.0-Modellen von ByteDance. Geben Sie einen Text-Prompt an und verbinden Sie optional Bilder oder Videos, um dem Modell zusätzlichen Kontext zu geben. Das Modell wird aus den verfügbaren Seed 2.0-Varianten ausgewählt, und der Node gibt die Textantwort des Modells zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Texteingabe für das Modell. (Standard: "") | STRING | Ja | N/A |
| `model` | Das Seed-Modell, das zur Generierung der Antwort verwendet wird. Diese Auswahl legt auch die Unterparameter des Modells offen. | DYNAMIC_COMBO | Ja | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells bestimmen. (Standard: "") | STRING | Nein | N/A |

### Modelleingaben (gemeinsam genutzt von Seed 2.0 Pro, Seed 2.0 Lite und Seed 2.0 Mini)

Alle drei Seed-Modelle legen bei Auswahl dieselben Unterparameter offen.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `temperature` | Steuert die Zufälligkeit. 0.0 ist deterministisch, höhere Werte sind zufälliger. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 2.0 (Schritt: 0.01) |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `images` | Optionale(s) Bild(er), die als Kontext für das Modell verwendet werden. Bis zu 20 Bilder. Erweiterbarer Slot: Verbinden Sie 1..20 Elemente, z. B. `image_1` bis `image_20`. | IMAGE | Nein | 0 bis 20 Bilder |
| `videos` | Optionale(s) Video(s), die als Kontext für das Modell verwendet werden. Bis zu 4 Videos. Erweiterbarer Slot: Verbinden Sie 1..4 Elemente, z. B. `video_1` bis `video_4`. | VIDEO | Nein | 0 bis 4 Videos |

**Hinweis:** Der Parameter `model` ist eine dynamische Kombination, die die Unterparameter für Referenz und Temperatur offenlegt, sobald ein Modell ausgewählt wurde. Die Slots `images` und `videos` sind erweiterbar, sodass Sie mehrere Eingaben für multimodalen Kontext verbinden können.

- `prompt` ist erforderlich und muss mindestens ein Nicht-Leerzeichen-Zeichen enthalten; andernfalls wird ein Fehler ausgelöst.
- Pro Anfrage werden maximal 20 Bilder unterstützt. Dieses Limit zählt alle Bilder über verbundene Batches hinweg.
- Pro Anfrage werden maximal 4 Videos unterstützt.
- Es wird ein Fehler ausgelöst, wenn das Modell eine leere Antwort zurückgibt oder die Antwort verweigert (der Verweigerungstext wird gemeldet).

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `output` | Die generierte Textantwort vom Seed-Modell. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/de.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
