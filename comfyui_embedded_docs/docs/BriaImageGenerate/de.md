# Bria FIBO 2.0 Image Generate

Erzeugt ein neues Bild aus einem Text-Prompt, einem strukturierten JSON-Prompt oder einem einzelnen Referenzbild mit Bria FIBO 2.0. Der Node sendet die Anfrage an die Bria API, wartet, bis die Generierung abgeschlossen ist, und gibt das Bild zusammen mit einem strukturierten Prompt zurück, mit dem es in einem späteren Lauf neu erzeugt oder verfeinert werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Einfache sprachliche Beschreibung des zu erzeugenden Bildes (Standard: leer). | STRING | Ja | Mehrzeiliger Text |
| `structured_prompt` | JSON-strukturierter Prompt aus einem früheren Bria-FIBO-Ergebnis. Mit demselben Seed wird dieses Bild neu erzeugt; ändern Sie das JSON oder fügen Sie einen Prompt hinzu, um es zu verfeinern (Standard: leer). | STRING | Ja | Mehrzeiliger Text |
| `aspect_ratio` | Seitenverhältnis der Ausgabe (Standard: `"1:1"`). Die Verhältnisse ab `"16:10"` sind FIBO-2.0-Größen mit zusätzlichen Anforderungen, die unten aufgeführt sind. | COMBO | Ja | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"16:10"`<br>`"10:16"`<br>`"2:1"`<br>`"1:2"`<br>`"21:9"`<br>`"9:21"`<br>`"3:1"`<br>`"1:3"`<br>`"4:1"`<br>`"1:4"`<br>`"5:1"`<br>`"1:5"` |
| `resolution` | Auflösung der Ausgabe in Megapixeln (Standard: `"1MP"`). | COMBO | Ja | `"1MP"`<br>`"4MP"` |
| `seed` | Seed, der die Generierung initialisiert (Standard: 42). | INT | Ja | 1 bis 2147483647 |
| `moderation` | Moderationseinstellungen. Die Auswahl von `"true"` blendet die unten aufgeführten Moderationseingaben ein. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |
| `image` | Optionales Referenzbild, auf das aufgebaut werden soll. Das Ergebnis ist ein neues Bild im ausgewählten Seitenverhältnis, keine Bearbeitung dieses Bildes. | IMAGE | Nein | - |

### Moderationseingaben

Wenn `moderation` auf `"true"` gesetzt ist, werden diese zusätzlichen Eingaben verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Gibt an, ob der Prompt-Text moderiert wird; die Anfrage schlägt fehl, wenn die Moderation ihn ablehnt (Standard: false). | BOOLEAN | Nein | `true`<br>`false` |
| `visual_input_moderation` | Gibt an, ob das Referenzbild moderiert wird; die Anfrage schlägt fehl, wenn die Moderation es ablehnt (Standard: false). | BOOLEAN | Nein | `true`<br>`false` |
| `visual_output_moderation` | Gibt an, ob das erzeugte Bild moderiert wird; die Anfrage schlägt fehl, wenn die Moderation es ablehnt (Standard: false). | BOOLEAN | Nein | `true`<br>`false` |

**Wichtige Einschränkungen:**

- Geben Sie mindestens eines von `prompt`, `structured_prompt` oder einem Referenz-`image` an. Wenn alle drei leer sind, löst der Node einen Fehler aus.
- Ein Referenzbild kann nicht mit `structured_prompt` kombiniert werden: Verwenden Sie entweder das eine oder das andere.
- Die FIBO-2.0-Verhältnisse (`"16:10"`, `"10:16"`, `"2:1"`, `"1:2"`, `"21:9"`, `"9:21"`, `"3:1"`, `"1:3"`, `"4:1"`, `"1:4"`, `"5:1"`, `"1:5"`) erfordern `resolution` `"1MP"` und genau eines von `prompt` oder `structured_prompt`.
- Dieser Node ist ein kostenpflichtiger API-Node; jeder Lauf kostet ungefähr 0,0572 USD.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das von der Bria API zurückgegebene erzeugte Bild. | IMAGE |
| `structured_prompt` | Strukturierte Beschreibung des erzeugten Bildes, um es mit diesem Node neu zu erzeugen oder zu verfeinern. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageGenerate/de.md)

---
**Source fingerprint (SHA-256):** `4d53fe457e2e349ac41b5c8a0d3d5599eafa53cb653c470335853f1d4517688f`
