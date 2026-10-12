# Anthropic Claude

Erzeugt Textantworten von den Claude-Modellen von Anthropic. Geben Sie einen Text-Prompt und optional ein oder mehrere Bilder für multimodalen Kontext an; der Node gibt die vom Modell generierte Textantwort zurück.

## Eingaben

Die Eingaben sind in gemeinsame Einstellungen, modellspezifische Einstellungen, die angezeigt werden, wenn ein Modell ausgewählt wird, und optionale Referenzbilder unterteilt.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das Claude-Modell, das zum Generieren der Antwort verwendet wird. Durch Auswahl eines Modells werden unten modellspezifische Einstellungen eingeblendet. | DYNAMIC_COMBO | Ja | `"Opus 5.5"`<br>`"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5.1"`<br>`"Fable 5"`<br>`"Sonnet 5.5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `prompt` | Texteingabe für das Modell. (Standard: leerer String) | STRING | Ja | N/A |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten des Modells bestimmen. (Standard: leerer String) | STRING | Nein | N/A |

### Opus 5.5, Opus 5, Fable 5.1 und Fable 5 Eingaben

Diese vier Modelle verwenden dieselben Einstellungen. Sie bieten keine Temperatureinstellung, und Reasoning ist immer aktiviert.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `max_tokens` | Maximale Anzahl zu generierender Tokens (enthält Reasoning-Tokens, wenn aktiviert). (Standard: 32768) | INT | Ja | 1024 bis 64000 (Opus 5.5)<br>4096 bis 64000 (Opus 5, Fable 5.1, Fable 5) |
| `reasoning_effort` | Aufwand für erweitertes Thinking. Reasoning ist für dieses Modell immer aktiviert. (Standard: "high") | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.8, Sonnet 5.5 und Sonnet 5 Eingaben

Diese drei Modelle verwenden dieselben Einstellungen. Sie bieten keine Temperatureinstellung.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `max_tokens` | Maximale Anzahl zu generierender Tokens (enthält Reasoning-Tokens, wenn aktiviert). (Standard: 32768) | INT | Ja | 1024 bis 64000 (Sonnet 5.5)<br>4096 bis 64000 (Opus 4.8, Sonnet 5) |
| `reasoning_effort` | Aufwand für erweitertes Thinking. `"off"` deaktiviert Reasoning. (Standard: "off") | COMBO | Ja | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.7, Opus 4.6, Sonnet 4.6 und Sonnet 4.5 Eingaben

Diese vier Modelle verwenden dieselben Einstellungen.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `max_tokens` | Maximale Anzahl zu generierender Tokens (enthält Reasoning-Tokens, wenn aktiviert). (Standard: 32768) | INT | Ja | 4096 bis 64000 |
| `temperature` | Steuert die Zufälligkeit. 0.0 ist deterministisch, 1.0 ist am zufälligsten. Wird für Opus 4.7 und jedes Modell ignoriert, wenn `reasoning_effort` gesetzt ist. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |
| `reasoning_effort` | Aufwand für erweitertes Thinking. `"off"` deaktiviert Reasoning. (Standard: "off") | COMBO | Ja | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

`reasoning_effort` bietet `"off"`, `"low"`, `"medium"` und `"high"` für alle vier Modelle. Opus 4.7, Opus 4.6 und Sonnet 4.6 akzeptieren zusätzlich `"max"`, und Opus 4.7 akzeptiert außerdem `"xhigh"`.

### Haiku 4.5 Eingaben

Dieses Modell bietet keine `reasoning_effort`-Einstellung.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `max_tokens` | Maximale Anzahl zu generierender Tokens (enthält Reasoning-Tokens, wenn aktiviert). (Standard: 32768) | INT | Ja | 4096 bis 64000 |
| `temperature` | Steuert die Zufälligkeit. 0.0 ist deterministisch, 1.0 ist am zufälligsten. Wird für Opus 4.7 und jedes Modell ignoriert, wenn `reasoning_effort` gesetzt ist. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `images` | Optionale(s) Bild(er), die als Kontext für das Modell verwendet werden. Bis zu 20 Bilder. Erweiterbarer Slot: 1 bis 20 Elemente verbinden (`image_1` ... `image_20`). | IMAGE | Nein | 0 bis 20 Bilder |

### Parametereinschränkungen

- **Bildlimit:** Pro Anfrage können maximal 20 Bilder angegeben werden. Wenn mehr als 20 Bilder verbunden werden, wird ein Fehler ausgelöst.
- **Prompt erforderlich:** Der Prompt muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist. Ein leerer Prompt löst einen Validierungsfehler aus.
- **Temperaturbehandlung:** Wenn Thinking aktiviert ist, verlangt die Anthropic-API, dass die Temperatur nicht gesetzt ist (Standard ist 1.0). Opus 5.5, Opus 5, Opus 4.8, Fable 5.1, Fable 5, Sonnet 5.5 und Sonnet 5 bieten keine Temperatureinstellung. Opus 4.7 ignoriert `temperature`, und jedes Modell, bei dem `reasoning_effort` auf etwas anderes als `"off"` gesetzt ist, ignoriert sie ebenfalls.
- **Reasoning-/Thinking-Verhalten:** Die Einstellung `reasoning_effort` steuert, ob Thinking aktiviert ist. Bei Opus 5.5, Opus 5, Fable 5.1 und Fable 5 ist Reasoning immer aktiviert. Haiku 4.5 unterstützt kein Reasoning. Wenn Thinking aktiviert ist, verwendet der Node den passenden Thinking-Modus für das ausgewählte Modell, entweder adaptiv oder budgetbasiert. Im Budget-Modus wird das Reasoning-Token-Budget begrenzt, damit mindestens 1024 Tokens für die eigentliche Antwort übrig bleiben. Wenn `reasoning_effort` bei Sonnet 5.5 `"off"` ist, verwendet die Anfrage `between_tools`-Thinking anstelle von deaktiviertem Thinking, sodass die Antwort weiterhin kein Reasoning enthält.
- **Mindestwert für max_tokens:** `max_tokens` akzeptiert Werte ab 1024 bei Opus 5.5 und Sonnet 5.5 sowie ab 4096 bei allen anderen Modellen.
- **Sicherheitsverweigerung:** Wenn Claude die Anfrage aus Sicherheitsgründen nicht beantwortet, löst der Node einen Fehler aus, der Sie bittet, den Prompt umzuformulieren oder ein anderes Modell zu verwenden.
- **Ausgabetext:** Thinking- und Reasoning-Blöcke sind nicht in der Ausgabe enthalten; es wird nur der generierte Text zurückgegeben.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
|------------------|--------------|----------|
| `output` | Die generierte Textantwort des Claude-Modells. Thinking-/Reasoning-Blöcke sind nicht enthalten. Wenn kein Text generiert wird, wird "Empty response from Claude model." zurückgegeben. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/de.md)

---
**Source fingerprint (SHA-256):** `35b737da0f4c3a9da72910bf2053b18ae6a5c60989dc9607b61037623bc94e38`
