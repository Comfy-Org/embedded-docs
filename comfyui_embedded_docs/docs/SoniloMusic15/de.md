# Sonilo Music 1.5

Der Node Sonilo Music 1.5 erzeugt aus einem Text-Prompt einen kompletten Song mit gesungenem Gesang. Beschreiben Sie Genre, Stimmung, Instrumente und Gesang und geben Sie optional eigene Songtexte an; der Node sendet die Anfrage an den Sonilo-Dienst und gibt den fertigen Track als Audio zurück. Verwenden Sie ihn, wenn Sie einen vollständigen Song statt eines Instrumental-Clips benötigen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Range |
| --- | --- | --- | --- | --- |
| `prompt` | Beschreibung des Songs: Genre, Stimmung, Instrumente und Gesang. Um die Worte selbst festzulegen, fügen Sie einen `Lyrics:`-Block mit `[Verse]`- und `[Chorus]`-Tags hinzu; ohne einen solchen Block schreibt das Modell seine eigenen Texte. Muss nach dem Entfernen von Leerzeichen 1 bis 2000 Zeichen lang sein. | STRING | Ja | 1 bis 2000 Zeichen |
| `duration` | `auto` passt die Songlänge an den Songtext an. `custom` verwendet den Wert von `seconds`, schneidet nicht passende Texte ab und wiederholt kurze Texte. | DYNAMIC_COMBO | Ja | `"auto"`<br>`"custom"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 18446744073709551615 |

### Benutzerdefinierte Dauer-Parameter (wenn `duration` auf `"custom"` steht)

| Parameter | Beschreibung | Datentyp | Erforderlich | Range |
| --- | --- | --- | --- | --- |
| `seconds` | Länge des erzeugten Songs in Sekunden (Standard: 60). | INT | Ja | 10 bis 360 |

**Hinweis:** Die Eingabe `prompt` ist erforderlich und darf nicht leer sein. Der Node prüft, dass sie nach dem Entfernen von Leerzeichen mindestens 1 Zeichen und höchstens 2000 Zeichen enthält.

**Hinweis:** Die Nutzung wird mit 0,0032175 USD pro Sekunde der angeforderten Dauer abgerechnet, und das Preis-Badge folgt `duration.seconds`, wenn `custom` ausgewählt ist.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Der erzeugte Song einschließlich Gesang als Audiodatei. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloMusic15/de.md)

---
**Source fingerprint (SHA-256):** `65ccf74ccdfa7a710d8c7bd9871e666d79ceadc7304644fe0101956832ca6024`
