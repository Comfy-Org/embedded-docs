# Schleifenergebnis

LoopResult ist ein nur für Entwickler vorgesehener Ausgabeknoten, der den Schlusspunkt eines Schleifenblocks markiert. Er sammelt die an ihn übergebenen Werte in ihrer Reihenfolge (benannt als `output0`, `output1` usw.) und gibt den externen Ausführungsblock frei, der durch eine Close-ID identifiziert wird. Da die Eingabe-Fingerabdruckbildung immer NaN zurückgibt, wird der Knoten als immer geändert behandelt und bei jedem Lauf erneut ausgeführt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `close_id` | Bezeichner des zu schließenden Schleifenblocks; nur der erste Wert der Liste wird verwendet | STRING | Ja | - |
| `output0`, `output1`, ... | Werte, die aus dem Schleifenblock gesammelt werden. Der Knoten akzeptiert beliebige zusätzliche Eingaben und sammelt sie in sequenzieller Reihenfolge beginnend bei `output0`, wobei er beim ersten fehlenden Index stoppt | Beliebiger Typ | Nein | - |

Hinweis: Dieser Knoten akzeptiert alle Eingaben (`accept_all_inputs`). Jede Eingabe zusätzlich zu `close_id` wird als gesammelter Schleifenwert behandelt und muss `output0`, `output1`, `output2` usw. heißen, ohne Lücken, damit sie im Ergebnis enthalten ist.

## Ausgaben

Dieser Knoten gibt keine Ausgaben zurück. Er gibt nur den externen Ausführungsblock frei, der mit `close_id` verknüpft ist.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopResult/de.md)

---
**Source fingerprint (SHA-256):** `637f8a39b0e99e8d4453cfc482463bd14d909b710264021ac2c27fdcd68b6063`
