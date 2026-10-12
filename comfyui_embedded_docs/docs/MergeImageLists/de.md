# Bildlisten zusammenführen (VERALTET)

Der Node „Merge Image Lists“ kombiniert mehrere separate Bildlisten zu einer einzigen, fortlaufenden Liste. Er nimmt alle Bilder aus jedem verbundenen Eingang und hängt sie in der Reihenfolge aneinander, in der sie empfangen werden. Dies ist nützlich, um Bilder aus verschiedenen Quellen für die weitere Verarbeitung zu organisieren oder zu stapeln.

**Hinweis:** Dieser Node ist veraltet und wurde durch den Node „Create List“ ersetzt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Eine Liste von Bildern, die zusammengeführt werden sollen. Dieser Eingang kann mehrere Verbindungen annehmen, und jede verbundene Liste wird in die endgültige Ausgabe eingefügt. | IMAGE | Ja | - |

**Hinweis:** Dieser Node ist dafür ausgelegt, mehrere Eingaben zu empfangen. Sie können mehrere Bildlisten mit dem einzelnen `images`-Eingabe-Socket verbinden. Der Node verkettet automatisch alle Bilder aus allen verbundenen Listen zu einer Ausgabeliste.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Die einzelne, zusammengeführte Liste, die alle Bilder aus jeder verbundenen Eingabeliste enthält. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/de.md)

---
**Source fingerprint (SHA-256):** `0c9e302b02694a6a23fc7776c872856b1a629df3efe914a3e591a89d5a28914a`
