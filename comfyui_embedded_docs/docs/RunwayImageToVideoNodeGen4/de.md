# RunwayImageToVideoNodeGen4

Der Node Runway Image to Video (Gen4 Turbo) generiert aus einem einzelnen Startframe mithilfe von Runways Gen4 Turbo-Modell ein Video. Er nimmt einen Text-Prompt und einen anfänglichen Bildframe entgegen und erstellt dann eine Videosequenz basierend auf den angegebenen Einstellungen für Dauer und Seitenverhältnis. Der Node übernimmt das Hochladen des Startframes an die Runway-API und gibt das generierte Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Generierung (Standard: leerer String) | STRING | Ja | - |
| `start_frame` | Startframe, der für das Video verwendet wird | IMAGE | Ja | - |
| `duration` | Videodauer in Sekunden | COMBO | Ja | `"5"`<br>`"10"` |
| `ratio` | Seitenverhältnis für das generierte Video (Standard: "1280:720") | COMBO | Ja | `"1280:720"`<br>`"720:1280"`<br>`"1104:832"`<br>`"832:1104"`<br>`"960:960"`<br>`"1584:672"` |
| `seed` | Zufälliger Seed für die Generierung (Standard: 0) | INT | Nein | 0 bis 4294967295 |

**Parametereinschränkungen:**

- Das `start_frame`-Bild darf die Abmessungen 7999x7999 Pixel nicht überschreiten
- Das `start_frame`-Bild muss ein Seitenverhältnis zwischen 0,5 und 2,0 aufweisen
- Der `prompt` muss mindestens ein Zeichen enthalten

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video basierend auf dem Eingabeframe und dem Prompt | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/de.md)

---
**Source fingerprint (SHA-256):** `1cbf70391f1dfd0f40a3085dad68b98ec20e964eab7d4a17b2fb3cd07a035277`
