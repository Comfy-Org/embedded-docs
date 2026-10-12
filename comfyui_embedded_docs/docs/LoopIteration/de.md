# Schleifeniteration

Dieser Node stellt Iterations-Metadaten für Workflows im Schleifenstil bereit. Er empfängt listenbasierte Eingaben und reicht das erste Element jeder Liste durch, sodass eine Schleife den aktuellen Index, ob es sich um den ersten oder letzten Schritt handelt, das aktuelle Listenelement und einen beliebigen laufenden Iterationswert verfolgen kann. Das Cache-Verhalten wird durch das `reuse_cache`-Flag gesteuert. Dieser Node ist als nur für Entwickler gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `iteration_index` | Der Index der aktuellen Iteration, als Liste übergeben. Das erste Element wird an die Ausgabe weitergegeben. | INT | Ja | - |
| `is_first` | Gibt an, ob die aktuelle Iteration die erste ist, als Liste übergeben. Das erste Element wird an die Ausgabe weitergegeben. | BOOLEAN | Ja | - |
| `is_last` | Gibt an, ob die aktuelle Iteration die letzte ist, als Liste übergeben. Das erste Element wird an die Ausgabe weitergegeben. | BOOLEAN | Ja | - |
| `list_item` | Das für diese Iteration aus der Liste entnommene Element. Optional; wenn angegeben, wird das erste Element an die Ausgabe weitergegeben, andernfalls wird None zurückgegeben. | ANY | Nein | - |
| `current_iteration_value` | Der von der aktuellen Iteration mitgeführte Wert. Optional; wenn angegeben, wird der vollständige Wert an die Ausgabe weitergegeben, andernfalls wird None zurückgegeben. | ANY | Nein | - |
| `reuse_cache` | Steuert, ob das Ergebnis aus dem Cache wiederverwendet werden darf. Wenn aktiviert, behält der Node einen stabilen Fingerabdruck bei, sodass zwischengespeicherte Ergebnisse wiederverwendet werden können. Wenn deaktiviert, wird ein nicht übereinstimmender Fingerabdruck erzeugt, sodass der Node bei jeder Iteration erneut ausgeführt wird. | BOOLEAN | Ja | - |

Hinweis: Dieser Node ist für Listen-Eingaben ausgelegt, das heißt, jede Eingabe wird als Liste erwartet und der Node gibt nur das erste Element jeder Liste aus (außer `current_iteration_value`, das als Liste weitergegeben wird). Er akzeptiert außerdem zusätzliche Eingaben über die hier aufgeführten hinaus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `iteration_index` | Der Index der aktuellen Iteration. | INT |
| `is_first` | Ob die aktuelle Iteration die erste ist. | BOOLEAN |
| `is_last` | Ob die aktuelle Iteration die letzte ist. | BOOLEAN |
| `list_item` | Das für diese Iteration aus der Liste entnommene Element oder None, wenn kein Element angegeben wurde. | ANY |
| `current_iteration_value` | Der von der aktuellen Iteration mitgeführte Wert oder None, wenn kein Wert angegeben wurde. Diese Ausgabe wird als Liste zurückgegeben. | ANY |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/de.md)

---
**Source fingerprint (SHA-256):** `c7072f22bd382f567792d2ea7a30312c64d33c213551f8983c25cd7b95adc4fb`
