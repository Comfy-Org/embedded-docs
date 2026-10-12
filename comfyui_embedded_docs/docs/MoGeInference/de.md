# MoGeInference

Führen Sie MoGe auf Bildern aus, um Tiefe und Geometrie zu schätzen. Dieser Node verarbeitet ein Eingabebild mit dem MoGe-Modell, um eine 3D-Punktwolke, eine Tiefenkarte, Kamera-Intrinsics, eine Maske und Oberflächennormalen zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `moge_model` | Das MoGe-Modell, das für die Inferenz verwendet werden soll. | MOGE_MODEL | Ja | N/A |
| `image` | Das Eingabebild für die Tiefen- und Geometrieschätzung. Es werden nur die ersten drei Farbkanäle (RGB) verwendet. | IMAGE | Ja | N/A |
| `resolution_level` | Steuert die Verarbeitungsauflösung. 0 = am schnellsten, 9 = maximales Detail. (Standard: 9) | INT | Ja | 0 bis 9 |
| `fov_x_degrees` | (Erweitert) Horizontales Sichtfeld der Quellkamera. Legt die Brennweite fest, die verwendet wird, um die Tiefenkarte in 3D zurückzuprojizieren. 0 = automatische Wiederherstellung aus den vorhergesagten Punkten. (Standard: 0.0) | FLOAT | Ja | 0.0 bis 170.0 (Schrittweite 0.1) |
| `batch_size` | Bilder pro Inferenzaufruf. Verringern Sie den Wert, wenn bei einem langen Video / Bildsatz der Speicher ausgeht (OOM). (Standard: 4) | INT | Ja | 1 bis 64 |
| `force_projection` | (Erweitert) Erzwingt die Projektion der vorhergesagten Punkte. (Standard: True) | BOOLEAN | Ja | True/False |
| `apply_mask` | (Erweitert) Setzt maskierte (Himmel / ungültige) Pixel in Punkten und Tiefe auf inf, damit das Meshing sie aussortiert. Deaktivieren Sie dies, um die rohe vorhergesagte Geometrie überall beizubehalten; die Maske wird trotzdem separat zurückgegeben. (Standard: True) | BOOLEAN | Ja | True/False |
| `refine_steps` | (Erweitert) Nur MoGe-3: sparse volumetrische Verfeinerungsdurchläufe über die vorhergesagte Tiefe. Mehr Durchläufe schärfen feine Details und Kanten bei ungefähr linearen Kosten. 0 deaktiviert die Verfeinerung. Wird von MoGe-1 / MoGe-2 ignoriert. (Standard: 3) | INT | Ja | 0 bis 8 |

Hinweis: Wenn die Eingabe `image` mehr Frames enthält als `batch_size`, verarbeitet der Node sie in mehreren Inferenzaufrufen und kombiniert die Ergebnisse zu einer einzigen Ausgabegeometrie.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `moge_geometry` | Ein Dictionary, das die geschätzte Geometrie enthält. Es enthält das ursprüngliche `image` und kann `points` (3D-Punktwolke), `depth` (Tiefenkarte), `intrinsics` (Kamera-Intrinsics-Matrix), `mask` (Maske, die gültige Pixel identifiziert) und `normal` (Oberflächennormalen) enthalten. | MOGE_GEOMETRY |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/de.md)

---
**Source fingerprint (SHA-256):** `10f3399d9b6bc4ff8a940c940f538a8ec8f38a15e7d65f162499c5ab264fad65`
