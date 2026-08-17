# BoşGizliHunyuan3Dv2

EmptyLatentHunyuan3Dv2 düğümü, Hunyuan3Dv2 3B üretim modelleri için özel olarak biçimlendirilmiş boş latent tensörler oluşturur. Hunyuan3Dv2 mimarisinin gerektirdiği doğru boyut ve yapıya sahip boş latent alanları üreterek, 3B üretim iş akışlarına sıfırdan başlamanızı sağlar. Düğüm, sonraki 3B üretim süreçleri için temel görevi gören sıfırlarla dolu latent tensörler üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `resolution` | Latent alanı için çözünürlük boyutu (varsayılan: 3072) | INT | Evet | 1 - 8192 |
| `batch_size` | Partideki latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Hunyuan3Dv2 3B üretim için biçimlendirilmiş boş örnekler içeren bir latent tensör döndürür | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/tr.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
