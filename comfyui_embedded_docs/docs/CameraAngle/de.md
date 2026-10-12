# CameraAngle

Dieser Node wählt einen Kamerawinkel um ein Motiv herum und wandelt diese Auswahl in zwei Dinge um: eine `camera_info`-Struktur, die 3D-Nodes rendern können, und eine einfache englischsprachige Aufnahmebeschreibung, die Sie in einen Prompt einfügen können. Das Motiv befindet sich im Ursprung der Szene, wo nachgelagerte 3D-Nodes ihre Modelle zentrieren, sodass der hier gewählte Winkel mit der Vorschau übereinstimmt.

Verwenden Sie ihn, um vor der Generierung den Bildausschnitt eines Renderings festzulegen oder einen Blickwinkel wie `front view eye-level shot medium shot` für ein Bild- oder Videomodell zu beschreiben. Die 3D-Vorschau im Node zeigt die resultierende Kameraposition.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `horizontal_angle` | Azimut um das Motiv in Grad: 0 ist die Vorderseite, 90 die rechte Seite und 180 die Rückseite. (Standard: 0) | INT | Ja | 0 bis 360 |
| `vertical_angle` | Höhenwinkel in Grad. Negative Werte blicken von unten nach oben, positive Werte von oben nach unten. (Standard: 0) | INT | Ja | -30 bis 60 |
| `zoom` | Objektiv-Zoom auf das Motiv: 0 ist eine Weitwinkelaufnahme, 10 eine Nahaufnahme. Der Wert wird auch in `camera_info.zoom` übernommen. (Standard: 5.0) | FLOAT | Ja | 0.0 bis 10.0 (Schritt 0.1) |
| `image` | Optionales Referenzbild, das auf der Vorderseite des Motivwürfels in der 3D-Vorschau angezeigt wird. | IMAGE | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `camera_info` | Kamerainformationen für 3D-Nodes: Position, Look-at-Ziel, Zoomfaktor, Kameratyp und Sichtfeld. Die Kamera behält ein festes Sichtfeld von 35 Grad und wird 6 Einheiten vom Ziel entfernt platziert. | LOAD3DCAMERA |
| `prompt` | Kurze Aufnahmebeschreibung, die aus Winkel, Erhebung und Entfernung erstellt wird, zum Beispiel `front view eye-level shot medium shot`. | STRING |

## Begriffe der Aufnahmebeschreibung

Die Ausgabe `prompt` kombiniert einen Begriff aus jeder der folgenden Gruppen. Die Werte werden zuvor auf die Widget-Bereiche begrenzt.

- Der horizontale Winkel wird in acht 45-Grad-Sektoren unterteilt: `front view`, `front-right quarter view`, `right side view`, `back-right quarter view`, `back view`, `back-left quarter view`, `left side view`, `front-left quarter view`.
- Der vertikale Winkel wird zu `low-angle shot` unter -15 Grad, `eye-level shot` unter 15, `elevated shot` unter 45 und `high-angle shot` ab 45 Grad aufwärts.
- Der Zoom wird zu `wide shot` unter 2, `medium shot` unter 6 und `close-up` bei 6 oder mehr.

Der Faktor `camera_info.zoom` skaliert den Widget-Wert auf 1.0 bis 1.875, sodass Zoom 0 den Wert 1.0 und Zoom 10 den Wert 1.875 ergibt.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CameraAngle/de.md)

---
**Source fingerprint (SHA-256):** `8ed2cd186bc6ca02dbc8da006b2e9156245ef691a2257f286f6e32ffa480fd5d`
