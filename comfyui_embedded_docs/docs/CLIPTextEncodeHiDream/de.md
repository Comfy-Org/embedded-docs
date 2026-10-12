# CLIP-Textkodierung (HiDream)

Der CLIPTextEncodeHiDream-Node verarbeitet vier separate Texteingaben mithilfe verschiedener Sprachmodelle (CLIP-L, CLIP-G, T5-XXL und LLaMA) und kombiniert sie zu einer einzelnen Conditioning-Ausgabe. Er tokenisiert jede Texteingabe mit ihrem entsprechenden Modell und kodiert sie gemeinsam mithilfe eines zeitplanbasierten Kodierungsansatzes, wodurch eine anspruchsvollere Textkonditionierung durch die gleichzeitige Nutzung mehrerer Sprachmodelle ermöglicht wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das zur Tokenisierung und Kodierung verwendet wird | CLIP | Ja | - |
| `clip_l` | Texteingabe für die Verarbeitung durch das CLIP-L-Modell. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `clip_g` | Texteingabe für die Verarbeitung durch das CLIP-G-Modell. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `t5xxl` | Texteingabe für die Verarbeitung durch das T5-XXL-Modell. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `llama` | Texteingabe für die Verarbeitung durch das LLaMA-Modell. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |

**Hinweis:** Alle vier Texteingaben (`clip_l`, `clip_g`, `t5xxl` und `llama`) sind für eine ordnungsgemäße Funktion erforderlich, da jede durch den Prozess der zeitplanbasierten Kodierung zur endgültigen Conditioning-Ausgabe beiträgt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die kombinierte Conditioning-Ausgabe aus allen verarbeiteten Texteingaben, kodiert mit der Methode der zeitplanbasierten Kodierung | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/de.md)

---
**Source fingerprint (SHA-256):** `c5e269c17bd2dd7d7171c02598a87983a988d953dd7df285978fc25a9c896e46`
