# Recraft Net Büyütme Görüntüsü

Bu düğüm, bir görüntüyü "crisp upscale" aracını kullanarak senkron olarak büyütür. Verilen bir raster görüntüyü çözünürlüğünü artırarak geliştirir; görüntüyü daha keskin ve daha temiz hale getirir. Bir görüntü grubu sağlandığında, her görüntü bağımsız olarak işlenir ve büyütülmüş sonuçlar bir grup olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Büyütülecek girdi görüntüsü. Bir görüntü grubunu kabul eder; her görüntü bağımsız olarak işlenir. | IMAGE | Evet | — |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Geliştirilmiş çözünürlük ve netliğe sahip, büyütülmüş görüntü. Girdi olarak bir görüntü grubu sağlanmışsa, bir görüntü grubu döndürür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `7a60c563504df7a81ce5d50e989bc4a8853f4bb30805a014c9fb567d8ec83e33`
