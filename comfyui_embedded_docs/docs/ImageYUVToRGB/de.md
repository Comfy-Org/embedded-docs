# ImageYUVToRGB

Der Node ImageYUVToRGB wandelt Bilder im YUV-Farbraum in den RGB-Farbraum um. Er nimmt drei separate Eingabebilder entgegen, die die Komponenten Y (Luma), U (Blauprojektion) und V (Rotprojektion) repräsentieren, und kombiniert sie zu einem einzelnen RGB-Bild.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `Y` | Das Eingabebild für die Y-Komponente (Luminanz). Wenn das Bild mehr als drei Kanäle hat, werden nur die ersten drei verwendet und zu einem einzelnen Kanal gemittelt. | IMAGE | Ja | - |
| `U` | Das Eingabebild für die U-Komponente (Blauprojektion). Wenn das Bild mehr als drei Kanäle hat, werden nur die ersten drei verwendet und zu einem einzelnen Kanal gemittelt. | IMAGE | Ja | - |
| `V` | Das Eingabebild für die V-Komponente (Rotprojektion). Wenn das Bild mehr als drei Kanäle hat, werden nur die ersten drei verwendet und zu einem einzelnen Kanal gemittelt. | IMAGE | Ja | - |

**Hinweis:** Alle drei Eingabebilder (Y, U und V) müssen zusammen bereitgestellt werden und kompatible Abmessungen haben (übereinstimmende Höhe, Breite und Batch-Größe), damit die Konvertierung erfolgreich durchgeführt werden kann.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das konvertierte RGB-Bild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/de.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
