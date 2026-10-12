# StringFormat

## Übersicht

Dieser Node formatiert Text mithilfe der Python-String-Formatierungsmethode. Er funktioniert wie eine Vorlage, bei der Sie ein Textmuster mit Platzhaltern definieren und anschließend Werte zum Ausfüllen dieser Platzhalter angeben. Er unterstützt alle Formatierungsoptionen und Funktionen von Python.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `f_string` | Die Format-String-Vorlage mit Platzhaltern (Standard: `{a}`). Unterstützt mehrzeilige Eingabe. | STRING | Ja | N/A |
| `values` | Dynamische Eingabe zum Bereitstellen von Werten zum Ausfüllen der Platzhalter im Format-String. Bei Bedarf können mehrere Werteingaben hinzugefügt werden. | STRING | Ja | N/A |

**Hinweis zur `values`-Eingabe:** Diese Eingabe ist dynamisch und kann erweitert werden, um mehrere benannte Werte aufzunehmen. Jede Werteingabe ist mit einem Buchstaben (a, b, c usw.) beschriftet und entspricht einem Platzhalter im Format-String (z. B. `{a}`, `{b}`, `{c}`). Sie können Werteingaben nach Bedarf hinzufügen oder entfernen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `STRING` | Die formatierte Textzeichenkette, bei der alle Platzhalter durch ihre entsprechenden Werte ersetzt wurden. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringFormat/de.md)

---
**Source fingerprint (SHA-256):** `72625287533829a8087687bb47f39bc265aced3d5f43066f615326d729725122`
