> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/tr.md)

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/en.md)

## Genel Bakış

Bir SAM3 izleme oturumundan belirli izlenen nesneleri indeks numaralarına göre seçer ve bunları tek bir çıktı maskesinde birleştirir. Bu, izleme sonuçlarından hangi nesneleri tutacağınızı ve hangilerini yok sayacağınızı seçmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `track_data` | SAM3TRACKDATA | Evet | Yok | Bir SAM3 izleyici düğümünden gelen, paketlenmiş maskeleri ve orijinal görüntü boyutunu içeren izleme verisi çıktısı. |
| `object_indices` | STRING | Hayır | Virgülle ayrılmış herhangi bir tam sayı listesi | Çıktı maskesine dahil edilecek, virgülle ayrılmış nesne indeksleri (örneğin, '0,2,3'). Boş bırakılırsa, izlenen tüm nesneler dahil edilir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `masks` | MASK | Her kare için, seçilen nesnelerin tek bir maskede birleştirildiği tek bir ikili maske. Hiçbir nesne seçilmezse veya izleme verisi yoksa, sıfır maskesi döndürür. |

---
**Source fingerprint (SHA-256):** `2da82effc4cdc6655d0d37e281858bf33f7b62d9056629ec810e3ff9b2e7b5a6`
