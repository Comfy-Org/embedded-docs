# Flux.1 Kontext [max] Image

Erzeugt oder bearbeitet ein Bild mit Flux.1 Kontext [max] über die BFL API auf Grundlage eines Prompts und eines Seitenverhältnisses. Wenn `input_image` verbunden ist, beschreibt der Prompt die Bearbeitung; ohne `input_image` erzeugt der Node ein neues Bild allein anhand des Prompts. Er bietet dieselben Eingaben wie Flux.1 Kontext [pro] Image.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Prompt` | Prompt für die Bilderzeugung. Bei einem Eingabebild geben Sie an, was und wie bearbeitet werden soll. | STRING | Ja | - |
| `aspect_ratio` | Seitenverhältnis des Bildes; muss zwischen 1:4 und 4:1 liegen (Standard: `"16:9"`). | STRING | Ja | - |
| `Guidance` | Guidance-Stärke für den Bilderzeugungsprozess (Standard: 3.0). | FLOAT | Ja | 0.1 bis 99.0 (Schritt 0.1) |
| `Schritte` | Anzahl der Schritte für den Bilderzeugungsprozess (Standard: 50). | INT | Ja | 1 bis 150 |
| `Seed` | Der Zufalls-Seed, der zum Erzeugen des Rauschens verwendet wird (Standard: 1234). | INT | Ja | 0 bis 18446744073709551615 |
| `prompt_upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung angepasst; die Ergebnisse sind jedoch nicht deterministisch, sodass derselbe Seed nicht genau dasselbe Ergebnis liefert (Standard: `False`). Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | True / False |
| `input_image` | Optionales Bild zum Bearbeiten. Wenn es weggelassen wird, wird der Prompt validiert, um sicherzustellen, dass er nicht leer ist. | IMAGE | Nein | - |

**Hinweis:** Der Node sendet die Anfrage an BFL und fragt so lange ab, bis das Bild bereit ist. Anfragen, die von der Inhaltsmoderation von BFL abgelehnt werden, schlagen fehl, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das erzeugte oder bearbeitete Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMaxImageNode/de.md)

---
**Source fingerprint (SHA-256):** `557f9e69de37ee89e161dffdaef7458ed026b884298594f2046454b6b8d3c415`
