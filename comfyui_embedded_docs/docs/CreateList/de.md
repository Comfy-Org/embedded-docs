# CreateList

Der Node Create List kombiniert mehrere Eingaben zu einer einzigen, sequenziellen Liste. Er akzeptiert eine beliebige Anzahl von Eingabe-Slots, die denselben Datentyp verwenden, und verkettet ihre Elemente in der Reihenfolge, in der die Slots verbunden sind. Das Ergebnis ist eine Liste, die alle verbundenen Elemente enthält.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `inputs` | Eine variable Anzahl von Eingabe-Slots mit den Namen `input`, `input_2`, `input_3` usw. Jeder Slot akzeptiert eine Liste von Elementen desselben Datentyps (zum Beispiel alle IMAGE oder alle STRING). Neue Slots werden bei Bedarf automatisch erstellt. Der Node verkettet die Listen in der Reihenfolge der Slots. | Beliebig | Ja | Beliebige Anzahl von Slots; jeder Slot akzeptiert eine beliebige Anzahl von Elementen |

**Hinweis:** Alle verbundenen Eingaben müssen denselben Datentyp haben. Jeder verbundene Slot stellt eine Liste von Elementen bereit, und der Node kombiniert die Listen in der Reihenfolge der Slots (`input`, dann `input_2`, dann `input_3`, ...). Der Node ist auch unter den Aliasen "Image Iterator", "Text Iterator" und "Iterator" auffindbar.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `list` | Eine einzige Liste mit allen Elementen aus den verbundenen Eingaben, verkettet in der Reihenfolge, in der die Slots bereitgestellt wurden. Der Datentyp der Ausgabe entspricht dem Datentyp der Eingabe. | Beliebig |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/de.md)

---
**Source fingerprint (SHA-256):** `4824fa6af46ab08cd3c10b033dbb3e43682b468e1dbd934fffb571349e025b96`
