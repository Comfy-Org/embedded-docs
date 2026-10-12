# Bild zuschneiden (zufällig)

Der Node Random Crop Images wählt zufällig einen rechteckigen Bereich aus jedem Eingabebild aus und schneidet ihn auf eine angegebene Breite und Höhe zu. Dies wird üblicherweise für die Datenaugmentierung verwendet, um Variationen von Trainingsbildern zu erzeugen. Die zufällige Position für den Zuschnitt wird durch einen Seed-Wert bestimmt, wodurch sichergestellt wird, dass derselbe Zuschnitt reproduziert werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Bild, das zugeschnitten werden soll. | IMAGE | Ja | - |
| `width` | Die Breite des Zuschnittbereichs (Standard: 512). | INT | Nein | 1 - 8192 |
| `height` | Die Höhe des Zuschnittbereichs (Standard: 512). | INT | Nein | 1 - 8192 |
| `seed` | Eine Zahl, die zur Steuerung der zufälligen Position des Zuschnitts verwendet wird (Standard: 0). | INT | Nein | 0 - 18446744073709551615 |

**Hinweis:** Die Parameter `width` und `height` müssen kleiner als oder gleich den Abmessungen des Eingabebilds sein. Wenn eine angegebene Dimension größer als das Bild ist, wird der Zuschnitt auf die Grenzen des Bildes beschränkt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das resultierende Bild nach Anwendung des zufälligen Zuschnitts. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/de.md)

---
**Source fingerprint (SHA-256):** `8452a07a1cf66a520fb482f5239df3f33cfe3a77a28e289894ccd1d2544ecf40`
