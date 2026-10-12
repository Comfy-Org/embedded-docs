# RunwayFirstLastFrameNode

Der Node „Runway First-Last-Frame to Video“ erzeugt ein Video unter Verwendung eines Start-Frames, eines End-Frames und eines Text-Prompts. Er erstellt mithilfe des gen3a_turbo-Modells von Runway einen sanften Übergang zwischen den beiden bereitgestellten Keyframes. Er ist besonders nützlich für komplexe Übergänge, bei denen sich der End-Frame vollständig vom Start-Frame unterscheidet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt für die Generierung (Standard: leerer String) | STRING | Ja | N/A |
| `start_frame` | Start-Frame, der für das Video verwendet werden soll | IMAGE | Ja | N/A |
| `end_frame` | End-Frame, der für das Video verwendet werden soll. Wird nur für gen3a_turbo unterstützt. | IMAGE | Ja | N/A |
| `duration` | Dauer des generierten Videos in Sekunden. Die längere Dauer von 10 s gibt der Generierung mehr Zeit, um sanft zwischen Start- und End-Frame überzugehen (Standard: `"5"`). | COMBO | Ja | `"5"`<br>`"10"` |
| `ratio` | Seitenverhältnis für das generierte Video (Standard: `"768:1280"`) | COMBO | Ja | `"768:1280"`<br>`"1280:768"` |
| `seed` | Zufälliger Seed für die Generierung (Standard: 0) | INT | Ja | 0 bis 4294967295 |

**Parametereinschränkungen:**

- Der `prompt` muss mindestens 1 Zeichen enthalten.
- Sowohl `start_frame` als auch `end_frame` dürfen maximal 7999x7999 Pixel groß sein.
- Sowohl `start_frame` als auch `end_frame` müssen Seitenverhältnisse zwischen 0,5 und 2,0 haben.
- Der Parameter `end_frame` wird nur bei Verwendung des gen3a_turbo-Modells unterstützt.

**Hinweise:**

- Die Generierungskosten basieren auf der ausgewählten Dauer: USD 0,0715 pro Sekunde (USD 0,3575 für 5 Sekunden, USD 0,715 für 10 Sekunden).
- Dieser Node ist als veraltet markiert.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
|------------------|--------------|----------|
| `output` | Das generierte Video, das zwischen Start- und End-Frame übergeht | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
