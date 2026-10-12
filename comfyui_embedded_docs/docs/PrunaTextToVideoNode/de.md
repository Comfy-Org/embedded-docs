# PrunaTextToVideoNode

Erzeugt ein Video aus einem Text-Prompt mit Prunas P-Video-2-Modell. Der Prompt beschreibt die Szene, ihre Bewegung und ihren Ton, und der Node erzeugt entweder einen eigenen Soundtrack oder verwendet einen Audio-Clip, der die Bewegung steuert und zum Soundtrack wird.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Pruna-Videomodell. Die Auswahl eines Modells blendet dessen eigene Eingaben unten ein. | DYNAMIC_COMBO | Ja | `"p-video-2"` |

### P-Video-2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.prompt` | Beschreibt das Video, seine Bewegung und seinen Ton. Muss mindestens ein Nicht-Leerzeichen-Zeichen enthalten, bis zu 5000 Zeichen (Standard: leer). | STRING | Ja | Bis zu 5000 Zeichen |
| `model.aspect_ratio` | Seitenverhältnis des Ausgabevideos (Standard: `"16:9"`). | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `model.duration` | Länge des Videos in Sekunden. `"auto"` lässt das Modell die Länge anhand des Prompts wählen. Wird ignoriert, wenn `model.audio` verbunden ist: Das Video folgt dann der Audiolänge, auf eine ganze Sekunde aufgerundet, bis zu 20 Sekunden (Standard: `"5"`). | COMBO | Ja | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `model.resolution` | Ausgabeauflösung. 720p rendert etwa 0,9 Megapixel (1280x704 bei 16:9), 1080p etwa 2 Megapixel (1920x1088 bei 16:9) (Standard: `"720p"`). | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `model.fps` | Frames pro Sekunde. 48 fps sind bei Draft mit 1080p nicht verfügbar (Standard: `"24"`). | COMBO | Ja | `"24"`<br>`"48"` |
| `model.draft` | Schnelleres, weniger detailliertes Rendering, das zu einem niedrigeren Tarif als ein Standard-Rendering abgerechnet wird (Standard: False). | BOOLEAN | Ja | True/False |
| `model.generate_audio` | Erzeugt einen Soundtrack für das Video. Wird ignoriert, wenn `model.audio` verbunden ist; dann wird dieses stattdessen zum Soundtrack (Standard: True). | BOOLEAN | Ja | True/False |
| `model.enhance_prompt` | Schreibt den Prompt vor der Generierung detaillierter um; kurze Prompts benötigen dies. Deaktivieren Sie es, um ein Ergebnis mit demselben Seed exakt zu reproduzieren (Standard: True). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.audio` | Audio, das die Bewegung steuert und zum Soundtrack wird. Mindestens 1 Sekunde lang; Audio, das länger als 20 Sekunden ist, wird gekürzt. Legt die Videolänge anstelle von `model.duration` fest. | AUDIO | Nein | - |
| `model.seed` | Seed für die Generierung. Derselbe Seed reproduziert ein Ergebnis nur dann exakt, wenn `model.enhance_prompt` deaktiviert ist (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Hinweise:**

- `model.prompt` ist erforderlich und auf 5000 Zeichen begrenzt.
- Draft bei 1080p kann nicht mit 48 fps kombiniert werden: Der Node löst einen Fehler aus; deaktivieren Sie daher entweder Draft oder verwenden Sie 24 fps.
- Verbundenes Audio muss mindestens 1 Sekunde lang sein; alles über 20 Sekunden wird ignoriert.
- Wenn `model.audio` verbunden ist, legt das Audio die Videolänge fest, sodass `model.duration` und `model.generate_audio` keine Wirkung haben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das generierte Video mit seinem Soundtrack. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `bb7bacf2591618220c72525c1e32382174abe3a55069720adbc84fc1d8081718`
