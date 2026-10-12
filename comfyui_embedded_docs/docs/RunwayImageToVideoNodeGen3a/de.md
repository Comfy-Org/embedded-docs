# RunwayImageToVideoNodeGen3a

Der Node Runway Image to Video (Gen3a Turbo) erzeugt aus einem einzelnen Startbild ein Video mithilfe des Gen3a Turbo-Modells von Runway. Er nimmt einen Text-Prompt und ein initiales Bild entgegen und erstellt dann eine Videosequenz basierend auf der angegebenen Dauer und dem Seitenverhältnis. Die Generierung wird remote über die API von Runway verarbeitet. Dieser Node ist als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Generierung (Standard: "") | STRING | Ja | N/A |
| `start_frame` | Startbild, das für das Video verwendet wird | IMAGE | Ja | N/A |
| `duration` | Dauer des generierten Videos in Sekunden (Standard: "5") | COMBO | Ja | `"5"`<br>`"10"` |
| `ratio` | Seitenverhältnis des generierten Videos (Standard: "768:1280") | COMBO | Ja | `"768:1280"`<br>`"1280:768"` |
| `seed` | Zufälliger Seed für die Generierung (Standard: 0) | INT | Ja | 0 bis 4294967295 |

**Parametereinschränkungen:**

- Der Parameter `prompt` muss mindestens ein Zeichen enthalten (er darf nicht leer sein).
- Der Parameter `start_frame` akzeptiert ein einzelnes Bild (maximal 1).
- Der Parameter `start_frame` darf die Abmessungen von 7999 x 7999 Pixeln nicht überschreiten.
- Der Parameter `start_frame` muss ein Seitenverhältnis zwischen 1:2 und 2:1 (0,5 bis 2,0) aufweisen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videosequenz | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/de.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
