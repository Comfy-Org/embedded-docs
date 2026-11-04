# Pika H3 Flex Video

Dieser Node erzeugt ein Video mit synchronisiertem Audio aus einem Text-Prompt, optional verankert durch ein erstes Bild, ein letztes Bild oder beides. Pika H3 Flex ist Pikas nachtrainiertes MiniMax H3-Modell: Es rendert das Bild und seinen Ton in einem Durchgang, und Sie legen Auflösung, Seitenverhältnis und Dauer fest. Ohne angeschlossenes Bild arbeitet der Node als Text-zu-Video; das Anschließen eines Bildes schaltet ihn auf Bild-zu-Video um.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Was im Video passiert, einschließlich des gewünschten Tons. Darf nicht leer sein. Standard: "" (leere Zeichenkette). | STRING | Ja | 1 bis 8000 Zeichen |
| `first_frame` | Optionales Bild, das als Anfangsbild verwendet wird. Wird es angeschlossen, läuft der Node als Bild-zu-Video statt als Text-zu-Video. | IMAGE | Nein | - |
| `last_frame` | Optionales Bild, das als Schlussbild verwendet wird. Kann zusammen mit `first_frame` oder allein verwendet werden. | IMAGE | Nein | - |
| `resolution` | Ausgabeauflösung. `"1080p"` und höher werden bei 768p gerendert und einmal hochskaliert. Derselbe Seed bei 480p ergibt ein anderes Video. Standard: `"768p"`. | COMBO | Ja | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. `"auto"` folgt dem ersten angeschlossenen Bild, andernfalls dem Prompt. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Clip-Länge in Sekunden. Die Ausgabelänge folgt einem Frame-Raster: 5 Sekunden ergeben 124 Frames, also etwa 5,17 Sekunden. Standard: 5. | INT | Ja | 5 bis 15 Sekunden |
| `rewrite_prompt` | Lässt Pika den Prompt zuerst erweitern. Derselbe Seed ergibt dann bei jedem Lauf ein anderes Video. Standard: False. | BOOLEAN | Ja | true<br>false |
| `seed` | Seed für die Stichprobenentnahme. Bei deaktiviertem `rewrite_prompt` wiederholt derselbe Seed das Video exakt, wobei ein lokaler Lauf mit demselben Seed ein anderes Ergebnis liefert. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:**

* Der Prompt muss zwischen 1 und 8000 Zeichen lang sein.
* Die Abrechnung richtet sich nach der gewählten Auflösung und der Clip-Länge und wird pro Sekunde der Ausgabe gezählt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Der erzeugte Clip mit seinem synchronisierten Audio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `63a90fc5874ed861db3c0821e702cfcd1a14650f09459b242b4ec5e3ba5b0cd5`
