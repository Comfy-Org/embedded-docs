# Görüntü Yükle (Çıktılardan)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

LoadImageOutput düğümü, çıktı klasöründen görüntüleri yükler. Yenile düğmesine tıkladığınızda, mevcut görüntülerin listesini günceller ve otomatik olarak ilkini seçer; bu sayede oluşturduğunuz görüntüler arasında kolayca geçiş yapabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Çıktı klasöründen bir görüntü yükleyin. Görüntü listesini güncellemek için bir yükleme seçeneği ve yenile düğmesi içerir. Yenile düğmesine tıklandığında, düğüm görüntü listesini günceller ve otomatik olarak ilk görüntüyü seçerek kolay geçiş yapılmasını sağlar. | COMBO | Evet | Birden çok seçenek mevcut |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Çıktı klasöründen yüklenen görüntü | IMAGE |
| `mask` | Yüklenen görüntüyle ilişkili maske | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/tr.md)

---
**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`
