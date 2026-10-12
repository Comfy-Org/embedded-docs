# GetItemFromList

Dieser Node gibt ein einzelnes Element aus einer Liste zurück, ausgewählt anhand seiner Position. Sie geben die Liste und die Indexnummer des gewünschten Elements an, und der Node gibt dieses Element aus. Dadurch eignet er sich, um ein bestimmtes Element aus einer Gruppe von Werten auszuwählen, beispielsweise ein bestimmtes Bild aus einem Batch.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `list` | Die Liste der Werte, aus denen ausgewählt wird. Da dieser Node als Node mit Listeneingabe gekennzeichnet ist, wird der verbundene Wert als Gruppe von Elementen behandelt. | Beliebiger Typ | Ja | Beliebige Werteliste |
| `index` | Die Position des zurückzugebenden Elements. Der Wert beginnt bei 0, daher gibt `0` das erste Element zurück, `1` das zweite Element und so weiter (Standard: 0). | INT | Ja | Beliebiger ganzzahliger Index |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `OUTPUT` | Das einzelne Element, das sich am angegebenen `index` innerhalb der bereitgestellten `list` befindet. | Beliebiger Typ |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetItemFromList/de.md)

---
**Source fingerprint (SHA-256):** `11c1c90fed0e29f1110b4c1dda64d60797aff38d7f3af69f76b74e94fe94e976`
