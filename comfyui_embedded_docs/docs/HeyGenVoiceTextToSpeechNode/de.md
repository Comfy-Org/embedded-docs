# HeyGen Voice 1.0 Text to Speech

Spricht Text in einer mit HeyGen Voice 1.0 Instant Clone geklonten Stimme aus. Der Node sendet den Text und die Voice-ID an HeyGen und gibt die erzeugte Sprachausgabe als Audio zurück. Zwei Modelle sind verfügbar: `heygen-voice-1` und das schnellere `heygen-voice-1-turbo`, das halb so viel kostet.

Die Auswahl eines `model` zeigt die für dieses Modell spezifischen Parameter an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `heygen-voice-1-turbo` ist schneller und kostet die Hälfte. Die Auswahl eines Modells zeigt die dafür spezifischen Parameter an: `voice_id`, `text`, `language` und `expressiveness_boost`. | DYNAMIC_COMBO | Ja | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | Stimme aus HeyGen Voice 1.0 Instant Clone (Standard: leer). | STRING | Ja | N/A |
| `text` | Text, der gesprochen werden soll. Bis zu 5000 Zeichen; Sprachausgaben, die länger als etwa 12 Minuten dauern, schlagen fehl, daher sehr langen chinesischen oder japanischen Text aufteilen (Standard: leer). | STRING | Ja | 1 bis 5000 Zeichen |
| `language` | Sprache des Textes. Legen Sie sie für eng verwandte Sprachen wie Serbisch oder Malaiisch fest, bei denen die automatische Erkennung zu Verwechslungen neigen kann (Standard: "auto"). | COMBO | Ja | `"auto"`<br>Mehrere Sprach-Presets |
| `expressiveness_boost` | Höhere Werte erhöhen die Ausdrucksstärke; niedrigere Werte bleiben näher an der Originalstimme (Standard: 0.5). | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.05) |

**Hinweis:** `voice_id` muss eine Stimme sein, die mit HeyGen Voice 1.0 Instant Clone erstellt wurde; wenn sie leer ist, bricht der Node mit einem Fehler ab. `text` muss mindestens ein Zeichen enthalten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Die aus dem Text erzeugte Sprachausgabe, gesprochen in der geklonten Stimme. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/de.md)

---
**Source fingerprint (SHA-256):** `61e345563db04a4dfc61e8862a328d5062aa2a77af57c2209ca4ca3862930be8`
