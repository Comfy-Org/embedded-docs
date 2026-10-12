# CLIP-Textkodierung (SD3)

CLIPTextEncodeSD3 verarbeitet Texteingaben für Stable Diffusion 3-Modelle, indem es mehrere Text-Prompts mit verschiedenen CLIP-Modellen kodiert. Der Node verarbeitet drei separate Texteingaben (`clip_g`, `clip_l` und `t5xxl`) und bietet Optionen zur Verwaltung von leerem Text-Padding. Der Node stellt die korrekte Token-Ausrichtung zwischen den verschiedenen Texteingaben sicher und gibt Conditioning-Daten zurück, die für SD3-Generierungspipelines geeignet sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das für die Textkodierung verwendete CLIP-Modell | CLIP | Ja | - |
| `clip_l` | Texteingabe für das lokale CLIP-Modell. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `clip_g` | Texteingabe für das globale CLIP-Modell. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `t5xxl` | Texteingabe für das T5-XXL-Modell. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `empty_padding` | Steuert, wie leere Texteingaben behandelt werden. Bei "none" führen leere Texteingaben für `clip_g`, `clip_l` oder `t5xxl` zu leeren Token-Listen statt zu Padding. Bei "empty_prompt" werden leere Eingaben als leere Prompts tokenisiert (Standard-Padding-Verhalten). Dies ist ein erweiterter Parameter (Standard: "none"). | COMBO | Ja | `"none"`<br>`"empty_prompt"` |

**Parametereinschränkungen:**

- Wenn `empty_padding` auf "none" gesetzt ist, führen leere Texteingaben für `clip_g`, `clip_l` oder `t5xxl` zu leeren Token-Listen statt zu Padding
- Der Node gleicht die Token-Längen zwischen den Eingaben `clip_l` und `clip_g` automatisch aus, indem die kürzere mit leeren Tokens aufgefüllt wird, wenn die Längen abweichen
- Alle Texteingaben unterstützen dynamische Prompts und mehrzeilige Texteingabe

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die kodierten Text-Conditioning-Daten, bereit für die Verwendung in SD3-Generierungspipelines | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/de.md)

---
**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`
