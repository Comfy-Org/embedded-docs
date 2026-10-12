# CLIP-Textkodierung (Kandinsky 5)

Der Node CLIP Text Encode (Kandinsky 5) bereitet Text-Prompts für die Verwendung mit dem Kandinsky 5-Modell vor. Er nimmt zwei separate Texteingaben entgegen, tokenisiert sie mit einem bereitgestellten CLIP-Modell und kombiniert sie zu einer einzelnen Conditioning-Ausgabe, die den Bildgenerierungsprozess steuert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das zum Tokenisieren und Kodieren der Text-Prompts verwendet wird. | CLIP | Ja |  |
| `clip_l` | Der primäre Text-Prompt. Diese Eingabe unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja |  |
| `qwen25_7b` | Der sekundäre Text-Prompt. Diese Eingabe unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja |  |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die kombinierten Conditioning-Daten, die aus beiden Text-Prompts erzeugt werden und bereit sind, in ein Kandinsky 5-Modell für die Bildgenerierung eingespeist zu werden. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/de.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
