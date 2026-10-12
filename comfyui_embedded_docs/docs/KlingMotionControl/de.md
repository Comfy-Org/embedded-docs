# Kling Bewegungssteuerung

Der Kling Motion Control-Node erzeugt ein Video, indem er Bewegung, Gesichtsausdrücke und Kamerabewegungen aus einem Referenzvideo auf einen Charakter anwendet, der durch ein Referenzbild und einen Text-Prompt definiert wird. Er ermöglicht Ihnen zu steuern, ob die endgültige Ausrichtung des Charakters aus dem Referenzvideo oder dem Referenzbild stammt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Eine Textbeschreibung des gewünschten Videos. Die maximale Länge beträgt 2500 Zeichen. | STRING | Ja | N/A |
| `reference_image` | Ein Bild des zu animierenden Charakters. Die Mindestabmessungen betragen 340x340 Pixel. Das Seitenverhältnis muss zwischen 1:2.5 und 2.5:1 liegen. | IMAGE | Ja | N/A |
| `reference_video` | Bewegungsreferenzvideo, das verwendet wird, um Bewegung/Gesichtsausdruck zu steuern. Die Dauerbegrenzungen hängen von der Einstellung `character_orientation` ab. Die Mindestabmessungen betragen 340x340 Pixel, die maximalen Abmessungen 3850x3850 Pixel. | VIDEO | Ja | N/A |
| `keep_original_sound` | Legt fest, ob das Original-Audio aus dem Referenzvideo in der Ausgabe beibehalten wird. Standard ist `True`. | BOOLEAN | Nein | N/A |
| `character_orientation` | Steuert, woher die Ausrichtung/Orientierung des Charakters stammt. `"video"`: Bewegungen, Gesichtsausdrücke, Kamerabewegungen und Ausrichtung folgen dem Bewegungsreferenzvideo (weitere Details über den Prompt). `"image"`: Bewegungen und Gesichtsausdrücke folgen weiterhin dem Bewegungsreferenzvideo, aber die Ausrichtung des Charakters entspricht dem Referenzbild (Kamera/weitere Details über den Prompt). | COMBO | Nein | `"video"`<br>`"image"` |
| `mode` | Der zu verwendende Generierungsmodus. | COMBO | Nein | `"pro"`<br>`"std"` |
| `model` | Die zu verwendende Kling-Modellversion. Standard ist `"kling-v2-6"`. | COMBO | Nein | `"kling-v3"`<br>`"kling-v2-6"` |

**Einschränkungen:**

- Die Dauer des `reference_video` muss zwischen 3 und 30 Sekunden liegen, wenn `character_orientation` auf `"video"` gesetzt ist.
- Die Dauer des `reference_video` muss zwischen 3 und 10 Sekunden liegen, wenn `character_orientation` auf `"image"` gesetzt ist.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video mit dem Charakter, der die Bewegung aus dem Referenzvideo ausführt. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/de.md)

---
**Source fingerprint (SHA-256):** `a61e55fabe53f4e13fa993c3d891db40024709ea4fb6b16b5716d893b2bd23b5`
