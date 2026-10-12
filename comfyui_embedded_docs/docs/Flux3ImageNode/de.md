# Flux3ImageNode

Flux 3 Image erzeugt mit FLUX 3 aus einem Prompt ein Bild oder bearbeitet und kombiniert Referenzbilder. Schreiben Sie als Anweisung, was Sie möchten, verbinden Sie dann bis zu 10 Referenzbilder und verweisen Sie im Prompt mit image 1, image 2 usw. auf sie. Der Prompt wird vor der Generierung interpretiert und erweitert, und das Ergebnis wird im gewählten Seitenverhältnis und in der gewählten Auflösung gerendert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Was generiert oder welche Bearbeitung durchgeführt werden soll. Der Prompt wird vor der Generierung interpretiert und erweitert. Verweisen Sie auf verbundene Referenzbilder als image 1, image 2 usw. (Standard: "") | STRING | Ja | 1 bis 15000 Zeichen |
| `images` | Erweiterbarer Slot für Referenzbilder; insgesamt bis zu 10 verbinden. Jedes Bild muss mindestens 256x256 Pixel groß sein, und sein Seitenverhältnis darf nicht extremer als 64:1 sein. | IMAGE | Nein | 0 bis 10 Bilder |
| `bounding_boxes` | Optionale Boxen aus dem Create Bounding Boxes-Node, die Objekte oder Text in der Ausgabe platzieren. Die Positionen beziehen sich auf die Leinwand, daher übergeben Sie dem Node das Seitenverhältnis der Ausgabe. | ARRAY | Nein | - |
| `aspect_ratio` | Seitenverhältnis des generierten Bildes. "auto" folgt dem ersten Referenzbild oder wählt ein Verhältnis aus dem Prompt. (Standard: "auto") | COMBO | Ja | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"7:5"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"5:7"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"9:21"` |
| `resolution` | Ausgabegröße beim gewählten Seitenverhältnis: 0,75K entspricht etwa 0,6 Megapixeln, 1K 1 MP, 1,5K 2,4 MP, 2K 4,2 MP, 4K 16,8 MP. (Standard: "2K") | COMBO | Ja | `"0.75K"`<br>`"1K"`<br>`"1.5K"`<br>`"2K"`<br>`"4K"` |
| `grounding` | Lässt das Modell den Prompt vor der Generierung mit Web- und Bildsuche recherchieren. (Standard: True) | BOOLEAN | Ja | True<br>False |
| `safety_tolerance` | Moderationstoleranz; 0 ist am strengsten. (Standard: 4) | INT | Ja | 0 bis 4 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; FLUX 3 wählt seinen eigenen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 4294967295 |

`safety_tolerance` ist eine erweiterte Eingabe, und `seed` enthält in der Benutzeroberfläche Steuerelemente für „Control After Generate“.

Referenzbilder werden hochgeladen, bevor die Anfrage gesendet wird. Ein einzelner Slot kann einen Batch aufnehmen, und jedes Einzelbild jedes Batches zählt zum Limit von 10 Bildern.

Zeilen von `bounding_boxes` werden an den Prompt angehängt, daher müssen der Prompt und die Box-Beschreibungen zusammen höchstens 15000 Zeichen umfassen.

Der angezeigte Preis hängt von `resolution` ab: $0.05863 bei 0,75K, $0.06864 bei 1K, $0.1001 bei 1,5K, $0.143 bei 2K und $0.86801 bei 4K.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `IMAGE` | Das generierte Bild, heruntergeladen aus dem FLUX 3-Ergebnis. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageNode/de.md)

---
**Source fingerprint (SHA-256):** `f32a90887227f9ce9e6ed04a76cde452a70f36fb97d8c36d7c55140855c1f593`
