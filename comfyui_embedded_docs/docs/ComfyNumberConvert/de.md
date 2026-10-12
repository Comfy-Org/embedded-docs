# ComfyNumberConvert

Der Node Number Convert wandelt verschiedene Eingabedatentypen in numerische Werte um. Er akzeptiert eine einzelne Eingabe vom Typ Ganzzahl, Fließkommazahl, Zeichenkette oder Boolean und erzeugt zwei Ausgaben: eine Fließkommazahl und eine Ganzzahl. Dies ist nützlich, um Text- oder logische Werte in ein Format umzuwandeln, das von anderen mathematischen oder verarbeitenden Nodes in Ihrem Workflow verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `value` | Der Wert, der in numerische Ausgaben umgewandelt werden soll. Akzeptiert eine Ganzzahl, eine Fließkommazahl, eine Zeichenkette oder einen Wahr/Falsch-Boolean. | INT, FLOAT, STRING, BOOLEAN | Ja | N/A |

**Hinweis:** Wenn die Eingabe eine Zeichenkette ist, darf sie nicht leer sein und muss eine gültige Darstellung einer Zahl enthalten (z. B. `"123"`, `"3.14"`). Der Node löst einen Fehler aus bei leeren Zeichenketten, Text, der nicht als Zahl interpretiert werden kann, oder Werten, die nicht endlich sind (wie `"inf"` oder `"nan"`). Bei Boolean-Eingaben wird `true` in 1.0 (FLOAT) und 1 (INT) umgewandelt, während `false` in 0.0 (FLOAT) und 0 (INT) umgewandelt wird. Bei FLOAT-Eingaben und bei Zeichenketten, die eine Dezimalzahl enthalten, wird die Ganzzahlausgabe durch Abschneiden des Dezimalanteils ermittelt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `FLOAT` | Der Eingabewert, umgewandelt in eine Fließkommazahl. | FLOAT |
| `INT` | Der Eingabewert, umgewandelt in eine Ganzzahl. Bei FLOAT-Eingaben und Dezimalzeichenketten wird eine Trunkierung durchgeführt. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/de.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
