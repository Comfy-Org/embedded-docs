# Google Gemini

Erzeugen Sie Textantworten mit den Gemini-Modellen von Google. Geben Sie einen Text-Prompt und optional ein oder mehrere Bilder, Audio-Clips, Videos oder Dateien als multimodalen Kontext an. Das ausgewählte Modell bestimmt, welche zusätzlichen Einstellungen angezeigt werden.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Gemini-Modell, das zur Generierung der Antwort verwendet wird. Das ausgewählte Modell bestimmt, welche zusätzlichen Eingaben angezeigt werden. | DYNAMIC_COMBO | Ja | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |

### Medieneingaben

Diese erweiterbaren Medieneingaben sind für jede Modelloption verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Optionales Bild oder optionale Bilder, die als Kontext für das Modell verwendet werden. Bis zu 16 Bilder. Erweiterbarer Slot: Verbinden Sie Bilder mit `image_1` bis `image_16`. | IMAGE | Nein | Bis zu 16 Bilder |
| `audio` | Optionaler Audioclip, der als Kontext für das Modell verwendet wird. Erweiterbarer Slot: `audio_1`. | AUDIO | Nein | 1 Audioclip |
| `video` | Optionaler Videoclip, der als Kontext für das Modell verwendet wird. Erweiterbarer Slot: `video_1`. | VIDEO | Nein | 1 Videoclip |

### Gemini 3.8 Flash Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingabe für das Modell. Fügen Sie detaillierte Anweisungen, Fragen oder Kontext hinzu. Darf nicht leer sein. | STRING | Ja | Mehrzeiliger Text (muss mindestens ein Nicht-Leerzeichen enthalten) |
| `video_processing` | Wie das Modell das angehängte Video liest. `static` tastet Frames mit einer festen Rate ab und sendet alle als Kontext; `agentic` lässt das Modell selbst durch die Zeitleiste navigieren und nur die Frames, Audio- oder Transkriptdaten laden, die es benötigt, was bei langen Videos deutlich weniger Eingabe-Token kostet. | COMBO | Ja | `"static"`<br>`"agentic"` (Standard: `"static"`) |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Gemini Input Files-Node. | GEMINI_INPUT_FILES | Nein | N/A |
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Token und ist langsamer. | COMBO | Ja | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (Standard: `"MEDIUM"`) |
| `max_output_tokens` | Maximale Anzahl der zu generierenden Token, einschließlich des internen Denkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, sodass eine höhere Obergrenze für kurze Antworten nichts extra kostet. | INT | Ja | 16-65536 (Standard: 32768) |
| `seed` | Seed für das Sampling. Auf 0 für einen zufälligen Seed setzen. Deterministische Ausgabe ist nicht garantiert. | INT | Ja | 0-2147483647 (Standard: 42) |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells vorgeben. | STRING | Ja | Mehrzeiliger Text (Standard: leer) |

### Gemini 3.7 Flash Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingabe für das Modell. Fügen Sie detaillierte Anweisungen, Fragen oder Kontext hinzu. Darf nicht leer sein. | STRING | Ja | Mehrzeiliger Text (muss mindestens ein Nicht-Leerzeichen enthalten) |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Gemini Input Files-Node. | GEMINI_INPUT_FILES | Nein | N/A |
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Token und ist langsamer. | COMBO | Ja | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (Standard: `"MEDIUM"`) |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. | FLOAT | Ja | 0.0-2.0 (Standard: 1.0) |
| `top_p` | Nucleus-Sampling: Stichproben aus dem kleinsten Token-Set entnehmen, dessen kumulative Wahrscheinlichkeit top_p erreicht. | FLOAT | Ja | 0.0-1.0 (Standard: 0.95) |
| `max_output_tokens` | Maximale Anzahl der zu generierenden Token, einschließlich des internen Denkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, sodass eine höhere Obergrenze für kurze Antworten nichts extra kostet. | INT | Ja | 16-65536 (Standard: 32768) |
| `seed` | Seed für das Sampling. Auf 0 für einen zufälligen Seed setzen. Deterministische Ausgabe ist nicht garantiert. | INT | Ja | 0-2147483647 (Standard: 42) |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells vorgeben. | STRING | Ja | Mehrzeiliger Text (Standard: leer) |

### Gemini 3.5 Flash Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingabe für das Modell. Fügen Sie detaillierte Anweisungen, Fragen oder Kontext hinzu. Darf nicht leer sein. | STRING | Ja | Mehrzeiliger Text (muss mindestens ein Nicht-Leerzeichen enthalten) |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Gemini Input Files-Node. | GEMINI_INPUT_FILES | Nein | N/A |
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Token und ist langsamer. | COMBO | Ja | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (Standard: `"MEDIUM"`) |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. | FLOAT | Ja | 0.0-2.0 (Standard: 1.0) |
| `top_p` | Nucleus-Sampling: Stichproben aus dem kleinsten Token-Set entnehmen, dessen kumulative Wahrscheinlichkeit top_p erreicht. | FLOAT | Ja | 0.0-1.0 (Standard: 0.95) |
| `max_output_tokens` | Maximale Anzahl der zu generierenden Token, einschließlich des internen Denkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, sodass eine höhere Obergrenze für kurze Antworten nichts extra kostet. | INT | Ja | 16-65536 (Standard: 32768) |
| `seed` | Seed für das Sampling. Auf 0 für einen zufälligen Seed setzen. Deterministische Ausgabe ist nicht garantiert. | INT | Ja | 0-2147483647 (Standard: 42) |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells vorgeben. | STRING | Ja | Mehrzeiliger Text (Standard: leer) |

