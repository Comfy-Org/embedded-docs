# OpenAI ChatGPT

Dieser Node generiert Textantworten von einem OpenAI-Modell. Er sendet Ihren Text-Prompt und optional Bilder oder Dateien an ein OpenAI-Modell und gibt die generierte Textantwort zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingaben für das Modell, die zur Generierung einer Antwort verwendet werden (Standard: leerer String). | STRING | Ja | - |
| `persist_context` | Dieser Parameter ist veraltet und hat keine Auswirkung (Standard: False). | BOOLEAN | Ja | - |
| `model` | Das Modell, das zur Generierung der Antwort verwendet wird (Standard: `gpt-5`) | COMBO | Ja | `gpt-6-astra`<br>`gpt-6-sol`<br>`gpt-6-luna`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | Optionales Bild oder optionale Bilder, die als Kontext für das Modell verwendet werden. Um mehrere Bilder einzubinden, können Sie den Node „Batch Images“ verwenden. | IMAGE | Nein | - |
| `files` | Optionale Datei oder optionale Dateien, die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node „OpenAI Chat Input Files“. | OPENAI_INPUT_FILES | Nein | - |
| `advanced_options` | Optionale Konfiguration für das Modell. Akzeptiert Eingaben vom Node „OpenAI Chat Advanced Options“. | OPENAI_CHAT_CONFIG | Nein | - |

Hinweis: Wenn eine `advanced_options`-Konfiguration verbunden ist, die einen Reasoning-Aufwand festlegt, muss das ausgewählte `model` diesen Aufwandswert unterstützen. Beispielsweise unterstützt die Modellfamilie gpt-4.1 keinen Reasoning-Aufwand, `gpt-6-sol` und `gpt-6-luna` unterstützen none, low, medium, high, xhigh und max, `gpt-5.5` unterstützt none, low, medium, high und xhigh, und `gpt-5.5-pro` unterstützt medium, high und xhigh. Wenn der Reasoning-Aufwand vom ausgewählten Modell nicht unterstützt wird, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output_text` | Die vom OpenAI-Modell generierte Textantwort. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/de.md)

---
**Source fingerprint (SHA-256):** `46b4558f1368191e2b4eb68f79e098f289c9eb80e1e05f7a516123c098295f2b`
