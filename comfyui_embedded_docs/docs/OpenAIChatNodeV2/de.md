# OpenAI ChatGPT

Dieser Node generiert Textantworten mit den GPT-Modellen von OpenAI. Er sendet einen Text-Prompt und optional Bilder oder Dateien als Kontext und gibt die Antwort als String zurück. Jede Einstellung befindet sich im Selektor `model`: Wenn Sie ein Modell auswählen, werden die eigenen `reasoning_effort`-Stufen, das Token-Limit, der Seed und der System-Prompt dieses Modells angezeigt, sodass kein separater Konfigurations-Node erforderlich ist. Dieser Node ersetzt den früheren OpenAI ChatGPT-Node, der im Quellcode inzwischen als veraltet markiert ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, das zur Generierung der Antwort verwendet wird. Jedes Modell stellt die von ihm unterstützten `reasoning_effort`-Stufen bereit (Standard: `"gpt-6.2-sol"`). | DYNAMIC_COMBO | Ja | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | Texteingabe für das Modell (Standard: leerer String). | STRING | Ja | - |
| `images` | Erweiterbarer Slot: 1..16 Elemente verbinden (`image_1`, `image_2`, ...). Optionale Bilder, die als Kontext für das Modell verwendet werden. | IMAGE | Nein | 0 bis 16 Bilder |
| `files` | Optionale Dateien, die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node OpenAI ChatGPT Input Files. | OPENAI_INPUT_FILES | Nein | - |
| `reasoning_effort` | Wie stark das Modell vor der Antwort nachdenkt. Höhere Stufen verwenden mehr Tokens und dauern länger. Die angebotenen Stufen hängen vom ausgewählten Modell ab (Standard: `"medium"`, `"high"` für `gpt-5.5-pro`). | COMBO | Ja | Siehe die modellspezifische Liste unten |
| `max_output_tokens` | Maximale Anzahl zu generierender Tokens, einschließlich Reasoning-Tokens. Ein niedriger Wert zusammen mit einem hohen `reasoning_effort` kann dazu führen, dass kein Platz für die Antwort bleibt (Standard: 32768). | INT | Ja | 16 bis 128000 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 2147483647 |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells vorgeben (Standard: leerer String). | STRING | Nein | - |

### Reasoning-Aufwandsstufen pro Modell

- `gpt-6.2-sol`, `gpt-6.2-astra`, `gpt-6-astra`, `gpt-6.1-sol`: `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, Standard `"medium"`.
- `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, Standard `"medium"`.
- `gpt-5.5-pro`: `"medium"`, `"high"`, `"xhigh"`, Standard `"high"`.
- `gpt-5.5`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, Standard `"medium"`.

### Hinweise zum Verhalten

- Es wird nur der Antworttext zurückgegeben. Nachrichten, die das Modell in seiner Kommentarphase während des Nachdenkens ausgibt, werden übersprungen.
- Wenn das Token-Budget aufgebraucht ist, bevor die Antwort geschrieben wurde, löst der Node einen Fehler aus, der Sie auffordert, `max_output_tokens` zu erhöhen.
- Bilder werden in ihrer eigenen Auflösung mit der automatischen Detailstufe der API gesendet, sodass große Bilder mehr Tokens verbrauchen.
- Jede Anfrage wird auf OpenAI-Seite gespeichert, und der zurückgegebene Text verbindet die Antwortteile mit Zeilenumbrüchen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die vom OpenAI-Modell generierte Textantwort. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
