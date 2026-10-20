# FLUX 3 Max Text to Video

FLUX 3 Max Text to Video erzeugt aus einem Text-Prompt ein Video mit synchronisiertem Audio. Der Prompt wird von FLUX 3 Max interpretiert und erweitert, bevor das Rendering beginnt; der Node wartet, bis das Rendering abgeschlossen ist, und gibt den fertigen Clip zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Was der Clip zeigen soll, in einfacher Sprache. Beschreiben Sie Umgebungsgeräusche, Musik und Sprache getrennt, um geschichtetes Audio zu erhalten (Standard: leer). | STRING | Ja | Mehrzeiliger Text |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. `"auto"` entspricht bei Text-Prompts 16:9 (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Länge des Clips in Sekunden (Standard: `"5"`). | COMBO | Ja | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Auflösung der Ausgabe (Standard: `"720p"`). | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Wie stark das Modell den Prompt vor der Generierung durchdenkt und erweitert. `"high"` dauert länger; der Preis bleibt gleich (Standard: `"high"`). | COMBO | Ja | `"low"`<br>`"high"` |
| `generate_audio` | Synchronisiertes Audio generieren. Aus erzeugt ein Video ohne Audiospur (Standard: true). | BOOLEAN | Ja | `true`<br>`false` |
| `seed` | Seed, der steuert, ob der Node erneut ausgeführt wird. Die Ergebnisse sind unabhängig von diesem Wert nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 2147483646 |

Hinweis: `prompt` muss mindestens ein Zeichen enthalten. Der angezeigte Preis richtet sich nach `resolution` und `duration`: 720p wird mit 0,060775 USD pro Sekunde und 1080p mit 0,103675 USD pro Sekunde berechnet, bis zum 7. November 2026; danach mit 0,2431 USD bzw. 0,4147 USD pro Sekunde. Die geschätzten Gesamtkosten für den Clip werden in der Benutzeroberfläche angezeigt.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Der generierte Videoclip, mit synchronisiertem Audio, wenn `generate_audio` aktiviert ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `6dcb11e7aa7f1592169ede449c4092740db43e635501205eba02a066f03a967f`
