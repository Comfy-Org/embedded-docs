# BoşGizliHunyuan3Dv2

Bu düğüm, Hunyuan3Dv2 3B üretim modelleri için biçimlendirilmiş boş (tamamı sıfır) latent örneklerinden oluşan bir toplu iş oluşturur. 3B üretim iş akışları için başlangıç noktası görevi gören doğru şekle sahip latent tensörünü üretir; latent, "hunyuan3dv2" türüyle etiketlenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `resolution` | Oluşturulacak latent uzayının çözünürlük boyutu (varsayılan: 3072) | INT | Evet | 1 - 8192 |
| `batch_size` | Toplu işteki latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | [batch_size, 64, resolution] şeklinde, sıfırla doldurulmuş örnekler içeren boş bir latent tensörü; "hunyuan3dv2" türüyle etiketlenmiştir | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/tr.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
