# Benutzerdefinierte Auswahl

Der Custom Combo-Node ermöglicht es Ihnen, Ihre eigene Liste von Textoptionen für ein Dropdown-Menü zu definieren, anstatt aus festen Werten auszuwählen. Es ist ein frontend-orientierter Node, der auch eine Backend-Darstellung besitzt, sodass Workflows, die ihn enthalten, kompatibel bleiben. Wenn Sie eine Option auswählen, gibt der Node den ausgewählten Text und seine Indexposition aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `choice` | Die aus dem benutzerdefinierten Dropdown ausgewählte Textoption. Die Liste der verfügbaren Optionen wird vom Benutzer in der Frontend-Oberfläche des Nodes definiert. | COMBO | Ja | Benutzerdefiniert |
| `index` | Ein ganzzahliger Wert, der verwendet werden kann, um einen Index anzugeben. Standard: 0. | INT | Nein | Jede ganze Zahl (Standard: 0) |

**Hinweis:** Die Validierung für die Eingaben dieses Nodes ist absichtlich deaktiviert. Dadurch können Sie beliebige benutzerdefinierte Textoptionen im Frontend schreiben, ohne dass das Backend prüft, ob Ihre Auswahl einer vordefinierten Liste entspricht. Widgets außer dem Combo-Dropdown sind vollständig im Frontend definiert. Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `STRING` | Der Textstring der Option, die aus dem benutzerdefinierten Combo-Feld ausgewählt wurde. | STRING |
| `INDEX` | Die Indexposition der ausgewählten Option in der Dropdown-Liste. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/de.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
