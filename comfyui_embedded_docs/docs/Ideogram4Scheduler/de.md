# Ideogram 4 Scheduler

Der Node Ideogram 4 Scheduler erzeugt eine Sequenz von Sigma-Werten (Rauschpegeln) für den Diffusions-Sampling-Prozess, basierend auf dem Ideogram-4-Referenzzeitplan. Er erstellt einen benutzerdefinierten Rauschplan, der sich an die Bildabmessungen anpasst und eine Feinabstimmung über statistische Parameter ermöglicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `steps` | Die Anzahl der Sampling-Schritte, für die der Zeitplan erzeugt wird (Standard: 20). Die Ausgabe enthält `steps + 1` Sigma-Werte. | INT | Ja | 1 bis 200 |
| `width` | Die Breite des Bildes in Pixeln (Standard: 1024). Die Auflösung relativ zu einer 512×512-Referenz verschiebt den Rauschplan. | INT | Ja | 256 bis 8192 (Schritt: 16) |
| `height` | Die Höhe des Bildes in Pixeln (Standard: 1024). Die Auflösung relativ zu einer 512×512-Referenz verschiebt den Rauschplan. | INT | Ja | 256 bis 8192 (Schritt: 16) |
| `mu` | Der Mittelwertparameter für die logit-normale Verteilung, der den zentralen Rauschpegel steuert. Wird mit dem Auflösungsterm kombiniert, um die logSNR-Verschiebung zu bilden (Standard: 0.0). | FLOAT | Ja | -10.0 bis 10.0 (Schritt: 0.05) |
| `std` | Der Standardabweichungsparameter für die logit-normale Verteilung, der die Streuung der Rauschpegel steuert (Standard: 1.75). | FLOAT | Ja | 0.1 bis 5.0 (Schritt: 0.05) |

Hinweis: Der Zeitplan wird aus einer logit-normalen Verteilung über die Referenzzeit abgeleitet. Ein Auflösungsterm gleich `0.5 * log((width × height) / (512 × 512))` wird zu `mu` addiert, sodass größere oder kleinere Bilder den Zeitplan relativ zu einer 512×512-Referenz bei demselben `mu`-Wert verschieben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `SIGMAS` | Ein Tensor aus Sigma-Werten, der den Rauschplan repräsentiert, mit einer Länge gleich `steps + 1`. Die Werte fallen von hohem Rauschen zu niedrigem Rauschen ab, wobei der letzte Wert auf 0.0 für vollständige Entrauschung gesetzt ist. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/de.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
