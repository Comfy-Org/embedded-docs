# SeedVR2Preprocess

Dieser Node bereitet ein in der Größe angepasstes Bild oder Video für das SeedVR2-Modell vor, indem er es auf die Form auffüllt, die das Modell erwartet. Pixelwerte werden auf den Bereich 0–1 begrenzt, Höhe und Breite werden auf Vielfache von 16 aufgefüllt, und die Frame-Anzahl wird durch Wiederholen des letzten Frames aufgefüllt, bis sie einem 4n+1-Muster (1, 5, 9, 13, ...) folgt. Der Alpha-Kanal wird während der Verarbeitung entfernt; der zugehörige Node Post-Process SeedVR2 Output stellt ihn später aus dem ursprünglichen, in der Größe angepassten Bild wieder her.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | Das zu verarbeitende, in der Größe angepasste Bild. | IMAGE | Ja | - |

Hinweis: Die Eingabe kann ein einzelner Frame, eine Sequenz von Frames oder ein Batch von Videos sein (4-D- oder 5-D-IMAGE-Tensoren). Wenn sie mehr als 3 Kanäle hat, wird der Alpha-Kanal entfernt und nur RGB beibehalten. Die kürzere Kante der Eingabe muss mindestens 2 Pixel betragen. Räumliches Padding wird mit Schwarz (Wert 0) gefüllt, und gültige Frame-Anzahlen folgen einem 4n+1-Muster (1, 5, 9, 13, ...).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `images` | Das aufgefüllte Bild für die VAE-Kodierung. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/de.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
