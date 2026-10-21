# Flux 3 Videofortsetzung

Dieser Node setzt einen vorhandenen Videoclip mit FLUX 3 fort: Der neue Clip knüpft an die letzten Frames des von Ihnen bereitgestellten Videos an. Er lädt Ihren Quellclip hoch, sendet den Prompt und die Einstellungen an den Generierungsdienst und gibt das resultierende Fortsetzungsvideo zurück, sobald es fertig ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `video` | Der fortzusetzende Clip. Clips mit mehr als 3840x2160 Pixeln Fläche werden passend herunterskaliert. | VIDEO | Ja | Einzelner Videoclip |
| `prompt` | Was die Fortsetzung zeigen soll; der Prompt wird vor der Generierung interpretiert und erweitert. (Standard: "") | STRING | Ja | Nichtleerer Text (mindestens 1 Zeichen) |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. 'auto' wählt eines anhand des Prompts und der Eingaben aus. (Standard: "auto") | COMBO | Ja | "auto" (Standard)<br>Mehrere vordefinierte Optionen |
| `duration` | Cliplänge in Sekunden. 'auto' passt die Länge an den Inhalt an. (Standard: "auto") | COMBO | Ja | "auto" (Standard)<br>Numerische Werte in Sekunden |
| `resolution` | Auflösung der Ausgabe. (Standard: "720p") | COMBO | Ja | "720p" (Standard)<br>"1080p"<br>"1440p"<br>"2160p" |
| `generate_audio` | Synchronisiertes Audio erzeugen (Umgebungsgeräusche, Sprache, Effekte). Aus erzeugt ein Video ohne Audiospur. (Standard: true) | BOOLEAN | Ja | true<br>false |
| `safety_tolerance` | Moderationstoleranz; 0 ist die strengste Stufe. Anfragen, die Bilder oder Videos senden, werden unabhängig von der hier festgelegten Einstellung auf 2 begrenzt. (Erweiterter Parameter, Standard: 2) | INT | Ja | 0 - 4 (effektives Maximum: 2 für Videoanfragen) |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; FLUX 3 wählt seinen eigenen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. (Standard: 42) | INT | Ja | 0 - 4294967295 (0xFFFFFFFF) |

### Hinweise

- `prompt` muss mindestens ein Zeichen enthalten, sonst schlägt die Generierung fehl. Obwohl das Feld standardmäßig eine leere Zeichenkette enthält, ist ein nicht leerer Prompt erforderlich, um den Node auszuführen.
- `safety_tolerance` akzeptiert jeden Wert von 0 bis 4, aber da dieser Node ein Video an die API sendet, ist die effektive Toleranz unabhängig vom ausgewählten Wert auf 2 begrenzt.
- Wenn `duration` auf eine Zahl gesetzt wird, wird sie in eine ganzzahlige Anzahl von Sekunden umgewandelt. Der spezielle Wert "auto" lässt den Dienst die Länge an den Inhalt anpassen.
- Die genauen Optionslisten für `aspect_ratio`, `duration` und `resolution` werden intern vom Node definiert. `resolution` bietet "720p" (Standard), "1080p", "1440p" und "2160p". Die Preisberechnung basiert auf der ausgewählten `resolution` und `duration`: "720p" wird mit 0,5863 USD pro Sekunde abgerechnet, "1080p" mit 0,7579 USD, "1440p" mit 0,9295 USD und "2160p" mit 1,3585 USD.
- `seed` steuert nur, ob der Node erneut ausgeführt wird; er wird nicht an den Generierungsdienst gesendet.
- Authentifizierungs- und Node-Identifikationsfelder (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) sind ausgeblendet und werden automatisch von der Plattform verwaltet.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
|------------------|--------------|----------|
| `video` | Der von FLUX 3 erzeugte Fortsetzungsclip, der an das Ende des Quellvideos anknüpft. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/de.md)

---
**Source fingerprint (SHA-256):** `112004aa664617ce23adba425705327898a1f7632c8d3e8fa4f9ae3e7620776b`
