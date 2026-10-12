# Flux2Scheduler

Flux2Scheduler erzeugt eine Folge von Rauschpegeln (Sigmas) für den Entrauschungsprozess, die speziell auf das Flux-Modell zugeschnitten ist. Er berechnet einen Zeitplan basierend auf der Anzahl der Entrauschungsschritte und den Abmessungen des Zielbilds, was den Fortschritt der Rauschentfernung während der Bilderzeugung beeinflusst.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `steps` | Die Anzahl der durchzuführenden Entrauschungsschritte. Ein höherer Wert führt in der Regel zu detaillierteren Ergebnissen, benötigt jedoch mehr Verarbeitungszeit (Standard: 20). | INT | Ja | 1 bis 4096 |
| `width` | Die Breite des zu erzeugenden Bildes in Pixeln. Dieser Wert beeinflusst die Berechnung des Rausch-Zeitplans (Standard: 1024). | INT | Ja | 16 bis 16384 |
| `height` | Die Höhe des zu erzeugenden Bildes in Pixeln. Dieser Wert beeinflusst die Berechnung des Rausch-Zeitplans (Standard: 1024). | INT | Ja | 16 bis 16384 |

Hinweis: Der Zeitplan wird aus der Länge der Bildsequenz berechnet, die sich aus `width` und `height` als `(width * height) / 256` ergibt; dies spiegelt das 16-fache latente Downsampling des Modells wider. Größere Bilder erzeugen längere Sequenzen, wodurch sich der Rausch-Zeitplan entsprechend verschiebt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Eine Folge von Rauschpegelwerten (`sigmas`), die den Entrauschungs-Zeitplan für den Sampler definieren. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/de.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
