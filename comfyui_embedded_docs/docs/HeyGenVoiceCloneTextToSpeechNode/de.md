# HeyGen Voice 1.0 Instant Clone Text to Speech

Klonen Sie eine Stimme aus einer Aufnahme eines Sprechers und sprechen Sie damit Text mit HeyGen Voice 1.0. Der Node lädt die Aufnahme hoch, synthetisiert die Sprachausgabe und gibt sie als Audio zurück, sodass ein einzelner Node von einer Stimmprobe zur fertigen Sprachausgabe führt.

Durch Auswahl eines `model` werden die spezifischen Parameter des Modells sichtbar: `audio`, `text`, `language`, `expressiveness_boost`, `recording_language`, `similarity`, `remove_background_noise` und `seed`.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `heygen-voice-1-turbo` ist schneller und kostet weniger (Standard: `"heygen-voice-1"`). | DYNAMIC_COMBO | Ja | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `audio` | Aufnahme eines Sprechers zum Klonen. Verwenden Sie mindestens 10 Sekunden klarer Sprache; nur die ersten 3 Minuten werden verwendet. | AUDIO | Ja | - |
| `text` | Zu sprechender Text, bis zu 5000 Zeichen. Sprachausgaben, die länger als etwa 12 Minuten dauern, schlagen fehl, deshalb sollten Sie sehr langen chinesischen oder japanischen Text aufteilen (Standard: leer). | STRING | Ja | 1 bis 5000 Zeichen |
| `language` | Sprache des Textes. Legen Sie sie für eng verwandte Sprachen wie Serbisch oder Malaiisch fest, die die automatische Erkennung verwechseln kann (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>Mehrere Sprachvoreinstellungen |
| `expressiveness_boost` | Höhere Werte sind ausdrucksstärker; niedrigere Werte bleiben näher an der Originalstimme (Standard: 0.5). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.05) |
| `recording_language` | In der Aufnahme gesprochene Sprache, wodurch der Klon auf diese Sprache eingeschränkt wird (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>Mehrere Sprachvoreinstellungen |
| `similarity` | Wie eng die Stimme der Aufnahme folgt (Standard: `"max"`). | COMBO | Ja | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Bereinigt Hintergrundgeräusche in der Aufnahme vor dem Klonen (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 2147483647 |

`text` muss mindestens ein Zeichen enthalten, und `audio` ist erforderlich: Eine Aufnahme mit mehreren Sprechern oder eine Aufnahme, die zu verrauscht zum Klonen ist, führt zu einer schlechten Stimmqualität. Legen Sie `recording_language` fest, wenn die Sprache der Stimmprobe nicht eindeutig ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Der in der geklonten Stimme gesprochene Text. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneTextToSpeechNode/de.md)

---
**Source fingerprint (SHA-256):** `ea18e2abce687e106ed0b37eb7afd723fbe72a3b4d58124a143c00b66d2fe7c9`
