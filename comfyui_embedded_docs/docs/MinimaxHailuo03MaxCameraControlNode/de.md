# MiniMax H3 Max Camera Control

Dieser Node erzeugt ein Video, das von einem Standbild ausgeht und die Kamera auf einen neuen Winkel und Abstand um das Motiv bewegt. Azimut, Elevation und Abstand beschreiben, wo die Kamera endet; das erste Bild bleibt exakt wie geliefert. Wenn kein Prompt angegeben wird, bleibt die Szene eingefroren und nur die Kamera bewegt sich.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell, das für die Videogenerierung verwendet wird. | DYNAMIC_COMBO | Ja | "MiniMax H3 Max" |

### MiniMax H3 Max Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Erstes Bild des Videos, mindestens 256x256 Pixel. Das Seitenverhältnis muss zwischen 0,4 und 2,5 liegen. | IMAGE | Ja | Einzelbild |
| `camera_info` | Optionale Endkamera, zum Beispiel aus Create Camera Info oder Compose Camera Angle Prompt, wobei das Bild als Vorderansicht dient. Wenn sie verbunden ist, legt sie Azimut und Elevation fest. | LOAD3D_CAMERA | Nein | Kamerainformationen |
| `prompt` | Optional. Wenn leer, bleibt die Szene eingefroren und nur die Kamera bewegt sich. | STRING | Ja | 0 bis 50000 Zeichen |
| `azimuth` | Horizontaler Orbit um das Motiv am Ende des Videos, in Grad ausgehend vom Bild (Standard: 90). Positive Werte bewegen die Kamera nach rechts, sodass sich das Motiv zur linken Bildseite dreht. Es ist ein Zielwert: Ein Orbit von 90 Grad landet oft zwischen 30 und 90 Grad. Wird ignoriert, wenn `camera_info` verbunden ist. | INT | Ja | -360 bis 360 |
| `elevation` | Vertikaler Kamerawinkel am Ende des Videos, in Grad (Standard: 0). Positive Werte blicken von oben nach unten, negative Werte von unten nach oben. Wird ignoriert, wenn `camera_info` verbunden ist. | INT | Ja | -90 bis 90 |
| `distance` | Kameraabstand am Ende des Videos relativ zum Bild: 1 behält ihn bei, unter 1 bewegt näher heran, über 1 zieht zurück (Standard: 1.0). | FLOAT | Ja | 0.1 bis 10.0 |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 1 bis 15 |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "480P"<br>"768P"<br>"1080P" |
| `prompt_expansion_mode` | Wie viel Aufwand in die Umschreibung des Prompts vor der Generierung fließt (Standard: "balanced"). | COMBO | Ja | "disabled"<br>"balanced"<br>"quality" |
| `seed` | Zufälliger Seed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 4294967295 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das generierte Video mit angewendeter Kamerabewegung. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxCameraControlNode/de.md)

---
**Source fingerprint (SHA-256):** `d9eed1a3ae91891b974bea39ea00101c0577cf5b204d4c701b13b232e0604153`
