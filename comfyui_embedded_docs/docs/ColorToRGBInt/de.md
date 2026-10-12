# ColorToRGBInt

Der **ColorToRGBInt**-Node konvertiert eine im Hexadezimalformat angegebene Farbe (wie `#FF5733`) in einen einzelnen RGB-Ganzzahlwert. Er extrahiert die Rot-, Grün- und Blau-Komponenten aus dem Farbstring, kombiniert sie zu einer einzelnen Ganzzahl und gibt außerdem die ursprüngliche hexadezimale Darstellung und den Alpha-Wert (Deckkraft) zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `color` | Ein Farbwert im Hexadezimalformat `#RRGGBB` oder `#RRGGBBAA`. Muss 7 oder 9 Zeichen lang sein und mit `#` beginnen. | COLOR | Ja | `#RRGGBB`<br>`#RRGGBBAA` |

**Hinweis:** Der Eingabe-String `color` muss dem Format `#RRGGBB` oder `#RRGGBBAA` folgen. Wenn er nicht 7 oder 9 Zeichen lang ist, nicht mit `#` beginnt oder ungültige Hexadezimalzeichen enthält, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `rgb_int` | Der berechnete RGB-Ganzzahlwert, abgeleitet aus der Formel: `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | Der hexadezimale Farbstring im Format `#RRGGBB`. Wenn die Eingabe einen Alpha-Kanal enthielt, wird er aus dieser Ausgabe entfernt. | COLOR |
| `alpha` | Der Alpha-Wert (Deckkraft) zwischen 0.0 und 1.0. Entspricht 1.0, wenn die Eingabe `#RRGGBB` ist, oder dem Alpha-Kanalwert geteilt durch 255, wenn die Eingabe `#RRGGBBAA` ist. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/de.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
