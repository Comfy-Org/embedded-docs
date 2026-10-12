# VOIDWarpedNoise

Erzeugt zeitlich korreliertes Rauschen für den zweiten Durchgang des VOID-Video-Verfeinerungsprozesses. Es nimmt das Ausgabevideo von Pass 1 und warpt gaußsches Rauschen entlang optischer Flussvektoren, sodass sich das Rauschen konsistent mit dem Videoinhalt bewegt. Das resultierende gewarpete Rauschen wird als Start-Latent für Pass 2 verwendet, wodurch die zeitliche Konsistenz in der endgültigen Ausgabe verbessert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `optical_flow` | Optisches Flussmodell von OpticalFlowLoader (RAFT-large). | OPTICAL_FLOW | Ja | - |
| `video` | Ausgabevideoframes von Pass 1 [T, H, W, 3]. | IMAGE | Ja | - |
| `width` | Zielbreite in Pixeln (Standard: 672). Das Eingabevideo wird vor der Rauscherzeugung auf diese Breite skaliert, und die Latent-Breite wird als Breite ÷ 8 abgeleitet. | INT | Ja | 16 bis MAX_RESOLUTION (Schritt 8) |
| `height` | Zielhöhe in Pixeln (Standard: 384). Das Eingabevideo wird vor der Rauscherzeugung auf diese Höhe skaliert, und die Latent-Höhe wird als Höhe ÷ 8 abgeleitet. | INT | Ja | 16 bis MAX_RESOLUTION (Schritt 8) |
| `length` | Anzahl der Pixel-Frames. Wird abgerundet, damit latent_t gerade ist (Anforderung patch_size_t=2), z. B. 49 zu 45 (Standard: 45). | INT | Ja | 1 bis MAX_RESOLUTION (Schritt 1) |
| `batch_size` | Anzahl identischer gewarpeter Rauschsequenzen, die erzeugt werden (Standard: 1). Das erzeugte Rauschen wird so oft entlang der Batch-Dimension wiederholt. | INT | Ja | 1 bis 64 |

**Hinweis zum Parameter `length`:** Der Wert `length` wird automatisch auf den nächstniedrigeren Wert abgerundet, der eine gerade `latent_t`-Dimension erzeugt, wie es die `patch_size_t=2`-Einschränkung des Modells CogVideoX-Fun-V1.5 erfordert (zum Beispiel wird 49 zu 45). Der Node protokolliert eine Warnung, wenn diese Rundung erfolgt. Frames jenseits des angepassten `length` werden ignoriert, und das Rauschen wird auf die resultierende Latent-Frame-Anzahl neu abgetastet.

**Hinweis zu `width` und `height`:** Diese Werte werden sowohl zum Skalieren der eingehenden Videoframes (bilinear, mittiger Zuschnitt) als auch zur Bestimmung der endgültigen Latent-Auflösung (geteilt durch 8) verwendet. Wenn das erzeugte Rauschen nicht der angeforderten Latent-Größe entspricht, wird es passend skaliert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `warped_noise` | Ein 5D-Tensor (B, C, T, H, W), der durch optischen Fluss gewarpetes gaußsches Rauschen enthält und zur Verwendung als initiales Latent in VOID Pass 2 bereitsteht. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/de.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
