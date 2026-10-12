# PixverseTemplateNode

Der Node PixVerse Template ermöglicht die Auswahl aus verfügbaren Vorlagen für die PixVerse-Videogenerierung. Er wandelt den ausgewählten Vorlagennamen in die entsprechende Vorlagen-ID um, die die PixVerse-API für die Videoerstellung benötigt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `template` | Die Vorlage, die für die PixVerse-Videogenerierung verwendet werden soll. Die verfügbaren Optionen entsprechen den vordefinierten Vorlagen im PixVerse-System. | STRING | Ja | Mehrere Optionen verfügbar |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `pixverse_template` | Die Vorlagen-ID, die dem ausgewählten Vorlagennamen entspricht und von anderen PixVerse-Nodes für die Videogenerierung verwendet werden kann. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/de.md)

---
**Source fingerprint (SHA-256):** `618f9203127c55e8b65802fe3711c6d7c7dc6b631e9050f9685419c1b23bc138`
