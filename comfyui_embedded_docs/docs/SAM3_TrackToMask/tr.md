# SAM3 İzden Maskeye

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/en.md)

## Genel Bakış

Bir SAM3 izleme oturumundan belirli izlenen nesneleri indeks numaralarına göre seçer ve bunları tek bir çıktı maskesinde birleştirir. Bu, izleme sonuçlarından hangi nesneleri tutacağınızı ve hangilerini yok sayacağınızı seçmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `iz_verisi` | Bir SAM3 izleyici düğümünden gelen, paketlenmiş maskeleri ve orijinal görüntü boyutunu içeren izleme verisi çıktısı. | SAM3TRACKDATA | Evet | Yok |
| `nesne_indeksleri` | Çıktı maskesine dahil edilecek, virgülle ayrılmış nesne indeksleri (örneğin, '0,2,3'). Boş bırakılırsa, izlenen tüm nesneler dahil edilir. | STRING | Hayır | Virgülle ayrılmış herhangi bir tam sayı listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `masks` | Her kare için, seçilen nesnelerin tek bir maskede birleştirildiği tek bir ikili maske. Hiçbir nesne seçilmezse veya izleme verisi yoksa, sıfır maskesi döndürür. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/tr.md)

---
**Source fingerprint (SHA-256):** `2da82effc4cdc6655d0d37e281858bf33f7b62d9056629ec810e3ff9b2e7b5a6`
