# WaveSpeed-Bild-Upscaling

Der WaveSpeed Image Upscale-Node verwendet einen externen KI-Dienst, um die Auflösung und Qualität eines Bildes zu erhöhen. Er nimmt ein einzelnes Eingabefoto entgegen und skaliert es auf eine höhere Zielauflösung wie 2K, 4K oder 8K hoch, wodurch ein schärferes und detaillierteres Ergebnis entsteht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das für die Hochskalierung zu verwendende KI-Modell. „SeedVR2“ und „Ultimate“ bieten unterschiedliche Qualitäts- und Preisstufen. | STRING | Ja | `"SeedVR2"`<br>`"Ultimate"` |
| `image` | Das Eingabebild, das hochskaliert werden soll. Es ist genau ein Bild erforderlich. | IMAGE | Ja | |
| `target_resolution` | Die gewünschte Ausgabeauflösung für das hochskalierte Bild. | STRING | Ja | `"2K"`<br>`"4K"`<br>`"8K"` |

**Hinweis:** Dieser Node erfordert genau ein Eingabebild. Die Angabe eines Bilderstapels führt zu einem Fehler.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `image` | Das hochskalierte Ausgabebild in hoher Auflösung. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/de.md)

---
**Source fingerprint (SHA-256):** `1d715431efb690d30d9fc3b4769047a9d568b49c62eb318615e2748c780b8c20`
