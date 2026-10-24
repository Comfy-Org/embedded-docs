# Flux.1 Kontext [pro] Image

Erzeugt oder bearbeitet ein Bild mit Flux.1 Kontext [pro] über die BFL-API, basierend auf einem Prompt und einem Seitenverhältnis. Bei verbundenem `input_image` beschreibt der Prompt die Bearbeitung; ohne dieses generiert der Node ein völlig neues Bild allein aus dem Prompt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Prompt` | Prompt für die Bildgenerierung. Bei einem Eingabebild geben Sie an, was und wie bearbeitet werden soll. | STRING | Ja | - |
| `aspect_ratio` | Seitenverhältnis des Bildes; muss zwischen 1:4 und 4:1 liegen (Standard: `"16:9"`). | STRING | Ja | - |
| `Guidance` | Guidance-Stärke für den Bildgenerierungsprozess (Standard: 3.0). | FLOAT | Ja | 0.1 bis 99.0 (Schritt: 0.1) |
| `Schritte` | Anzahl der Schritte für den Bildgenerierungsprozess (Standard: 50). | INT | Ja | 1 bis 150 |
| `Seed` | Der Zufallsseed zur Erzeugung des Rauschens (Standard: 1234). | INT | Ja | 0 bis 18446744073709551615 |
| `Prompt-Upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung angepasst, aber die Ergebnisse sind nicht deterministisch, sodass derselbe Seed nicht exakt dasselbe Ergebnis liefert (Standard: `False`). Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | True / False |
| `Eingabebild` | Optionales Bild zur Bearbeitung. Wenn nicht angegeben, wird der Prompt validiert, um sicherzustellen, dass er nicht leer ist. | IMAGE | Nein | - |

**Hinweis:** Der Node sendet die Anfrage an BFL und fragt in Intervallen ab, bis das Bild bereit ist. Anfragen, die von der Inhaltsmoderation von BFL abgelehnt werden, schlagen fehl, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das generierte oder bearbeitete Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextProImageNode/de.md)

---
**Source fingerprint (SHA-256):** `7a5be7e7859b1aca5130552345c76045ab64be3b4bee588091d147480a9ae1ac`
