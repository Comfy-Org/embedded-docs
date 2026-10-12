# ConditioningSetAreaPercentage

Der Node ConditioningSetAreaPercentage ist darauf spezialisiert, den Einflussbereich von Conditioning-Elementen anhand prozentualer Werte anzupassen. Er ermöglicht die Angabe der Abmessungen und Position des Bereichs als Prozentsätze der Gesamtbildgröße sowie einen `strength`-Parameter, um die Intensität des Conditioning-Effekts zu modulieren.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Stellt die zu ändernden Conditioning-Elemente dar und dient als Grundlage für die Anwendung von Bereichs- und Strength-Anpassungen. | CONDITIONING |
| `width` | Legt die Breite des Bereichs als Prozentsatz der gesamten Bildbreite fest und beeinflusst, wie stark das Conditioning horizontal auf das Bild wirkt. | `FLOAT` |
| `height` | Bestimmt die Höhe des Bereichs als Prozentsatz der gesamten Bildhöhe und beeinflusst die vertikale Ausdehnung des Conditioning-Einflusses. | `FLOAT` |
| `x` | Gibt den horizontalen Startpunkt des Bereichs als Prozentsatz der gesamten Bildbreite an und positioniert den Conditioning-Effekt. | `FLOAT` |
| `y` | Gibt den vertikalen Startpunkt des Bereichs als Prozentsatz der gesamten Bildhöhe an und positioniert den Conditioning-Effekt. | `FLOAT` |
| `strength` | Steuert die Intensität des Conditioning-Effekts innerhalb des angegebenen Bereichs und ermöglicht eine Feinabstimmung seiner Wirkung. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Gibt die geänderten Conditioning-Elemente mit aktualisierten Bereichs- und Strength-Parametern zurück, bereit für die weitere Verarbeitung oder Anwendung. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/de.md)
