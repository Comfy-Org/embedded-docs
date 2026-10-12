# PreviewAny

PreviewAny wandelt jeden Eingabewert in lesbaren Text um, damit Sie ihn überprüfen können. Zeichenketten werden unverändert übernommen, Zahlen und boolesche Werte werden in reinen Text umgewandelt, und andere Datentypen werden nach Möglichkeit zu JSON serialisiert (mit Rückfall auf ihre reine Zeichenkettenform, wenn die Serialisierung fehlschlägt). Der resultierende Text wird in der Benutzeroberfläche angezeigt und außerdem als Zeichenketten-Ausgabe für die weitere Verarbeitung zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `source` | Akzeptiert jeden Eingabedatentyp für die Vorschauanzeige. Wenn kein Wert bereitgestellt wird, zeigt die Vorschau 'None' an. | ANY | Ja | Beliebiger Datentyp |

**Konvertierungsverhalten**

- Werte vom Typ STRING werden genau so angezeigt, wie sie bereitgestellt wurden.
- Werte vom Typ INT, FLOAT oder BOOLEAN werden in reinen Text umgewandelt.
- Jeder andere nicht leere Wert wird in JSON-Text mit einer Einrückung von 4 Leerzeichen umgewandelt; wenn diese Konvertierung fehlschlägt, fällt der Node auf die reine Textform des Werts zurück. Wenn auch das fehlschlägt, zeigt die Vorschau die Meldung 'source exists, but could not be serialized.' an.
- Wenn kein Wert verbunden ist oder der Wert leer ist, zeigt die Vorschau 'None' an.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `result` | Der in das Textformat konvertierte Eingabewert. Derselbe Text wird auch in der Benutzeroberfläche angezeigt. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/de.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
