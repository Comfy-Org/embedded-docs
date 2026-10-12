# VAE dekodieren (gekachelt)

Der Node VAEDecodeTiled dekodiert latente Repräsentationen mithilfe eines gekachelten Ansatzes in Bilder, um große Bilder effizient zu verarbeiten. Er verarbeitet die Eingabe in kleineren Kacheln, um den Speicherverbrauch zu steuern und gleichzeitig die Bildqualität zu erhalten. Der Node unterstützt außerdem Video-VAEs, indem er temporale Frames in Blöcken mit Überlappung für sanfte Übergänge verarbeitet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die latente Repräsentation, die in Bilder dekodiert werden soll | LATENT | Ja | - |
| `vae` | Das VAE-Modell, das zum Dekodieren der latenten Samples verwendet wird | VAE | Ja | - |
| `tile_size` | Die Größe jeder Kachel für die Verarbeitung (Standard: 512) | INT | Ja | 64-4096 (step: 32) |
| `overlap` | Der Überlappungsbetrag zwischen benachbarten Kacheln (Standard: 64) | INT | Ja | 0-4096 (step: 32) |
| `temporal_size` | Nur für Video-VAEs verwendet: Anzahl der gleichzeitig zu dekodierenden Frames (Standard: 64) | INT | Ja | 8-4096 (step: 4) |
| `temporal_overlap` | Nur für Video-VAEs verwendet: Anzahl der zu überlappenden Frames (Standard: 8) | INT | Ja | 4-4096 (step: 4) |

**Hinweis:** Die Eingaben `tile_size`, `overlap`, `temporal_size` und `temporal_overlap` sind als erweiterte Einstellungen markiert.

**Hinweis:** Der Node passt Überlappungswerte automatisch an, wenn sie praktische Grenzen überschreiten. Wenn `tile_size` kleiner als das Vierfache von `overlap` ist, wird die Überlappung auf ein Viertel der Kachelgröße reduziert. Ebenso wird, wenn `temporal_size` kleiner als das Doppelte von `temporal_overlap` ist, die temporale Überlappung halbiert. Der Node berücksichtigt außerdem die internen Kompressionsraten des VAE, wenn er Kachel- und Überlappungsgrößen für räumliche und temporale Dimensionen berechnet. Wenn die eingegebenen Latents einen verschachtelten Batch von Latents bilden, wird nur das erste Element im Batch dekodiert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Das dekodierte Bild oder die dekodierten Bilder, die aus der latenten Repräsentation erzeugt wurden. Beim Dekodieren von Video-Latents ist die Ausgabe eine Sequenz von Einzelbildern. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/de.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
