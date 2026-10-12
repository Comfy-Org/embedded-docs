# FluxKontextImageScale

Dieser Node skaliert das Eingabebild mithilfe des Lanczos-Algorithmus auf eine optimale Größe, die beim Training des Flux Kontext-Modells verwendet wird, basierend auf dem Seitenverhältnis des Eingabebilds. Dieser Node ist besonders nützlich bei der Eingabe großer Bilder, da übergroße Eingaben zu einer verringerten Qualität der Modellausgabe oder zu Problemen wie mehreren im Ergebnis erscheinenden Subjekten führen können.

## Eingaben

| Parametername | Beschreibung | Datentyp | Eingabetyp | Standardwert | Wertebereich |
| --- | --- | --- | --- | --- | --- |
| `image` | Eingabebild, das in der Größe geändert werden soll | IMAGE | Erforderlich | - | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Größenangepasstes Bild | IMAGE |

## Liste voreingestellter Größen

Im Folgenden finden Sie eine Liste der Standardgrößen, die beim Modelltraining verwendet werden. Der Node wählt die Größe aus, die dem Seitenverhältnis des Eingabebilds am nächsten kommt:

| Breite | Höhe | Seitenverhältnis |
|-------|--------|--------------|
| 672   | 1568   | 0.429       |
| 688   | 1504   | 0.457       |
| 720   | 1456   | 0.494       |
| 752   | 1392   | 0.540       |
| 800   | 1328   | 0.603       |
| 832   | 1248   | 0.667       |
| 880   | 1184   | 0.743       |
| 944   | 1104   | 0.855       |
| 1024  | 1024   | 1.000       |
| 1104  | 944    | 1.170       |
| 1184  | 880    | 1.345       |
| 1248  | 832    | 1.500       |
| 1328  | 800    | 1.660       |
| 1392  | 752    | 1.851       |
| 1456  | 720    | 2.022       |
| 1504  | 688    | 2.186       |
| 1568  | 672    | 2.333       |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextImageScale/de.md)
