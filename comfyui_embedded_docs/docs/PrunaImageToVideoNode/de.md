# PrunaImageToVideoNode

Animiert ein Bild mit dem P-Video-2-Modell von Pruna zu einem Video. Das erste Einzelbild ist erforderlich und legt das Seitenverhältnis der Ausgabe fest; ein optionales letztes Einzelbild gibt dem Video einen Endpunkt, zu dem interpoliert wird. Der Prompt beschreibt, wie sich die Szene bewegt, und der Node erzeugt entweder eine eigene Tonspur oder verwendet einen Audioclip, der die Bewegung antreibt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Pruna-Videomodell, das verwendet werden soll. Bei Auswahl eines Modells werden unten seine eigenen Eingaben eingeblendet. | DYNAMIC_COMBO | Ja | `"p-video-2"` |

### P-Video-2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.first_frame` | Bild, mit dem das Video beginnt. Die Ausgabe behält das Seitenverhältnis dieses Bildes bei. | IMAGE | Ja | - |
| `model.last_frame` | Bild, mit dem das Video endet. Sein Seitenverhältnis muss nahe am Seitenverhältnis des ersten Einzelbildes liegen. | IMAGE | Nein | - |
| `model.prompt` | Beschreibt, wie sich die Szene bewegt und anhört. Muss mindestens ein Zeichen enthalten, das kein Leerraumzeichen ist, bis zu 5000 Zeichen (Standard: leer). | STRING | Ja | Bis zu 5000 Zeichen |
| `model.duration` | Länge des Videos in Sekunden. `"auto"` lässt das Modell die Länge anhand des Prompts wählen. Wird ignoriert, wenn `model.audio` verbunden ist: Das Video folgt dann der Audiolänge, auf eine ganze Sekunde aufgerundet, bis zu 20 Sekunden (Standard: `"5"`). | COMBO | Ja | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `model.resolution` | Ausgabeauflösung. 720p rendert etwa 0,9 Megapixel (1280x704 bei 16:9), 1080p etwa 2 Megapixel (1920x1088 bei 16:9) (Standard: `"720p"`). | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `model.fps` | Frames pro Sekunde. 48 fps ist mit Draft bei 1080p nicht verfügbar (Standard: `"24"`). | COMBO | Ja | `"24"`<br>`"48"` |
| `model.draft` | Schnelleres, weniger detailliertes Rendering, das zu einem niedrigeren Tarif als ein Standard-Rendering abgerechnet wird (Standard: False). | BOOLEAN | Ja | True/False |
| `model.generate_audio` | Erzeugt eine Tonspur für das Video. Wird ignoriert, wenn `model.audio` verbunden ist; diese wird dann stattdessen zur Tonspur (Standard: True). | BOOLEAN | Ja | True/False |
| `model.enhance_prompt` | Schreibt den Prompt vor der Generierung detaillierter um; kurze Prompts benötigen dies. Deaktivieren Sie es, um ein Ergebnis mit demselben Seed exakt zu reproduzieren (Standard: True). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.audio` | Audio, das die Bewegung antreibt und zur Tonspur wird. Mindestens 1 Sekunde lang; Audio, das länger als 20 Sekunden ist, wird abgeschnitten. Legt die Videolänge anstelle von `model.duration` fest. | AUDIO | Nein | - |
| `model.seed` | Seed für die Generierung. Derselbe Seed reproduziert ein Ergebnis nur dann exakt, wenn `model.enhance_prompt` deaktiviert ist (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Hinweise:**

- `model.first_frame` ist erforderlich und legt das Seitenverhältnis der Ausgabe fest, daher hat dieser Node keine Eingabe für das Seitenverhältnis.
- `model.last_frame` ist optional, aber sein Seitenverhältnis muss nahe am Seitenverhältnis des ersten Einzelbildes liegen, sonst löst der Node einen Fehler aus.
- `model.prompt` ist erforderlich und auf 5000 Zeichen begrenzt.
- Draft bei 1080p kann nicht mit 48 fps kombiniert werden: Der Node löst einen Fehler aus; deaktivieren Sie also entweder Draft oder verwenden Sie 24 fps.
- Verbundenes Audio muss mindestens 1 Sekunde lang sein; alles über 20 Sekunden wird ignoriert.
- Wenn `model.audio` verbunden ist, legt das Audio die Videolänge fest, daher haben `model.duration` und `model.generate_audio` keine Auswirkung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das generierte Video mit seiner Tonspur. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `da8952e478eee593543fa7ae1aa329ad5bd5078024f905cdba185d18e76db130`
