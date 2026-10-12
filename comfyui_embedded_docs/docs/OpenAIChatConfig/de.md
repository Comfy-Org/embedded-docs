# OpenAIChatConfig

Der OpenAIChatConfig-Node definiert erweiterte Optionen, die steuern, wie der OpenAI Chat Node Antworten generiert. Er ermöglicht es Ihnen, die Kürzungsstrategie festzulegen, die Anzahl der Ausgabe-Tokens zu begrenzen, benutzerdefinierte Anweisungen bereitzustellen und auszuwählen, wie viel Reasoning-Aufwand das Modell vor der Antwort betreiben soll.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `truncation` | Die Kürzungsstrategie, die für die Modellantwort verwendet werden soll. auto: Wenn der Kontext dieser Antwort und vorheriger Antworten die Kontextfenstergröße des Modells überschreitet, kürzt das Modell die Antwort, um sie an das Kontextfenster anzupassen, indem Eingabeelemente in der Mitte der Konversation entfernt werden. disabled: Wenn eine Modellantwort die Kontextfenstergröße eines Modells überschreitet, schlägt die Anfrage mit einem 400-Fehler fehl (Standard: "auto") | COMBO | Ja | "auto"<br>"disabled" |
| `max_output_tokens` | Eine Obergrenze für die Anzahl der Tokens, die für eine Antwort generiert werden können, einschließlich sichtbarer Ausgabe-Tokens und Reasoning-Tokens (Standard: 4096) | INT | Nein | 16 bis 16384 |
| `instructions` | Anweisungen für das Modell, wie die Antwort generiert werden soll (mehrzeilige Eingabe wird unterstützt) | STRING | Nein | - |
| `reasoning_effort` | Wie stark das Modell vor der Antwort nachdenkt. "default" überlässt die Wahl dem Modell. Unterstützte Stufen unterscheiden sich je nach Modell: GPT-6 Astra low-max, GPT-6 Sol/Luna und GPT-5.6 none-max (minimal wird nicht unterstützt), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1 hat kein Reasoning. Nicht unterstützte Stufen werden abgelehnt, bevor die Anfrage gesendet wird. (Standard: "default") | COMBO | Nein | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Hinweis: Obwohl `top_p` und `temperature` in der API-Spezifikation als Eigenschaften aufgeführt sind, werden sie nicht von allen Modellen unterstützt und daher nicht als Eingaben bereitgestellt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Konfigurationsobjekt, das die angegebenen erweiterten Einstellungen enthält, zur Verwendung mit OpenAI Chat Nodes | OPENAI_CHAT_CONFIG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/de.md)

---
**Source fingerprint (SHA-256):** `4237ad464230c464223c184eab38c7d707a29ba5f47da04c2ec2034cd4347207`
