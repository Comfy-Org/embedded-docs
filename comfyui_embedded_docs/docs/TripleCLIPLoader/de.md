# CLIP laden (dreifach)

TripleCLIPLoader lädt drei Text-Encoder-Modelle gleichzeitig und kombiniert sie zu einem einzelnen CLIP-Modell. Er wird für Workflows verwendet, die mehrere zusammenarbeitende Text-Encoder benötigen, wie etwa SD3, das die Modelle clip-l, clip-g und t5 verwendet.

Ein gängiges Rezept für SD3 ist: clip-l, clip-g, t5.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | Das erste Text-Encoder-Modell, das aus den verfügbaren Text-Encodern geladen wird | COMBO | Ja | Mehrere Optionen verfügbar (alle Dateien im text_encoders-Ordner) |
| `clip_name2` | Das zweite Text-Encoder-Modell, das aus den verfügbaren Text-Encodern geladen wird | COMBO | Ja | Mehrere Optionen verfügbar (alle Dateien im text_encoders-Ordner) |
| `clip_name3` | Das dritte Text-Encoder-Modell, das aus den verfügbaren Text-Encodern geladen wird | COMBO | Ja | Mehrere Optionen verfügbar (alle Dateien im text_encoders-Ordner) |

**Hinweis:** Alle drei Parameter sind erforderlich. Die verfügbaren Optionen sind die Text-Encoder-Dateien in Ihrem text_encoders-Ordner. Wenn eine ausgewählte Datei nicht gefunden werden kann, löst der Node einen Fehler aus. Der Node lädt alle drei ausgewählten Modelle und kombiniert sie zu einem einzelnen CLIP-Modell.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `CLIP` | Ein kombiniertes CLIP-Modell, das alle drei geladenen Text-Encoder enthält | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/de.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
