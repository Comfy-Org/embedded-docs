# RTDETR_detect

Der Node RT-DETR Detect führt eine Objekterkennung auf Eingabebildern mithilfe eines RT-DETR-Modells durch. Er identifiziert Objekte, gibt Bounding Boxes um sie herum zurück und kennzeichnet sie gemäß den Klassen des COCO-Datensatzes. Sie können die Ergebnisse nach Konfidenzwert und Objektklasse filtern und die Gesamtzahl der Erkennungen begrenzen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das für die Objekterkennung verwendete RT-DETR-Modell. | MODEL | Ja | N/A |
| `image` | Das/die Eingabebild(er), in dem/denen Objekte erkannt werden sollen. Der Node verarbeitet Bilder in Stapeln von bis zu 32. | IMAGE | Ja | N/A |
| `threshold` | Der minimale Konfidenzwert, den eine Erkennung aufweisen muss, um in die Ergebnisse aufgenommen zu werden (Standard: 0.5). | FLOAT | Ja | N/A |
| `class_name` | Filtert Erkennungen nach Klasse. Auf 'all' setzen, um die Filterung zu deaktivieren (Standard: "all"). | COMBO | Ja | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | Maximale Anzahl der pro Bild zurückzugebenden Erkennungen. In absteigender Reihenfolge des Konfidenzwerts (Standard: 100). | INT | Ja | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `bboxes` | Eine Liste von Bounding Boxes für jedes Eingabebild. Jede Box enthält Koordinaten (x, y, width, height), ein Klassenlabel und einen Konfidenzwert. | BOUNDINGBOX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/de.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
