# Google Gemini

Erzeugen Sie Textantworten mit den Gemini-Modellen von Google. Geben Sie einen Text-Prompt und optional ein oder mehrere Bilder, Audioclips, Videos oder Dateien als multimodalen Kontext an. Der Node sendet den Prompt und alle angehängten Medien an das ausgewählte Modell und gibt die Textantwort des Modells zurück.

**Hinweis:** Dieser Node ist im Quellcode als veraltet (deprecated) markiert.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Gemini-Modell, das zur Generierung der Antwort verwendet wird. Die Auswahl eines Modells blendet unten dessen eigene Eingaben ein. | DYNAMIC_COMBO | Ja | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Texteingabe für das Modell. Fügen Sie detaillierte Anweisungen, Fragen oder Kontext hinzu. (Standard: "") | STRING | Ja | Muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist |
| `seed` | Seed für die Stichprobenentnahme. Auf 0 setzen für einen zufälligen Seed. Deterministische Ausgabe ist nicht garantiert. (Standard: 42) | INT | Ja | 0 bis 2147483647 |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells bestimmen. (Standard: "") | STRING | Nein |  |

### Gemini 3.8 Flash Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"Gemini 3.8 Flash"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Tokens und ist langsamer. (Standard: "MEDIUM") | COMBO | Ja | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `max_output_tokens` | Maximale Anzahl zu generierender Tokens, einschließlich des internen Nachdenkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, daher kostet eine höhere Obergrenze bei kurzen Antworten nichts extra. (Standard: 32768) | INT | Ja | 16 bis 65536 |

**Hinweis:** Dieses Modell bietet keine Sampling-Steuerung über `temperature` oder `top_p`.

### Gemini 3.7 Flash Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"Gemini 3.7 Flash"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Tokens und ist langsamer. (Standard: "MEDIUM") | COMBO | Ja | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 2.0 |
| `top_p` | Nucleus-Sampling: Stichprobenentnahme aus der kleinsten Token-Menge, deren kumulative Wahrscheinlichkeit top_p erreicht. (Standard: 0.95) | FLOAT | Ja | 0.0 bis 1.0 |
| `max_output_tokens` | Maximale Anzahl zu generierender Tokens, einschließlich des internen Nachdenkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, daher kostet eine höhere Obergrenze bei kurzen Antworten nichts extra. (Standard: 32768) | INT | Ja | 16 bis 65536 |

### Gemini 3.5 Flash Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"Gemini 3.5 Flash"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Tokens und ist langsamer. (Standard: "MEDIUM") | COMBO | Ja | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 2.0 |
| `top_p` | Nucleus-Sampling: Stichprobenentnahme aus der kleinsten Token-Menge, deren kumulative Wahrscheinlichkeit top_p erreicht. (Standard: 0.95) | FLOAT | Ja | 0.0 bis 1.0 |
| `max_output_tokens` | Maximale Anzahl zu generierender Tokens, einschließlich des internen Nachdenkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, daher kostet eine höhere Obergrenze bei kurzen Antworten nichts extra. (Standard: 32768) | INT | Ja | 16 bis 65536 |

### Gemini 3.1 Pro Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"Gemini 3.1 Pro"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Tokens und ist langsamer. (Standard: "HIGH") | COMBO | Ja | `"LOW"`<br>`"HIGH"` |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 2.0 |
| `top_p` | Nucleus-Sampling: Stichprobenentnahme aus der kleinsten Token-Menge, deren kumulative Wahrscheinlichkeit top_p erreicht. (Standard: 0.95) | FLOAT | Ja | 0.0 bis 1.0 |
| `max_output_tokens` | Maximale Anzahl zu generierender Tokens, einschließlich des internen Nachdenkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, daher kostet eine höhere Obergrenze bei kurzen Antworten nichts extra. (Standard: 32768) | INT | Ja | 16 bis 65536 |

### Gemini 3.1 Flash-Lite Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"Gemini 3.1 Flash-Lite"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Tokens und ist langsamer. (Standard: "LOW") | COMBO | Ja | `"LOW"`<br>`"HIGH"` |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 2.0 |
| `top_p` | Nucleus-Sampling: Stichprobenentnahme aus der kleinsten Token-Menge, deren kumulative Wahrscheinlichkeit top_p erreicht. (Standard: 0.95) | FLOAT | Ja | 0.0 bis 1.0 |
| `max_output_tokens` | Maximale Anzahl zu generierender Tokens, einschließlich des internen Nachdenkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, daher kostet eine höhere Obergrenze bei kurzen Antworten nichts extra. (Standard: 32768) | INT | Ja | 16 bis 65536 |

### Medien- und Dateieingaben

Die folgenden Eingaben werden von allen Modellen gemeinsam verwendet und erscheinen neben den modellspezifischen Eingaben.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Erweiterbarer Slot: Verbinden Sie 1 bis 16 Bilder (`image_1` ... `image_16`). Optionale(s) Bild(er) zur Verwendung als Kontext für das Modell. Bis zu 16 Bilder. | IMAGE | Nein | 0 bis 16 Bilder |
| `audio` | Erweiterbarer Slot: Verbinden Sie einen Audioclip (`audio_1`). Optionaler Audioclip zur Verwendung als Kontext für das Modell. | AUDIO | Nein | 0 bis 1 Clip |
| `video` | Erweiterbarer Slot: Verbinden Sie einen Videoclip (`video_1`). Optionaler Videoclip zur Verwendung als Kontext für das Modell. | VIDEO | Nein | 0 bis 1 Clip |
| `files` | Optionale Datei(en) zur Verwendung als Kontext für das Modell. Akzeptiert Eingaben vom Node Gemini Input Files. | GEMINI_INPUT_FILES | Nein |  |

**Hinweis:** Wenn Medien (Bilder, Audio oder Video) angehängt werden, lädt der Node die ersten 10 Medienelemente in den ComfyAPI-Speicher hoch und übergibt sie als URLs; dieses URL-Budget wird von allen Medientypen gemeinsam genutzt und in der Reihenfolge verbraucht (zuerst Video, dann Audio, dann Bilder). Alle verbleibenden Medien werden inline als Base64-Daten kodiert, mit einer maximalen kombinierten Inline-Payload von 18 MB. Wenn die Inline-Payload 18 MB überschreiten würde, löst der Node einen Fehler aus. Der Parameter `prompt` muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist. Wenn `seed` auf 0 gesetzt wird, wird ein zufälliger Seed angefordert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die vom Gemini-Modell generierte Textantwort. Wenn das Modell keinen Text erzeugt, wird die Zeichenkette "Empty response from Gemini model..." zurückgegeben. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `8ae14c6465569695e1e99b0040cb2c745e5f3d9ddcd3b03013530dc7e7135b87`
