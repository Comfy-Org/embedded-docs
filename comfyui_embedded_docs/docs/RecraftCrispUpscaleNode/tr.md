# Recraft Net Büyütme Görüntüsü

'crisp upscale' aracını kullanarak bir girdi görüntüsünü senkronize şekilde büyütür, çözünürlüğünü artırır ve daha keskin ve temiz hale getirir. Girdi batch'indeki her görüntü bağımsız olarak işlenir ve büyütülmüş sonuçlar bir batch olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Büyütülecek girdi görüntüsü. Bir batch görüntü kabul eder. | IMAGE | Evet | — |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Geliştirilmiş çözünürlük ve netliğe sahip büyütülmüş görüntü. Girdi olarak bir batch sağlandıysa bir batch görüntü döndürür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `7a60c563504df7a81ce5d50e989bc4a8853f4bb30805a014c9fb567d8ec83e33`
