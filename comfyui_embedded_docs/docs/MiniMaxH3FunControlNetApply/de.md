# MiniMax H3 Fun ControlNet anwenden

Dieser Node wendet einen MiniMax H3 Fun ControlNet als Modell-Patch auf ein Text-zu-Video-Modell an. Er kann ein optionales Steuervideo und eine optionale Maske verwenden, um die Generierung zu steuern, und gibt eine gepatchte Kopie des Modells für weiteres Sampling zurück. Wenn die Stärke auf 0 gesetzt ist oder weder ein Steuervideo noch eine Maske bereitgestellt wird, wird das Eingabemodell unverändert zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Diffusionsmodell, auf das der MiniMax H3 Fun ControlNet-Patch angewendet wird. | MODEL | Ja | N/A |
| `model_patch` | Der MiniMax H3 Fun ControlNet-Patch, dessen Steuersignale in das Modell injiziert werden; er muss mit dem angegebenen `model` kompatibel sein. | MODEL_PATCH | Ja | N/A |
| `vae` | VAE, der verwendet wird, um die Steuer- und Quellvideo-Frames in den vom Modell erwarteten latenten Raum zu kodieren. | VAE | Ja | N/A |
| `strength` | Gesamtstärke des ControlNet-Effekts. Bei Einstellung auf 0 führt der Node nichts aus und gibt das Eingabemodell unverändert zurück. (Standard: 1.0) | FLOAT | Ja | min 0.0, max 10.0, step 0.01 |
| `start_percent` | Beginn des Sampling-Bereichs, ausgedrückt als Prozentsatz des Sampling-Zeitplans, in dem das ControlNet aktiv ist. Der Wert wird intern in den entsprechenden Sigma-Wert umgerechnet. Dies ist eine erweiterte Einstellung. (Standard: 0.0) | FLOAT | Ja | min 0.0, max 1.0, step 0.001 |
| `end_percent` | Ende des Sampling-Bereichs, ausgedrückt als Prozentsatz des Sampling-Zeitplans, in dem das ControlNet aktiv ist. Der Wert wird intern in den entsprechenden Sigma-Wert umgerechnet. Dies ist eine erweiterte Einstellung. (Standard: 1.0) | FLOAT | Ja | min 0.0, max 1.0, step 0.001 |
| `control_video` | Optionale Videoframes, die als visueller Hinweis für das ControlNet verwendet werden. Die Frames werden auf die Größe des generierten Videos angepasst und mit dem `vae` kodiert. | IMAGE | Nein | N/A |
| `mask` | 1 markiert die Bereiche, die neu generiert werden sollen. Maskenwerte über 0.5 werden als markierte Bereiche behandelt. | MASK | Nein | N/A |
| `source_video` | Video hinter der Maske; wird nur gelesen, wenn eine Maske angegeben ist. | IMAGE | Nein | N/A |

Hinweis: Damit der Patch eine Wirkung hat, muss `strength` größer als 0 sein und mindestens eines von `control_video` oder `mask` angegeben werden. `source_video` wird ignoriert, sofern keine `mask` bereitgestellt wird; wenn `mask` ohne `source_video` angegeben wird, wird der Inhalt hinter den maskierten Bereichen als Schwarz behandelt. Wenn sowohl `control_video` als auch `mask` angegeben werden, kombiniert der Steuerhinweis die Merkmale des Steuervideos mit dem maskierten Quellinhalt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model` | Eine gepatchte Kopie des Eingabemodells mit angewendetem MiniMax H3 Fun ControlNet. Wenn `strength` 0 ist oder kein Steuervideo bzw. keine Maske bereitgestellt wird, wird das ursprüngliche Modell unverändert zurückgegeben. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/de.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`
