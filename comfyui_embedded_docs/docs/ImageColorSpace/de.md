# Bildfarbraum konvertieren

Der Node ImageColorSpace konvertiert Bilder zwischen den Farbräumen sRGB (Rec.709), linearem Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3 und HDR ACEScct. LogC3 verwendet die EI-800-Kurve mit Rec.709-Primärfarben und auf [0, 1] begrenzten Codes; ACEScct verwendet AP1-Primärfarben und D60-Weißpunkt, mit Bradford-Anpassung an D65. Bei der Konvertierung in eine SDR-Ausgabe oder von HDR PQ nach HDR wird überschüssige Luminanz über den Batch hinweg per Tonemapping abgebildet und werden Farben außerhalb des Gamuts komprimiert; lineare und ACEScct-Ausgaben sowie Konvertierungen von linear nach HDR bewahren erweiterte Werte. HLG- und PQ-Ausgaben clippen negative Kanäle. Konvertierungen werden in float32 berechnet, und etwaige Alpha-Kanäle werden unverändert durchgereicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu konvertierende Eingabebild. | IMAGE | Ja | Jedes gültige Bild. |
| `source` | Farbraum der Eingabepixel. Standard: "sRGB". | COMBO | Ja | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |
| `destination` | Farbraum der Ausgabepixel. Stellen Sie den Save-Node auf denselben Farbraum ein. Konvertieren Sie LogC3 oder ACEScct zu linear, bevor Sie EXR speichern, oder zu sRGB/HDR/HDR PQ, bevor Sie Videos speichern. Standard: "sRGB". | COMBO | Ja | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das konvertierte Bild im angegebenen Zielfarbraum. | IMAGE |

## Hinweise

- Linear 1.0 verwendet denselben 203-Nit-Referenzweißpunkt wie sRGB; HLG verwendet eine 1000-Nit-Referenzanzeige.
- Lineare und ACEScct-Ausgaben bewahren erweiterte Werte; Konvertierungen von linear nach HDR bewahren Highlights ohne Tonemapping.
- SDR-Ausgabe und PQ-zu-HLG-Konvertierung tonemappen überschüssige Luminanz über den Batch hinweg (wobei ein gemeinsamer Weißpunkt verwendet wird, damit sich die Belichtung nicht von Frame zu Frame ändert) und komprimieren Farben außerhalb des Gamuts. HLG- und PQ-Ausgaben clippen negative Kanäle.
- Konvertierungen werden in float32 berechnet und geben das Intermediate-Gerät und den dtype zurück.
- LogC3 und ACEScct sind Kamera-Log-Kodierungen: Konvertieren Sie sie für das EXR-Speichern zu linear oder vor dem Speichern von Videos zu sRGB/HDR/HDR PQ.
- Straight-Alpha wird nicht farbtransformiert; nur die RGB-Kanäle werden konvertiert.
- Wenn `source` und `destination` identisch sind, wird keine Farbtransformation angewendet – das Bild wird lediglich auf das Intermediate-Gerät und den dtype verschoben.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/de.md)

---
**Source fingerprint (SHA-256):** `fdf8b4f16a1e0c7ff9a86b8cc40f6f796175205e4b1f491b595a74a8456b9b94`