### Gemini 3.1 Pro Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingabe für das Modell. Fügen Sie detaillierte Anweisungen, Fragen oder Kontext hinzu. Darf nicht leer sein. | STRING | Ja | Mehrzeiliger Text (muss mindestens ein Nicht-Leerzeichen enthalten) |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Gemini Input Files-Node. | GEMINI_INPUT_FILES | Nein | N/A |
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Token und ist langsamer. | COMBO | Ja | `"LOW"`<br>`"HIGH"` (Standard: `"HIGH"`) |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. | FLOAT | Ja | 0.0-2.0 (Standard: 1.0) |
| `top_p` | Nucleus-Sampling: Stichproben aus dem kleinsten Token-Set entnehmen, dessen kumulative Wahrscheinlichkeit top_p erreicht. | FLOAT | Ja | 0.0-1.0 (Standard: 0.95) |
| `max_output_tokens` | Maximale Anzahl der zu generierenden Token, einschließlich des internen Denkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, sodass eine höhere Obergrenze für kurze Antworten nichts extra kostet. | INT | Ja | 16-65536 (Standard: 32768) |
| `seed` | Seed für das Sampling. Auf 0 für einen zufälligen Seed setzen. Deterministische Ausgabe ist nicht garantiert. | INT | Ja | 0-2147483647 (Standard: 42) |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells vorgeben. | STRING | Ja | Mehrzeiliger Text (Standard: leer) |

### Gemini 3.1 Flash-Lite Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingabe für das Modell. Fügen Sie detaillierte Anweisungen, Fragen oder Kontext hinzu. Darf nicht leer sein. | STRING | Ja | Mehrzeiliger Text (muss mindestens ein Nicht-Leerzeichen enthalten) |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Gemini Input Files-Node. | GEMINI_INPUT_FILES | Nein | N/A |
| `thinking_level` | Wie stark das Modell intern nachdenkt, bevor es antwortet. HIGH verbessert die Qualität bei schwierigen Aufgaben, kostet aber mehr (Thinking-)Token und ist langsamer. | COMBO | Ja | `"LOW"`<br>`"HIGH"` (Standard: `"LOW"`) |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist kreativer. | FLOAT | Ja | 0.0-2.0 (Standard: 1.0) |
| `top_p` | Nucleus-Sampling: Stichproben aus dem kleinsten Token-Set entnehmen, dessen kumulative Wahrscheinlichkeit top_p erreicht. | FLOAT | Ja | 0.0-1.0 (Standard: 0.95) |
| `max_output_tokens` | Maximale Anzahl der zu generierenden Token, einschließlich des internen Denkens des Modells. Bei thinking_level HIGH kann ein niedriger Wert keinen Platz für die Antwort lassen; erhöhen Sie diesen Wert, wenn Antworten leer oder abgeschnitten zurückkommen. Das Modell stoppt frühzeitig, wenn es fertig ist, sodass eine höhere Obergrenze für kurze Antworten nichts extra kostet. | INT | Ja | 16-65536 (Standard: 32768) |
| `seed` | Seed für das Sampling. Auf 0 für einen zufälligen Seed setzen. Deterministische Ausgabe ist nicht garantiert. | INT | Ja | 0-2147483647 (Standard: 42) |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells vorgeben. | STRING | Ja | Mehrzeiliger Text (Standard: leer) |

Hinweis: Für Gemini 3.8 Flash sind `temperature` und `top_p` nicht verfügbar, und `video_processing` ist nur für diese Modelloption verfügbar. Die `thinking_level`-Optionen und Standardwerte unterscheiden sich je nach Modell wie oben aufgeführt.

Hinweis: Die Eingabe `prompt` darf nicht leer sein. Der Node validiert, dass sie mindestens ein Nicht-Leerzeichen enthält.

Hinweis: Der Node lädt die ersten bis zu 10 Medienelemente als URLs hoch, wobei Video, dann Audio, dann Bilder priorisiert werden. Alle verbleibenden Medien werden inline als Base64 gesendet. Die gesamten Inline-Medien sind auf 18 MB begrenzt; bei Überschreitung löst der Node einen Fehler aus, der Sie auffordert, die Anzahl oder Größe der angehängten Medien zu reduzieren.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `STRING` | Die vom ausgewählten Gemini-Modell generierte Textantwort. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV3/de.md)

---
**Source fingerprint (SHA-256):** `d04d1e97a9c213297899291ad30db14a9f946b07506d0377fead4e29510c5ad9`
