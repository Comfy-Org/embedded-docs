# PatchModelAddDownscale (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink) wendet die Kohya-Deep-Shrink-Technik auf ein Modell an, indem Zwischenmerkmale an einem ausgewählten Block verkleinert und anschließend wieder auf ihre ursprüngliche Größe skaliert werden. Die Verkleinerung erfolgt nur während eines ausgewählten Teils des Denoising-Prozesses, wodurch der Verarbeitungsaufwand reduziert werden kann, während das Endergebnis nahe am Original bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `Modell` | Das Modell, auf das der Downscale-Patch angewendet werden soll | MODEL | Ja | - |
| `Blocknummer` | Die spezifische Blocknummer, an der die Verkleinerung angewendet wird (Standard: 3) | INT | Ja | 1-32 |
| `Downscale-Faktor` | Der Faktor, um den die Merkmale verkleinert werden (Standard: 2.0) | FLOAT | Ja | 0.1-9.0 |
| `Startprozent` | Der Startpunkt im Denoising-Prozess, an dem die Verkleinerung beginnt (Standard: 0.0) | FLOAT | Ja | 0.0-1.0 |
| `Endprozent` | Der Endpunkt im Denoising-Prozess, an dem die Verkleinerung stoppt (Standard: 0.35) | FLOAT | Ja | 0.0-1.0 |
| `Downscale nach Skip` | Ob die Verkleinerung nach Skip-Verbindungen angewendet werden soll (Standard: True) | BOOLEAN | Ja | - |
| `Downscale-Methode` | Die Interpolationsmethode für Verkleinerungsvorgänge (Standard: "bicubic") | COMBO | Ja | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `Upscale-Methode` | Die Interpolationsmethode für Vergrößerungsvorgänge (Standard: "bicubic") | COMBO | Ja | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

Der Downscale-Patch wird nur angewendet, wenn der aktuelle Denoising-Schritt in den durch `start_percent` und `end_percent` definierten Bereich fällt, und nur an dem durch `block_number` ausgewählten Block. Wenn `downscale_after_skip` aktiviert ist, wird der Patch nach der Skip-Verbindung angewendet; wenn deaktiviert, wird er vor der Skip-Verbindung angewendet. Die Merkmale werden anschließend wieder auf ihre ursprüngliche Größe hochskaliert, jedoch nur, wenn die aktuelle Merkmalsgröße nicht mehr der vor der Verkleinerung aufgezeichneten Größe entspricht.

Die Parameter `block_number`, `start_percent`, `end_percent` und `downscale_after_skip` sind in der Node-Oberfläche als erweiterte Optionen markiert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendetem Downscale-Patch | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/de.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
