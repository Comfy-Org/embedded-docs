# Magnific-Bild-Upscale (Präzise V2)

Der Magnific Image Upscale (Precise V2)-Node führt eine hochgenaue Bild-Hochskalierung mit feiner Kontrolle über Schärfe, Körnung und Detailverbesserung durch. Er verarbeitet Bilder über eine externe API und unterstützt eine maximale Ausgabeauflösung von 10060×10060 Pixeln. Der Node bietet verschiedene Verarbeitungsstile und kann die Eingabe automatisch herunterskalieren, wenn die angeforderte Ausgabe die maximal zulässige Größe überschreiten würde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das hochskaliert werden soll. Es ist genau ein Bild erforderlich. Die Mindestabmessungen betragen 160x160 Pixel. Das Seitenverhältnis muss zwischen 1:3 und 3:1 liegen. | IMAGE | Ja | - |
| `scale_factor` | Der gewünschte Hochskalierungsfaktor. | COMBO | Ja | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `flavor` | Verarbeitungsstil: sublime für allgemeine Verwendung, photo für Fotografien, photo_denoiser für verrauschte Fotos. | COMBO | Ja | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` |
| `sharpen` | Intensität der Bildschärfe. Höhere Werte erhöhen Kantendefinition und Klarheit. Standard: 7. | INT | Ja | 0 bis 100 |
| `smart_grain` | Intelligente Körnungs-/Texturverbesserung, um zu verhindern, dass das Bild zu glatt oder künstlich aussieht. Standard: 7. | INT | Ja | 0 bis 100 |
| `ultra_detail` | Steuert feine Details, Texturen und Mikrodetails, die beim Hochskalieren hinzugefügt werden. Standard: 30. | INT | Ja | 0 bis 100 |
| `auto_downscale` | Skaliert das Eingabebild automatisch herunter, wenn die Ausgabe die maximale Auflösung überschreiten würde. Standard: False. Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | - |

**Hinweis:** Wenn `auto_downscale` deaktiviert ist und die angeforderte Ausgabegröße (Eingabeabmessungen × `scale_factor`) 10060x10060 Pixel überschreitet, löst der Node einen Fehler aus. Wenn `auto_downscale` aktiviert ist, versucht der Node, einen optimalen Skalierungsfaktor zu finden, der den Qualitätsverlust minimal hält.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das resultierende hochskalierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/de.md)

---
**Source fingerprint (SHA-256):** `aeb2b3569fd7b1d2417890586b8ac84ff921c4405f63f190188af93044ccfd28`
