# ClipTextEncodeSdxlRefiner

Dieser Node ist speziell für das SDXL-Refiner-Modell konzipiert, um Text-Prompts durch die Einbeziehung ästhetischer Bewertungen und Dimensionsinformationen in Conditioning-Informationen umzuwandeln und so die Bedingungen für Generierungsaufgaben zu verbessern, wodurch der endgültige Verfeinerungseffekt optimiert wird. Er fungiert wie ein professioneller Art Director, der nicht nur Ihre kreative Absicht vermittelt, sondern auch präzise ästhetische Standards und Spezifikationsanforderungen in die Arbeit einbringt.

## Über SDXL Refiner

SDXL Refiner ist ein spezialisiertes Verfeinerungsmodell, das sich auf die Verbesserung von Bilddetails und -qualität auf Basis des SDXL-Basismodells konzentriert. Dieser Prozess ist wie ein Bildretuscheur:

1. Zuerst empfängt er vorläufige Bilder oder Textbeschreibungen, die vom Basismodell generiert wurden
2. Anschließend steuert er den Verfeinerungsprozess durch präzise ästhetische Bewertungen und Dimensionsparameter
3. Schließlich konzentriert er sich auf die Verarbeitung hochfrequenter Bilddetails, um die Gesamtqualität zu verbessern

Refiner kann auf zwei Arten verwendet werden:

- Als eigenständiger Verfeinerungsschritt zur Nachbearbeitung von Bildern, die vom Basismodell generiert wurden
- Als Teil eines Experten-Integrationssystems, das die Verarbeitung während der Low-Noise-Phase der Generierung übernimmt

## Eingaben

| Parametername | Beschreibung | Datentyp | Eingabetyp | Standardwert | Wertebereich |
| --- | --- | --- | --- | --- | --- |
| `clip` | CLIP-Modellinstanz, die für die Tokenisierung und Kodierung von Text verwendet wird; die Kernkomponente zur Umwandlung von Text in ein für das Modell verständliches Format | CLIP | Erforderlich | - | - |
| `ascore` | Steuert die visuelle Qualität und Ästhetik generierter Bilder, ähnlich wie das Festlegen von Qualitätsstandards für Kunstwerke:<br/>- Hohe Scores (7.5-8.5): Strebt nach feineren, detailreicheren Effekten<br/>- Mittlere Scores (6.0-7.0): Ausgewogene Qualitätskontrolle<br/>- Niedrige Scores (2.0-3.0): Geeignet für Negativ-Prompts | FLOAT | Optional | 6.0 | 0.0-1000.0 |
| `width` | Gibt die Breite des Ausgabebilds in Pixeln an; muss ein Vielfaches von 8 sein. SDXL erzielt die besten Ergebnisse, wenn die Gesamtpixelzahl nahe bei 1024×1024 liegt (etwa 1 Mio. Pixel) | INT | Erforderlich | 1024 | 64-16384 |
| `height` | Gibt die Höhe des Ausgabebilds in Pixeln an; muss ein Vielfaches von 8 sein. SDXL erzielt die besten Ergebnisse, wenn die Gesamtpixelzahl nahe bei 1024×1024 liegt (etwa 1 Mio. Pixel) | INT | Erforderlich | 1024 | 64-16384 |
| `text` | Text-Prompt-Beschreibung; unterstützt mehrzeilige Eingabe und dynamische Prompt-Syntax. Im Refiner sollten Text-Prompts stärker darauf ausgerichtet sein, die gewünschte visuelle Qualität und Detailmerkmale zu beschreiben | STRING | Erforderlich | - | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Verfeinerte Conditioning-Ausgabe, die eine integrierte Kodierung von Textsemantik, ästhetischen Standards und Dimensionsinformationen enthält, speziell zur Anleitung des SDXL-Refiner-Modells bei der präzisen Bildverfeinerung | CONDITIONING |

## Hinweise

1. Dieser Node ist speziell für das SDXL-Refiner-Modell optimiert und unterscheidet sich von regulären CLIPTextEncode-Nodes
2. Ein Ästhetik-Score von 7.5 wird als Basiswert empfohlen; dies ist die Standardeinstellung, die im SDXL-Training verwendet wird
3. Alle Dimensionsparameter müssen Vielfache von 8 sein, und eine Gesamtpixelzahl nahe bei 1024×1024 (etwa 1 Mio. Pixel) wird empfohlen
4. Das Refiner-Modell konzentriert sich auf die Verbesserung von Bilddetails und -qualität, daher sollten Text-Prompts die gewünschten visuellen Effekte statt den Szeneninhalt betonen
5. In der praktischen Anwendung wird Refiner typischerweise in den späteren Phasen der Generierung eingesetzt (etwa in den letzten 20 % der Schritte) und konzentriert sich auf die Detailoptimierung

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXLRefiner/de.md)
