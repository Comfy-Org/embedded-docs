# Branch

Branch wählt einen von mehreren verbundenen Eingängen anhand seines Namens aus und leitet ihn an die Ausgabe weiter. Er funktioniert als Lazy Switch: Nur der ausgewählte Zweig wird ausgewertet, sodass die anderen Zweige unverbunden bleiben können oder Ausgaben enthalten können, die Sie nicht berechnen möchten. Jede neue Verbindung fügt eine weitere Zweig-Eingabe hinzu, Eingaben können per Doppelklick umbenannt werden, und der aktive Zweig wird über den Selektor `branch` ausgewählt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `autogrow` | Die verbundenen Zweige. Jede Verbindung fügt eine neue Zweig-Eingabe hinzu, bis zu 32; alle Zweige müssen denselben Datentyp verwenden, der zum Ausgabetyp wird. | AUTOGROW | Ja | 1 bis 32 Zweige |
| `branch` | Name des Zweigs, der an die Ausgabe weitergeleitet wird. Die Optionen sind die Namen der verbundenen Zweig-Eingaben, und eine Eingabe kann per Doppelklick umbenannt werden. | STRING | Ja | Namen der verbundenen Zweige |
| `branch_names` | Interne Liste der Namen der verbundenen Zweige, die vom Frontend synchron gehalten wird. Sie ordnet dem ausgewählten Namen seinen Zweig zu und ist nicht zur manuellen Bearbeitung gedacht. | ARRAY | Ja | - |

**Hinweis:** Nur der ausgewählte Zweig wird angefordert, daher werden die anderen Zweige nicht ausgewertet. Der Node löst einen Fehler aus, wenn der ausgewählte Name nicht verbunden ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Der Wert des ausgewählten Zweigs, unverändert weitergegeben. | MATCH_TYPE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BranchNode/de.md)

---
**Source fingerprint (SHA-256):** `2b4dca360c1b459a9f05eb54fedb7cdea6842fb0c606ee6f937ed00f715ee23a`
