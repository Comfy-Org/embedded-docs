# Meta Muse Text zu Bild

Meta Muse Image Text to Image erzeugt Bilder aus einem Text-Prompt unter Verwendung von Metas Muse Image-Modell. Das Modell reflektiert den Prompt vor dem Rendern und kann während der Planung des Bildes Websuche, Bildsuche und Codeausführung verwenden. Der Node ruft die Muse Image API auf und gibt das resultierende Bild oder die resultierenden Bilder zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. | DYNAMIC_COMBO | Ja | `"muse-image-1.0"` |

Wenn Sie ein Modell in der Liste auswählen, werden die Einstellungen angezeigt, die dieses Modell unterstützt. Das einzige verfügbare Modell ist `muse-image-1.0`; seine Einstellungen sind unten aufgeführt.

### muse-image-1.0 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der das Bild beschreibt. Das Modell reflektiert den Prompt und kann vor dem Rendern seine integrierte Web- und Bildsuche verwenden. | STRING | Ja | Mehrzeiliger Text, mindestens 1 Zeichen |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. Bilder werden mit etwa 2,5 Megapixeln gerendert (1:1 ist 1600x1600, 16:9 ist 2048x1152); „auto“ lässt das Modell anhand des Prompts wählen. | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | Wie stark das Modell nachdenkt, plant und sich vor dem Rendern selbst verfeinert. | COMBO | Ja | `"high"`<br>`"low"` |
| `enable_web_search` | Lässt das Modell während der Planung des Bildes das Web nach Fakten und aktuellen Informationen durchsuchen. | BOOLEAN | Nein | True<br>False (Standard: True) |
| `enable_image_search` | Lässt das Modell während der Planung des Bildes nach Referenzbildern suchen. | BOOLEAN | Nein | True<br>False (Standard: True) |
| `enable_shell` | Lässt das Modell während der Planung Code ausführen, für präzise Layouts, Diagramme und Schaubilder; wenn deaktiviert, werden Mengen und Ausrichtung angenähert. | BOOLEAN | Nein | True<br>False (Standard: True) |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die API hat keinen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. | INT | Ja | 0 – 2147483647 (Standard: 42) |

Hinweis: Der Prompt muss mindestens ein Zeichen enthalten. Wenn `aspect_ratio` auf „auto“ gesetzt ist, wird keine explizite Größe an die API gesendet und das Modell entscheidet die Ausgabegröße anhand des Prompts. Der Parameter `seed` steuert nur, wann der Node erneut ausgeführt wird; er wird nicht an die API gesendet, sodass die generierten Ergebnisse nicht deterministisch sind.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das von der API zurückgegebene generierte Bild, dekodiert und als Batch-Bild bereitgestellt. Wenn die API-Antwort mehrere Bilder enthält, werden sie zu einem Batch zusammengefasst. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/de.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`
