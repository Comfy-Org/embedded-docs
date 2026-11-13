# Breeze Text to Speech

Wandelt Text mit Breeze TTS 2 in Sprache um. Wählen Sie eine Breeze-Stimme, legen Sie die Sprache des Textes fest und steuern Sie optional, wie die Zeile vorgetragen wird. Englisch und Chinesisch können beide Breeze-TTS-2-Modelle verwenden; alle anderen Sprachen verwenden Breeze TTS 2 Multilingual.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `voice` | Breeze-Stimme zum Sprechen, aus Breeze Voice Selector oder einem der Breeze-Node zur Stimmenerstellung. | BREEZE_VOICE | Ja | - |
| `text` | Zu sprechender Text, 1 bis 1000 Zeichen. Audio-Tags wie `(laughs)` oder `(sighs)` werden vorgetragen statt vorgelesen. Standard: leer. | STRING | Ja | 1 bis 1000 Zeichen |
| `language` | Sprache des Textes. Englisch und Chinesisch können beide Modelle verwenden; andere Sprachen verwenden Breeze TTS 2 Multilingual. Eine Stimme klingt am besten in ihrer eigenen Sprache, daher sollte für eine andere Sprache eine Kopie verwendet werden, die mit Breeze Voice Localize erstellt wurde. | DYNAMIC_COMBO | Ja | Mehrere Optionen verfügbar |
| `delivery` | Wie die Zeile vorgetragen wird: `neutral` behält die Stimme unverändert bei, `directed` folgt geschriebenen Anweisungen. Standard: `"neutral"`. | DYNAMIC_COMBO | Ja | `"neutral"`<br>`"directed"` |
| `speed` | Tempo-Multiplikator, der die Tonhöhe unverändert lässt. Standard: 1.0. | FLOAT | Nein | 0.5 bis 2.0 (Schritt 0.05) |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 2147483647 |

### Eingaben für Sprache "English" und "Chinese"

Diese erscheinen nur, wenn `language` Englisch oder Chinesisch ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` oder `Breeze TTS 2 Multilingual`. Standard: `"Breeze TTS 2"`. | COMBO | Ja | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

### Eingaben für Delivery "neutral"

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `speaker_boost` | Hält die Stimme näher an ihrem ursprünglichen Klang. Standard: false. | BOOLEAN | Nein | true<br>false |

### Eingaben für Delivery "directed"

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `instructions` | Wie der Text vorgetragen werden soll, geschrieben in derselben Sprache wie der Text. Standard: leer. | STRING | Nein | Mehrzeiliger Text |
| `strength` | Wie stark die Stimme den Anweisungen folgt. Standard: 4.0. | FLOAT | Nein | 1.0 bis 10.0 (Schritt 0.1) |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Die generierte Sprache als WAV-Audio. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/de.md)

---
**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`
