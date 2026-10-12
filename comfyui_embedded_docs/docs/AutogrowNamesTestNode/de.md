# AutogrowNamesTestNode

Dieser Node ist ein Test für die Autogrow-Eingabefunktion. Er akzeptiert eine dynamische Gruppe von Float-Eingaben, jede mit einem vordefinierten Namen, und kombiniert ihre Werte zu einem einzelnen kommagetrennten String.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `autogrow` | Eine dynamische Eingabegruppe. Sie können mehrere Float-Eingaben hinzufügen, jede mit einem vordefinierten Namen aus der Liste: "a", "b" oder "c". Der Node akzeptiert jede Kombination dieser benannten Eingaben. | FLOAT | Ja | Benannte Slots: `a`, `b`, `c` |

**Hinweis:** Die `autogrow`-Eingabe ist dynamisch. Einzelne Float-Eingaben mit den Namen „a“, „b“ und „c“ können nach Bedarf hinzugefügt oder entfernt werden. Alle bereitgestellten Werte werden vom Node verarbeitet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Ein einzelner String, der die Werte aller bereitgestellten Float-Eingaben enthält, durch Kommas verbunden. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/de.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
