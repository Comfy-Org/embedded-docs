# AddNoise

Dieser Node fügt einem latenten Bild kontrolliertes Rauschen hinzu, indem ein angegebener Rauschgenerator und Sigma-Werte verwendet werden. Er verarbeitet die Eingabe durch das Sampling-System des Modells, um die Rauschskalierung entsprechend dem angegebenen Sigma-Bereich anzuwenden, und gibt eine neue latente Darstellung mit angewendetem Rauschen zurück. Dieser Node ist derzeit als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das Sampling-Parameter und Verarbeitungsfunktionen enthält | MODEL | Ja | - |
| `noise` | Der Rauschgenerator, der das Basis-Rauschmuster erzeugt | NOISE | Ja | - |
| `sigmas` | Sigma-Werte, die die Intensität der Rauschskalierung steuern. Wenn leer, gibt der Node das ursprüngliche latente Bild unverändert zurück. Wenn mehrere Sigmas angegeben werden, wird die Rauschskala als absolute Differenz zwischen dem ersten und letzten Sigma-Wert berechnet. Wenn nur ein Sigma angegeben wird, wird dieser Wert direkt als Skala verwendet. | SIGMAS | Ja | - |
| `latent_image` | Die latente Eingabedarstellung, der Rauschen hinzugefügt wird. Leere latente Bilder (die nur Nullen enthalten) werden während der Verarbeitung nicht verschoben. | LATENT | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Die modifizierte latente Darstellung mit hinzugefügtem Rauschen. Alle NaN- oder Unendlich-Werte in der Ausgabe werden zur Stabilität in Nullen umgewandelt. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/de.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
