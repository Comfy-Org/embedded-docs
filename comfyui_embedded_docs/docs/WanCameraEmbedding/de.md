# WanCameraEmbedding

Dieser Node erzeugt ein Kamera-Trajektorien-Embedding unter Verwendung von Plücker-Embeddings für den gewählten Kamerapfad. Er erstellt eine Sequenz von Kameraposen, die Bewegungen wie Schwenken, Zoomen oder Drehen simulieren, und wandelt diese in einen Embedding-Tensor um, der in Videogenerierungs-Pipelines verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `camera_pose` | Der Typ der zu simulierenden Kamerabewegung (Standard: "Static") | COMBO | Ja | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `width` | Die Breite der Ausgabe in Pixeln (Standard: 832, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Die Höhe der Ausgabe in Pixeln (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Die Länge der Kamera-Trajektoriensequenz (Standard: 81, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `speed` | Die Geschwindigkeit der Kamerabewegung (Standard: 1.0, Schritt: 0.1) | FLOAT | Nein | 0.0 bis 10.0 |
| `fx` | Der Brennweitenparameter x (Standard: 0.5, Schritt: 0.000000001) | FLOAT | Nein | 0.0 bis 1.0 |
| `fy` | Der Brennweitenparameter y (Standard: 0.5, Schritt: 0.000000001) | FLOAT | Nein | 0.0 bis 1.0 |
| `cx` | Die x-Koordinate des Hauptpunkts (Standard: 0.5, Schritt: 0.01) | FLOAT | Nein | 0.0 bis 1.0 |
| `cy` | Die y-Koordinate des Hauptpunkts (Standard: 0.5, Schritt: 0.01) | FLOAT | Nein | 0.0 bis 1.0 |

Hinweis: `fx`, `fy`, `cx` und `cy` sind erweiterte intrinsische Kameraparameter. Der Parameter `speed` skaliert den Rotationswinkel und die Translationsdistanz der ausgewählten Kamerabewegung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `camera_embedding` | Der erzeugte Kamera-Embedding-Tensor, der die Trajektoriensequenz enthält | TENSOR |
| `width` | Der Breitenwert, der für die Verarbeitung verwendet wurde | INT |
| `height` | Der Höhenwert, der für die Verarbeitung verwendet wurde | INT |
| `length` | Der Längenwert, der für die Verarbeitung verwendet wurde | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/de.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
