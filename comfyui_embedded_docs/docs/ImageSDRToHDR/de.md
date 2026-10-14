# Convert SDR to HDR

Der **Convert SDR to HDR**-Node erweitert sRGB-Bilder mit Standard-Dynamic-Range zu Rec.2020 HLG HDR. Er behält das bestehende Aussehen des Bildes bei und ordnet dessen Helligkeit in einen größeren Bereich ein, daher muss das Ergebnis mit ausgewähltem HDR-Farbraum gespeichert werden. Alpha bleibt unverändert erhalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das/die SDR-Bild(er) in sRGB, das/die zu HDR erweitert werden soll(en). | IMAGE | Ja | - |
| `algorithm` | HDR-Erweiterungsalgorithmus. Die Auswahl eines Algorithmus blendet dessen Parameter (`target_luminance`) ein. | DYNAMIC_COMBO | Ja | `"lottes"` |

### lottes Eingaben

Diese Parameter erscheinen, wenn `algorithm` auf `"lottes"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `target_luminance` | Spitzenweiß-Zielwert in Nits. 0 behält die kalibrierte Darstellung bei. Dunkle Bilder werden nicht auf diesen Spitzenwert normalisiert. (Standard: 650.0) | FLOAT | Ja | 0.0 bis 10000.0 (Schritt 1.0) |

Jedes Bild des Stapels wird separat konvertiert: Die sRGB-Kodierung wird in lineares Licht invertiert, die Helligkeit wird mit einer rationalen Kurve im Lottes-Stil erweitert, die mit einer kalibrierten monotonen Log-Gain-Kurve gemischt wird, und das Ergebnis wird anschließend als Rec.2020 HLG neu kodiert. Da die Ausgabe HDR ist, muss der Speicher-Node den Farbraum `HDR` verwenden; beim Speichern als sRGB wird die Helligkeit falsch dargestellt.

HLG geht von einem Referenzdisplay mit 1000 Nits aus, daher behalten `target_luminance`-Werte unter 1000 diese Referenz bei, und ein Wert von `0` lässt die kalibrierte Darstellung unverändert. Einkanalige Bilder werden vor der Konvertierung auf drei Kanäle erweitert, und der Alphakanal wird unverändert übernommen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das/die Rec.2020-HLG-HDR-Bild(er). | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/de.md)

---
**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`
