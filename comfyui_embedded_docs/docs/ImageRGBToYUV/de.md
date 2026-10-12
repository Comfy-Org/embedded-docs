# ImageRGBToYUV

Der Node ImageRGBToYUV konvertiert ein RGB-Bild mithilfe einer RGB-zu-YCbCr-Farbkonvertierung in YUV-ähnliche Farbkomponenten. Er teilt das Ergebnis in drei separate Bilder auf – Y (Luminanz bzw. Helligkeit), U (Blau-Differenz-Chrominanz) und V (Rot-Differenz-Chrominanz) – und gibt jede Komponente mit derselben Breite und Höhe wie die Eingabe zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das RGB-Eingabebild, das in Y-, U- und V-Komponenten umgewandelt werden soll. Wenn das Bild einen Alphakanal enthält, werden nur die ersten drei (RGB) Kanäle verwendet. | IMAGE | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `Y` | Die Luminanzkomponente (Helligkeit) des YUV-Farbraums, zurückgegeben als dreikanaliges Bild | IMAGE |
| `U` | Die Blau-Differenz-Chrominanzkomponente des YUV-Farbraums, zurückgegeben als dreikanaliges Bild | IMAGE |
| `V` | Die Rot-Differenz-Chrominanzkomponente des YUV-Farbraums, zurückgegeben als dreikanaliges Bild | IMAGE |

Jede Ausgabe hat dieselbe Breite und Höhe wie das Eingabebild. Die entsprechende Y-, U- oder V-Komponente wird über alle drei Kanäle wiederholt, sodass jede Ausgabe als standardmäßiges dreikanaliges Bild zurückgegeben wird.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/de.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
