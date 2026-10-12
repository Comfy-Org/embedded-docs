# LtxvApiTextToVideo

Der Node LTXV Text To Video erzeugt Videos in professioneller Qualität aus einer Textbeschreibung. Er verbindet sich mit einer externen API, um Videos mit anpassbarer Dauer, Auflösung und Bildrate zu erstellen. Sie können außerdem festlegen, dass dem Video KI-generiertes Audio hinzugefügt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das KI-Modell, das für die Videogenerierung verwendet werden soll. "LTX-2 (Pro)" bietet höhere Qualität, während "LTX-2 (Fast)" für Geschwindigkeit optimiert ist. | COMBO | Ja | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Die Textbeschreibung, die die KI zur Generierung des Videos verwendet. Dieses Feld unterstützt mehrzeiligen Text und muss 1 bis 10.000 Zeichen enthalten. Standard: "" (leer). | STRING | Ja | - |
| `duration` | Die Länge des generierten Videos in Sekunden (Standard: 8). | COMBO | Ja | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | Die Pixelabmessungen (Breite x Höhe) des Ausgabevideos. | COMBO | Ja | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Die Bilder pro Sekunde für das Video (Standard: 25). | COMBO | Ja | `25`<br>`50` |
| `generate_audio` | Wenn true, enthält das generierte Video KI-generiertes Audio, das zur Szene passt (Standard: False). Dies ist eine erweiterte optionale Einstellung. | BOOLEAN | Nein | - |

**Wichtige Einschränkungen:**

* Der `prompt` muss zwischen 1 und 10.000 Zeichen lang sein.
* Wenn Sie eine `duration` von mehr als 10 Sekunden auswählen, müssen Sie außerdem das Modell `"LTX-2 (Fast)"`, eine Auflösung von `"1920x1080"` und eine `fps` von `25` verwenden. Diese Kombination ist für längere Videos erforderlich.
* Der Preis hängt vom ausgewählten `model`, `duration` und `resolution` ab.

**Hinweis:** Dieser Node ist veraltet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/de.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`
