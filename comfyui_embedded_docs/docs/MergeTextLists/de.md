# MergeTextLists

Dieser Node führt mehrere Textlisten zu einer einzigen, kombinierten Liste zusammen. Er ist darauf ausgelegt, Texteingaben als Listen zu empfangen und sie miteinander zu verketten. Der Node protokolliert die Gesamtzahl der Texte in der zusammengeführten Liste.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `texts` | Die Textlisten, die zusammengeführt werden sollen. Mehrere Listen können an den Eingang angeschlossen werden und werden zu einer einzigen verkettet. | STRING | Ja | N/A |

**Hinweis:** Dieser Node ist als Gruppenprozess (`is_group_process = True`) konfiguriert, was bedeutet, dass er mehrere Listeneingaben automatisch verarbeitet, indem er sie verkettet, bevor die Hauptverarbeitungsfunktion ausgeführt wird.

**Hinweis:** Dieser Node ist veraltet und wurde durch den Node „Create List“ ersetzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `texts` | Die einzelne, zusammengeführte Liste, die alle Eingabetexte enthält. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/de.md)

---
**Source fingerprint (SHA-256):** `bb7f45725c2c41a18d8cd3040d093c11be2ceb03cf1849385aa55d12fd9eb555`
