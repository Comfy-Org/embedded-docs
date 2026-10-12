# LumaConceptsNode

Enthält ein oder mehrere Kamera-Konzepte zur Verwendung mit den Nodes Luma Text to Video und Luma Image to Video. Dieser Node ermöglicht es Ihnen, bis zu vier Kamera-Konzepte auszuwählen und sie optional mit vorhandenen Konzeptketten zu kombinieren.

**Hinweis:** Dieser Node ist im Quellcode als veraltet gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `concept1` | Erste Kamera-Konzept-Auswahl aus verfügbaren Luma-Konzepten | STRING | Ja | Mehrere Optionen verfügbar<br>Enthält die Option "None" |
| `concept2` | Zweite Kamera-Konzept-Auswahl aus verfügbaren Luma-Konzepten | STRING | Ja | Mehrere Optionen verfügbar<br>Enthält die Option "None" |
| `concept3` | Dritte Kamera-Konzept-Auswahl aus verfügbaren Luma-Konzepten | STRING | Ja | Mehrere Optionen verfügbar<br>Enthält die Option "None" |
| `concept4` | Vierte Kamera-Konzept-Auswahl aus verfügbaren Luma-Konzepten | STRING | Ja | Mehrere Optionen verfügbar<br>Enthält die Option "None" |
| `luma_concepts` | Optionale Kamera-Konzepte, die den hier ausgewählten hinzugefügt werden | LUMA_CONCEPTS | Nein | N/A |

**Hinweis:** Alle Konzeptparameter (`concept1` bis `concept4`) können auf "None" gesetzt werden, wenn Sie nicht alle vier Konzept-Slots verwenden möchten. Der Node führt alle bereitgestellten `luma_concepts` mit den ausgewählten Konzepten zusammen, um eine kombinierte Konzeptkette zu erstellen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `luma_concepts` | Kombinierte Kamera-Konzeptkette, die alle ausgewählten Konzepte enthält | LUMA_CONCEPTS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/de.md)

---
**Source fingerprint (SHA-256):** `fc9da6288e29d89519f13e2412381ad8d689fc48353a80546a380dbe8f979037`
