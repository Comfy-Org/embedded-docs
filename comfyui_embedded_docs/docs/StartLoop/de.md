# Loop starten

Der Start Loop-Node startet eine Schleifenstruktur innerhalb eines Workflows. Er führt den verbundenen Schleifenkörper einmal pro Iteration aus und kann Iterationen auf drei Arten zählen: eine feste Anzahl von Wiederholungen (simple), einen numerischen Indexbereich (For) oder einen Durchlauf pro Element in einer Liste (List). Jeder Durchlauf stellt den aktuellen Index, First/Last-Flags und einen optionalen mitgeführten Wert bereit, der von einer Iteration zur nächsten weitergegeben werden kann.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mode` | Der Iterationsmodus der Schleife (Standard: "simple"). Der ausgewählte Modus bestimmt, welche zusätzlichen Parameter angezeigt werden. | DYNAMIC_COMBO | Ja | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | Wiederverwendung unveränderter Iterationsergebnisse aus vorherigen Ausführungen. Deaktivieren, um jede Iteration erneut auszuführen. Standard: false. | BOOLEAN | Ja | true<br>false |
| `parent_iteration` | Verbinden Sie iteration_index von einem äußeren Start Loop, um diese Schleife zu verschachteln. Dieser Eingang ist nur als Force-Input verfügbar (eine Verbindung ist erforderlich). | INT | Nein | Beliebige Ganzzahl |
| `initial_iteration_value` | Wert, der in der ersten Iteration als current_iteration_value bereitgestellt wird. | ANY (type-matched) | Nein | Beliebiger Wert |

### Eingaben für den einfachen Modus

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `num_iterations` | Anzahl der Ausführungen des Schleifenkörpers. Standard: 4. | INT | Ja | Mindestens 0 |

### Eingaben für den For-Modus

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `start_iteration_index` | Index der ersten Iteration bei Verwendung des For-Schleifenmodus. Standard: 0. | INT | Ja | Beliebige Ganzzahl |
| `max_iteration` | Der exklusive Stoppwert für iteration_index im For-Modus. Standard: 4. | INT | Ja | Maximal 0xffffffffffffffff |
| `step` | Die Index-Schrittweite zwischen den einzelnen Iterationen bei Verwendung des For-Schleifenmodus. Standard: 1. | INT | Ja | Mindestens 1 |

### Eingaben für den Listen-Modus

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `list` | Liste von Elementen, über die die Schleife iteriert. Der Schleifenkörper wird einmal pro Element ausgeführt. | ANY (type-matched list item) | Ja | Beliebige Liste |

Hinweise:

- Nur die Parameter, die zum aktuell ausgewählten `mode` gehören, werden angezeigt und verwendet.
- Im Simple-Modus laufen die Iterationsindizes von 0 bis `num_iterations` minus 1. Im For-Modus laufen die Indizes von `start_iteration_index` bis (aber nicht einschließlich) `max_iteration`, wobei sie um `step` erhöht werden. Im List-Modus läuft eine Iteration pro Element in `list`.
- `step` darf nicht 0 sein; ein Wert von 0 löst einen Fehler aus. Werte unter 1 sind nicht erlaubt.
- Wenn die berechnete Anzahl von Iterationen null ist, wird der `is_last`-Ausgang als true gemeldet und der Schleifenkörper wird nicht ausgeführt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `iteration_index` | Index der aktuellen Schleifeniteration. | INT |
| `is_first` | True während der ersten Iteration der Schleife. | BOOLEAN |
| `is_last` | True während der letzten Iteration der Schleife. | BOOLEAN |
| `list_item` | Aktuelles Element aus der Liste bei Verwendung des List-Modus. None in Simple- und For-Modus. | ANY (type-matched) |
| `current_iteration_value` | Mitgeführter Wert der Schleife für die aktuelle Iteration: initial_iteration_value in der ersten Iteration, dann next_iteration_value von End Loop in jeder nachfolgenden Iteration. | ANY (type-matched) |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/de.md)

---
**Source fingerprint (SHA-256):** `be34fedd4db9d4f4cc795855c87f6489f294e029da316b5dc66e5af7dff004a9`
