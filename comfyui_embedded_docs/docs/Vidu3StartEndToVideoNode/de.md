# Vidu3StartEndToVideoNode

Dieser Node generiert ein Video, indem er einen Übergang zwischen einem Startbild und einem Endbild erzeugt, der durch einen Text-Prompt gesteuert wird. Er verwendet das Vidu-Q3-Modell, um zwischen den beiden Bildern zu interpolieren, und erzeugt ein Video mit der gewählten Dauer und Auflösung.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell zur Videogenerierung. Durch Auswahl einer Option werden zusätzliche Konfigurationsparameter für `resolution`, `duration` und `audio` angezeigt. | DYNAMIC_COMBO | Ja | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `first_frame` | Das Startbild der Videosequenz. | IMAGE | Ja | - |
| `end_frame` | Das Endbild der Videosequenz. | IMAGE | Ja | - |
| `prompt` | Prompt-Beschreibung (max. 2000 Zeichen). | STRING | Ja | Bis zu 2000 Zeichen |
| `seed` | Seed-Wert zur Steuerung der Zufälligkeit der Generierung. Verfügt über eine Option zur Steuerung nach der Generierung (Standard: 1). | INT | Ja | 0 bis 2147483647 |

### viduq3-pro und viduq3-turbo Eingaben

Die folgenden Parameter werden von beiden Modelloptionen (`viduq3-pro` und `viduq3-turbo`) gemeinsam verwendet. Sie erscheinen, nachdem ein Modell ausgewählt wurde.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 1 bis 16 |
| `audio` | Wenn aktiviert, wird ein Video mit Ton ausgegeben (einschließlich Dialogen und Soundeffekten) (Standard: False). | BOOLEAN | Ja | `True`<br>`False` |

**Hinweis:** Die Bilder `first_frame` und `end_frame` müssen ähnliche Seitenverhältnisse aufweisen. Das Seitenverhältnis der beiden Bilder muss innerhalb von 80 % bis 125 % des jeweils anderen liegen (relative Nähe zwischen 0,8 und 1,25).

**Hinweis:** Für `viduq3-turbo` beträgt der Preis 0,06 USD pro Sekunde bei 720p und 0,08 USD pro Sekunde bei 1080p. Für `viduq3-pro` beträgt der Preis 0,15 USD pro Sekunde bei 720p und 0,16 USD pro Sekunde bei 1080p.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
