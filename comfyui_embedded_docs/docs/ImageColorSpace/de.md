# Bildfarbraum konvertieren

Der Node ImageColorSpace konvertiert Bilder zwischen den Farbräumen sRGB (Rec.709), linearem Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3, linearem ACEScg und HDR ACEScct. LogC3 verwendet die EI-800-Kurve mit Rec.709-Primärfarben und auf [0, 1] begrenzten Codes; ACEScg ist szenenlineares AP1 mit D60-Weißpunkt, und ACEScct ist dessen Log-Kodierung; beide werden per Bradford-Transformation an D65 angepasst. Bei der Konvertierung in eine SDR-Ausgabe oder von HDR PQ nach HDR wird überschüssige Luminanz über den Batch hinweg per Tonemapping abgebildet und werden Farben außerhalb des Gamuts komprimiert; lineare, ACEScg- und ACEScct-Ausgaben sowie Konvertierungen von linear nach HDR bewahren erweiterte Werte. HLG- und PQ-Ausgaben clippen negative Kanäle. Konvertierungen werden in float32 berechnet, und etwaige Alpha-Kanäle werden unverändert durchgereicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu konvertierende Eingabebild. | IMAGE | Ja | Jedes gültige Bild. |
| `source` | Farbraum der Eingabepixel. Standard: "sRGB". | COMBO | Ja | `"sRGB"`<br>`"HDR"`<br>`"HDR ACEScct"`<br>`"HDR LogC3"`<br>`"HDR PQ"`<br>`"linear"`<br>`"linear ACEScg"` |
| `destination` | Farbraum der Ausgabepixel. Stellen Sie den Save-Node auf denselben Farbraum ein. Konvertieren Sie LogC3 oder ACEScct zu linearem ACEScg, bevor Sie ACEScg-EXR speichern, zu linear, bevor Sie Rec.709-EXR speichern, oder zu sRGB/HDR/HDR PQ, bevor Sie Videos speichern. Standard: "sRGB". | COMBO | Ja | `"sRGB"`<br>`"HDR"`<br>`"HDR ACEScct"`<br>`"HDR LogC3"`<br>`"HDR PQ"`<br>`"linear"`<br>`"linear ACEScg"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das konvertierte Bild im angegebenen Zielfarbraum. | IMAGE |

## Hinweise

- Linear 1.0 und ACEScg 1.0 verwenden denselben 203-Nit-Referenzweißpunkt wie sRGB; HLG verwendet eine 1000-Nit-Referenzanzeige.
- Lineare, ACEScg- und ACEScct-Ausgaben bewahren erweiterte Werte; Konvertierungen von linear nach HDR bewahren Highlights ohne Tonemapping.
- SDR-Ausgabe und PQ-zu-HLG-Konvertierung tonemappen überschüssige Luminanz über den Batch hinweg (wobei ein gemeinsamer Weißpunkt verwendet wird, damit sich die Belichtung nicht von Frame zu Frame ändert) und komprimieren Farben außerhalb des Gamuts. HLG- und PQ-Ausgaben clippen negative Kanäle.
- Konvertierungen werden in float32 berechnet und geben das Intermediate-Gerät und den dtype zurück.
- LogC3 und ACEScct sind Kamera-Log-Kodierungen: Konvertieren Sie sie für ACEScg-EXR zu linearem ACEScg (AP1), für Rec.709-EXR zu linear (Rec.709) oder vor dem Speichern von Videos zu sRGB/HDR/HDR PQ.
- Straight-Alpha wird nicht farbtransformiert; nur die RGB-Kanäle werden konvertiert.
- Wenn `source` und `destination` identisch sind, wird keine Farbtransformation angewendet – das Bild wird lediglich auf das Intermediate-Gerät und den dtype verschoben.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/de.md)

---
**Source fingerprint (SHA-256):** `cbb3452e6844985580d5b91c6b1cbfbd770307cda6c92aba8b21c9bdd45ae370`
