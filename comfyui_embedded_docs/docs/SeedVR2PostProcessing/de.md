# SeedVR2PostProcessing

Dieser Node richtet das generierte Bild am ursprünglichen skalierten Bild aus und wendet eine optionale Farbkorrektur an. Er nimmt die Ausgabe eines SeedVR2-Upscaling-Prozesses und passt sie an Farben und Dimensionen des ursprünglichen Referenzbilds an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Das zu verarbeitende generierte Bild. | IMAGE | Ja | - |
| `original_resized_images` | Das ursprüngliche skalierte Bild vor der Vorverarbeitung, das als Referenz verwendet wird. | IMAGE | Ja | - |
| `color_correction_method` | Methode, um die Farben des generierten Bilds an das Originalbild anzupassen. lab: überträgt Farbe im CIELAB-Raum und bewahrt Details (am originalgetreuesten). wavelet: überträgt niedrigfrequente Farbe und behält hochfrequente Details des Upscalings bei. adain: gleicht Mittelwert/Standardabweichung pro Kanal ab (am schnellsten, globale Tönung). none: überspringt die Farbübertragung (nur geometrische Ausrichtung). (Standard: "lab") | COMBO | Ja | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Hinweis:** Beide Eingaben können Tensoren der Dimension 4-D (Batch, Höhe, Breite, Kanäle) oder 5-D (Batch, Frames, Höhe, Breite, Kanäle) sein. Der Node schneidet beide auf die kleinste Batch-Anzahl, Frame-Anzahl, Höhe und Breite zu, sodass sie nicht exakt übereinstimmen müssen. Wenn eine andere Farbkorrekturmethode als `none` verwendet wird, wird das Referenzbild zuerst auf die Ausgabegröße skaliert. Die Farbkorrektur wird in speicherbewussten Blöcken verarbeitet, wobei bei Speichermangel auf eine kleinere Blockgröße zurückgegriffen wird. Die Höhe und Breite der Ausgabe werden auf gerade Zahlen abgerundet. Wenn das Referenzbild einen Alphakanal hat (4 Kanäle), bleibt dieser Alphakanal erhalten und wird auf die Ausgabe angewendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `images` | Das ausgerichtete, farbkorrigierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/de.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
