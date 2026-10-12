# Wan 2.7 Text zu Video

Dieser Node generiert ein Video aus einer Textbeschreibung mithilfe des Wan-2.7-Modells. Er sendet Ihren Prompt an die Wan-Video-Generierungs-API, wartet, bis die Aufgabe abgeschlossen ist, und gibt das resultierende Video zurück. Optional können Sie einen Audioclip anschließen, um die Bewegung und das Timing des Videos zu beeinflussen; wenn kein Audio bereitgestellt wird, generiert das Modell automatisch passendes Audio.

## Eingaben

### Gemeinsame Eingaben

Diese Eingaben sind immer auf der obersten Ebene des Nodes verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das spezifische Modell, das für die Videogenerierung verwendet werden soll. | DYNAMIC_COMBO | Ja | `"wan2.7-t2v"` |
| `audio` | Audio zur Steuerung der Videogenerierung (z. B. Lippensynchronisation, taktsynchrone Bewegung). Dauer: 3s-30s. Wenn nicht bereitgestellt, generiert das Modell automatisch passende Hintergrundmusik oder Soundeffekte. | AUDIO | Nein | - |
| `seed` | Seed, der für die Generierung verwendet werden soll (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung verbessert werden soll (Standard: True). | BOOLEAN | Ja | True<br>False |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: False). | BOOLEAN | Ja | True<br>False |

### wan2.7-t2v Eingaben

Diese Einstellungen erscheinen, wenn das Modell `wan2.7-t2v` ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll. Standard ist eine leere Zeichenkette. | STRING | Nein | - |
| `resolution` | Die Auflösung des Ausgabevideos (Standard: "720P"). | COMBO | Ja | `"720P"`<br>`"1080P"` |
| `ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Die Länge des Videos in Sekunden (Standard: 5). | INT | Ja | 2 bis 15 |

**Hinweis:** Die Eingabe `prompt` darf nicht leer sein. Die Eingabe `audio` ist optional; wenn sie bereitgestellt wird, akzeptiert der Node Audio zwischen 1,5 und 60 Sekunden, obwohl der Tooltip 3s-30s empfiehlt. Wenn kein Audio bereitgestellt wird, generiert das Modell automatisch passendes Audio. Wenn `negative_prompt` leer gelassen wird, wird es nicht an die API gesendet. `prompt_extend` und `watermark` sind erweiterte Optionen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`
