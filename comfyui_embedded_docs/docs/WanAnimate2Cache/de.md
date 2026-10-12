# WanAnimate2Cache

Die Aktivierungen des Pose-Videos werden pro Block einmalig zwischengespeichert, sodass sie nicht bei jedem Sampling-Schritt neu berechnet werden müssen, was die Generierungszeit ungefähr halbiert. Der Kompromiss ist ein zusätzlicher Speicherverbrauch: etwa 12,5 GB System-RAM bei einer Auflösung von 480x832 mit 81 Frames in bf16, der mit Auflösung und Videolänge skaliert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Wan Animate2-Modell, an das der Cache angehängt wird. | MODEL | Ja | |
| `device` | Wo der Cache gehalten werden soll. cpu (RAM) ist die sichere Wahl; der Cache passt bei typischen Größen nicht zusammen mit dem Modell in den VRAM. gpu (VRAM) kann schneller sein, wenn der Cache hineinpasst. (Standard: "cpu") | STRING | Ja | "cpu"<br>"gpu" |
| `dtype` | Speicherpräzision. Der Wert default speichert die Aktivierungen im Compute-Datentyp des Modells. int8 halbiert den Cache, int4 viertelt ihn, convrot wird verwendet, um die Genauigkeit zu erhalten. (Standard: "default") | STRING | Ja | "default"<br>"int8"<br>"int4" |

Hinweis: Wenn Kontextfenster verwendet werden, wird jedes Fenster separat zwischengespeichert, sodass der Speicherverbrauch mit der Anzahl der Fenster skaliert. Der static_standard-Zeitplan sollte verwendet werden, weil gleichmäßige Zeitpläne die Fenster bei jedem Schritt verschieben und der Cache nie wiederverwendet wird.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model` | Das geklonte Modell mit angehängtem Aktivierungs-Cache des Pose-Videos. Der Cache wird automatisch freigegeben, wenn die Generierung abgeschlossen ist. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/de.md)

---
**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`
