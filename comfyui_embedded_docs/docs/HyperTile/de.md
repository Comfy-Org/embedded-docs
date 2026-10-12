# HyperTile

HyperTile wendet eine Tiling-Technik auf den Attention-Mechanismus in Diffusionsmodellen an, um den Speicherverbrauch während der Bilderzeugung zu reduzieren. Es teilt den latenten Raum in kleinere Kacheln auf, verarbeitet die Attention für jede Kachel separat und setzt die Ergebnisse anschließend wieder zusammen. Dadurch können größere Bildgrößen verwendet werden, ohne dass der Speicher ausgeht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das die HyperTile-Optimierung angewendet werden soll | MODEL | Ja | - |
| `tile_size` | Die Ziel-Kachelgröße für die Verarbeitung (Standard: 256). Intern wird der Wert auf einen Mindestwert von 32 begrenzt und dann durch 8 geteilt, um die effektive Kachelgröße zu erhalten. | INT | Ja | 1 - 2048 |
| `swap_size` | Steuert, wie die Kacheln während der Verarbeitung neu angeordnet werden, um die Effizienz zu verbessern. Größere Werte ermöglichen mehr Variation bei den Kachelgrößen (Standard: 2) | INT | Ja | 1 - 128 |
| `max_depth` | Die maximale Tiefenebene (Auflösungsskala), auf die Tiling angewendet wird. Ein Wert von 0 wendet Tiling nur bei der höchsten Auflösung an (Standard: 0) | INT | Ja | 0 - 10 |
| `scale_depth` | Wenn aktiviert, wird die Kachelgröße auf tieferen Tiefenebenen proportional skaliert. Dies kann helfen, die Qualität bei niedrigeren Auflösungen zu erhalten (Standard: False) | BOOLEAN | Ja | True / False |

Hinweis: `tile_size`, `swap_size`, `max_depth` und `scale_depth` sind als erweiterte Eingaben gekennzeichnet, daher werden sie nur angezeigt, wenn erweiterte Optionen in der Oberfläche aktiviert sind.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeter HyperTile-Optimierung | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/de.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
