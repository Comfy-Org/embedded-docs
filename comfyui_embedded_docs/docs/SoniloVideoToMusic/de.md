# Sonilo Video zu Musik

Erzeugen Sie Musik aus einem Video mit dem KI-Modell von Sonilo. Dieser Node analysiert den Inhalt eines Eingabevideos und erstellt ein dazu passendes Musikstück. Er verwendet einen externen KI-Dienst, um das Video zu verarbeiten und das Audio zu generieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Eingabevideo, aus dem Musik generiert werden soll. Maximale Dauer: 6 Minuten. | VIDEO | Ja | - |
| `prompt` | Optionaler Text-Prompt zur Steuerung der Musikgenerierung. Für beste Qualität leer lassen – das Modell analysiert dann den Videoinhalt vollständig. (Standard: leerer String) | STRING | Nein | - |
| `seed` | Seed für Reproduzierbarkeit. Wird derzeit vom Sonilo-Dienst ignoriert, aber zur Konsistenz des Graphen beibehalten. (Standard: 0) | INT | Nein | 0 bis 18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die generierte Musik als Audiodatei. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/de.md)

---
**Source fingerprint (SHA-256):** `ed118d346add099f41a99635638ecb9aa4026b2210b17628c34cdad6bb919767`
