# Flux 3 Text zu Video

Erzeugt ein Video mit synchronisiertem Audio aus einem Text-Prompt unter Verwendung von FLUX 3. Der Node sendet Ihren Prompt an den FLUX 3-Dienst, wartet, bis die Generierung abgeschlossen ist, und gibt den fertigen Videoclip zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Was Sie möchten, in einfacher Sprache; der Prompt wird vor der Generierung interpretiert und erweitert. Beschreiben Sie Umgebungsgeräusche, Musik und Sprache getrennt, um mehrschichtiges Audio zu erhalten. (Standard: "") | STRING | Ja | Mehrzeiliger Text |
| `aspect_ratio` | Ausgabe-Seitenverhältnis. 'auto' wählt eines anhand des Prompts und der Eingaben aus. (Standard: "auto") | COMBO | Ja | Mehrere Optionen verfügbar, einschließlich `"auto"` |
| `duration` | Cliplänge in Sekunden. 'auto' passt die Länge an den Inhalt an. (Standard: "auto") | COMBO | Ja | Mehrere Optionen verfügbar, einschließlich `"auto"` |
| `resolution` | Ausgabeauflösung. (Standard: "720p") | COMBO | Ja | `"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` |
| `generate_audio` | Synchronisiertes Audio erzeugen (Umgebungsgeräusche, Sprache, Effekte). Wenn deaktiviert, wird ein Video ohne Audiospur erzeugt. (Standard: True) | BOOLEAN | Ja | True<br>False |
| `safety_tolerance` | Moderations-Toleranz, 0 ist die strengste. Anfragen, die Bilder oder Videos senden, werden auf 2 begrenzt, unabhängig davon, was Sie hier einstellen. (Standard: 2) | INT | Ja | 0 bis 4 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; FLUX 3 wählt seinen eigenen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 4294967295 |

Hinweis: `safety_tolerance` ist eine erweiterte Eingabe. Die Eingabe `seed` enthält in der Benutzeroberfläche die Steuerelemente für „Control After Generate“. Der angezeigte Preis basiert auf `resolution` und `duration`: HD (720p) wird mit 0,2431 $ pro Sekunde und FHD (1080p) mit 0,4147 $ pro Sekunde berechnet. QHD (1440p) kostet 0,572 $ pro Sekunde, UHD (2160p) 1,144 $ pro Sekunde. Wenn eine feste Dauer gewählt wird, werden die geschätzten Gesamtkosten für den Clip angezeigt; wenn `duration` auf "auto" gesetzt ist, wird der Preis pro Sekunde angezeigt.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
|------------------|--------------|----------|
| `video` | Der erzeugte Videoclip, mit synchronisiertem Audio, wenn `generate_audio` aktiviert ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `2fa8c715c8467e2a2a3e131875d3b459a5599c2bab550656670aa1461e896aab`
