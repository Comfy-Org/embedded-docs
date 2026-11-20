# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video verwandelt einen Text-Prompt in ein Video mit Ton und verwendet dabei Creatifys nachtrainiertes H3-Modell, das für Videoanzeigen entwickelt wurde. Verbinden Sie ein erstes Frame, um ein Standbild zu animieren, und optional ein letztes Frame, um die Aufnahme auf einem gewählten Bild enden zu lassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt, der das Video beschreibt. Muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist. | STRING | Ja | Beliebiger nicht leerer Text |
| `first_frame` | Bild, mit dem das Video beginnt. Wenn es verbunden ist, lassen Sie `aspect_ratio` auf `"auto"`, damit das Video dem Bild folgt. | IMAGE | Nein | - |
| `last_frame` | Bild, mit dem das Video endet. Erfordert ein verbundenes `first_frame`. | IMAGE | Nein | - |
| `resolution` | Auflösung des Ausgabevideos (Standard: `"768p"`). | COMBO | Ja | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"auto"` folgt dem ersten Frame, wenn eines verbunden ist; lassen Sie es in diesem Fall auf `"auto"` (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Länge des Videos in Sekunden (Standard: 5). Bei `"2k"` beträgt das Maximum 14 Sekunden. | INT | Ja | 1 bis 15 (Schritt 1) |
| `prompt_enhancement` | Wie Creatify den Prompt vor dem Rendern umschreibt: `"auto"` und `"ads"` verwandeln ihn in einen Videoanzeigen-Prompt und können gesprochene Zeilen hinzufügen, `"general"` schreibt ihn für beliebige andere Videos um, `"none"` rendert ihn wie geschrieben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt wird. An Boreal-H3 wird kein Seed gesendet, daher kann ein erneutes Ausführen mit denselben Eingaben ein anderes Video erzeugen (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:** Mit einem `first_frame` stammt das Seitenverhältnis immer vom Bild, daher führt jeder andere Wert für `aspect_ratio` zu einem Fehler. Ein `last_frame` ohne `first_frame` wird abgelehnt, und eine `duration` über 14 Sekunden wird bei `"2k"` abgelehnt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit Ton. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/de.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`
