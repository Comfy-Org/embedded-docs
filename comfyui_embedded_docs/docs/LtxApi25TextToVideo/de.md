# LTX 2.5 Text To Video

LTX 2.5 Text To Video ist ein API-Node, der mithilfe des LTX 2.5-Modells Videos in professioneller Qualität aus einer Textbeschreibung generiert. Sie geben einen Prompt an und wählen Generierungseinstellungen wie Modellstufe, Dauer, Auflösung, Bildrate und ob Audio eingeschlossen werden soll; der Node übermittelt die Aufgabe an die LTX API und gibt das resultierende Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Die LTX 2.5-Modellstufe, die für die Videogenerierung verwendet werden soll. | STRING | Ja | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `model.duration` | Die Länge des generierten Videos. | INT | Ja | Ganzzahl |
| `model.resolution` | Die Ausgabeauflösung des Videos. Verfügbare Optionen hängen vom ausgewählten `model` ab. | STRING | Ja | Mit "LTX-2.5 (Fast)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840"<br>Mit "LTX-2.5 (Pro)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920" |
| `model.fps` | Bildrate des generierten Videos (Standard: 25). | INT | Nein | Ganzzahl |
| `model.generate_audio` | Ob Audio zusammen mit dem Video generiert werden soll (Standard: True). | BOOLEAN | Nein | True<br>False |
| `prompt` | Die Textbeschreibung des zu generierenden Videos. Ein nicht leerer Prompt mit bis zu 10.000 Zeichen ist erforderlich (Standard: ""). | STRING | Ja | 1 bis 10000 Zeichen |
| `seed` | Seed-Wert für reproduzierbare Generierung (Standard: 42). | INT | Nein | Ganzzahl |

Hinweis: Die verfügbaren Optionen für `model.resolution` hängen vom ausgewählten `model` ab. "LTX-2.5 (Fast)" unterstützt Auflösungen bis zu 2160x3840, während "LTX-2.5 (Pro)" Auflösungen bis zu 1920x1080 unterstützt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das von der LTX API zurückgegebene generierte Video, bereit zur weiteren Verwendung im Workflow. Wenn die Audiogenerierung aktiviert wurde, enthält das Video synchronisiertes Audio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/de.md)

---
**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`
