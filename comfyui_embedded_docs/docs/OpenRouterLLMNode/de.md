# OpenRouterLLMNode

Der OpenRouter-LLM-Node sendet einen Text-Prompt an eine kuratierte Auswahl populärer Sprachmodelle, die über den OpenRouter-Dienst verfügbar sind, und gibt die generierte Textantwort zurück. Er unterstützt Modelle von Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) und Perplexity Sonar und kann optional Bilder oder Videos als Referenzeingaben in die Anfrage aufnehmen.

## Eingaben

Wenn im `model`-Selektor ein Modell ausgewählt wird, zeigt der Node modellspezifische Widgets zusätzlich zu den gemeinsamen Eingaben an – Reasoning-Aufwand, Web-Suchgröße und/oder Referenzmedien-Slots – abhängig von den Fähigkeiten des gewählten Modells.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingabe für das Modell. | STRING | Ja | N/A |
| `model` | Das OpenRouter-Modell, das zur Generierung der Antwort verwendet wird. | DYNAMIC_COMBO | Ja | Mehrere Optionen verfügbar (siehe Modellabschnitte unten) |
| `seed` | Seed für das Sampling. Zum Auslassen auf 0 setzen. Die meisten Modelle behandeln dies nur als Hinweis. (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells bestimmen. (Standard: "") | STRING | Nein | N/A |

### Anthropic Claude Models Eingaben

Gemeinsam genutzt von `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` und `anthropic/claude-haiku-4.5`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Diese Modelle unterstützen bis zu 20 Referenzbilder (siehe Referenzeingaben).

### OpenAI GPT Models Eingaben

Gemeinsam genutzt von `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` und `openai/gpt-5.5`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Diese Modelle unterstützen bis zu 20 Referenzbilder (siehe Referenzeingaben).

### Google Gemini 3.5 Flash Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Dieses Modell unterstützt bis zu 20 Referenzbilder und bis zu 4 Referenzvideos (siehe Referenzeingaben).

### xAI Grok Models Eingaben

Gemeinsam genutzt von `x-ai/grok-4.5`, `x-ai/grok-4.20` und `x-ai/grok-4.3`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Diese Modelle unterstützen bis zu 20 Referenzbilder (siehe Referenzeingaben).

### DeepSeek Models Eingaben

Gemeinsam genutzt von `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` und `deepseek/deepseek-v3.2`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Nur-Text-Modelle – keine Referenzbilder oder -videos.

### Qwen 3.6 Max Preview Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Nur-Text-Modell – keine Referenzbilder oder -videos.

### Qwen 3.6 Plus und Qwen 3.6 Flash Eingaben

Gemeinsam genutzt von `qwen/qwen3.6-plus` und `qwen/qwen3.6-flash`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Diese Modelle unterstützen bis zu 10 Referenzbilder und bis zu 4 Referenzvideos (siehe Referenzeingaben).

### Mistral Large 2512 Eingaben

Keine profilspezifischen Eingaben (Standardprofil). Dieses Modell unterstützt bis zu 8 Referenzbilder (siehe Referenzeingaben).

### Mistral Medium 3.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Dieses Modell unterstützt bis zu 8 Referenzbilder (siehe Referenzeingaben).

### Z.AI GLM Models Eingaben

Gemeinsam genutzt von `z-ai/glm-4.6` und `z-ai/glm-5`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Nur-Text-Modelle – keine Referenzbilder oder -videos.

### Moonshot Kimi K3 und K2.6 Eingaben

Gemeinsam genutzt von `moonshotai/kimi-k3` und `moonshotai/kimi-k2.6`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Diese Modelle unterstützen bis zu 10 Referenzbilder (siehe Referenzeingaben).

### Moonshot Kimi K2 Thinking Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Nur-Text-Modell – keine Referenzbilder oder -videos.

### Perplexity Sonar Pro Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Wie viel Web-Suchkontext abgerufen wird. Größer = fundierter, aber langsamer/teurer. (Standard: "medium") | COMBO | Nein | "low"<br>"medium"<br>"high" |

Nur-Text-Modell – keine Referenzbilder oder -videos.

### Perplexity Sonar Reasoning Pro und Sonar Deep Research Eingaben

Gemeinsam genutzt von `perplexity/sonar-reasoning-pro` und `perplexity/sonar-deep-research`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Wie viel Web-Suchkontext abgerufen wird. Größer = fundierter, aber langsamer/teurer. (Standard: "medium") | COMBO | Nein | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Reasoning-Aufwand. 'off' deaktiviert das Reasoning vollständig. (Standard: "off") | COMBO | Nein | "off"<br>"low"<br>"medium"<br>"high" |

Nur-Text-Modelle – keine Referenzbilder oder -videos.

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Optionale Referenzbild(er), als URLs gesendet. Erweiterbarer Slot: Verbinden Sie 1..N Bildeingaben (`image_1`, `image_2`, ...); das Anzahllimit hängt vom ausgewählten Modell ab (siehe Modellabschnitte). | IMAGE | Nein | 0 bis 20 (modellabhängig: 8, 10 oder 20) |
| `videos` | Optionale Referenzvideos, als URLs gesendet. Erweiterbarer Slot: Verbinden Sie 1..N Videoeingaben (`video_1`, `video_2`, ...); das Anzahllimit hängt vom ausgewählten Modell ab (siehe Modellabschnitte). | VIDEO | Nein | 0 bis 4 (modellabhängig) |

**Hinweise:**

- **Verfügbare Modelle:** Die verfügbaren Modelloptionen werden dynamisch erstellt und enthalten Modelle mit unterschiedlichen Fähigkeiten. Die vollständige Liste der 34 Modelle lautet:
  - Anthropic: `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5`, `anthropic/claude-haiku-4.5`
  - OpenAI: `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro`, `openai/gpt-5.5`
  - Google: `google/gemini-3.5-flash`
  - xAI: `x-ai/grok-4.5`, `x-ai/grok-4.20`, `x-ai/grok-4.3`
  - DeepSeek: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `deepseek/deepseek-v3.2`
  - Qwen: `qwen/qwen3.6-max-preview`, `qwen/qwen3.6-plus`, `qwen/qwen3.6-flash`
  - Mistral: `mistralai/mistral-large-2512`, `mistralai/mistral-medium-3-5`
  - Z.AI: `z-ai/glm-4.6`, `z-ai/glm-5`
  - Moonshot: `moonshotai/kimi-k3`, `moonshotai/kimi-k2.6`, `moonshotai/kimi-k2-thinking`
  - Perplexity: `perplexity/sonar-pro`, `perplexity/sonar-reasoning-pro`, `perplexity/sonar-deep-research`

- **Bild- und Videoeinschränkungen:** Die maximale Anzahl an Referenzbildern und -videos hängt vom ausgewählten Modell ab. Der Node löst einen Fehler aus, wenn die Gesamtzahl der bereitgestellten Bilder oder Videos das Limit des Modells überschreitet. Modelle ohne Bild- oder Videounterstützung zeigen die entsprechenden Referenz-Slots nicht an.

- **Reasoning-Verhalten:** Wenn `reasoning_effort` auf einen anderen Wert als "off" gesetzt ist, wird der Anbieter in der Anfrage gebeten, intern Schlussfolgerungen zu ziehen, ohne die Reasoning-Spur zurückzugeben.

- **Seed-Verhalten:** Der Parameter `seed` hat ein "control_after_generate"-Verhalten, d. h., er kann so eingestellt werden, dass er sich nach jeder Node-Ausführung automatisch ändert (z. B. randomisieren, inkrementieren oder fixieren), abhängig von den Widget-Einstellungen des Benutzers.

- **System-Prompt:** Der Parameter `system_prompt` ist optional und in der Benutzeroberfläche als erweiterter Parameter gekennzeichnet.

- **Fehlerfälle:** Der Node löst einen Fehler aus, wenn der Prompt nach dem Entfernen von Leerzeichen leer ist, wenn OpenRouter einen Fehler zurückgibt, wenn das ausgewählte Modell die Antwort verweigert oder wenn die Antwort keine Auswahlmöglichkeiten oder Nachricht enthält. Ein Preis-Badge auf dem Node zeigt eine ungefähre Kostenschätzung pro 1K Token basierend auf dem ausgewählten Modell.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Textantwort des OpenRouter-Modells. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/de.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
