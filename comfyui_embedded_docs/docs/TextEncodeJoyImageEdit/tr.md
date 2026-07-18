# TextEncodeJoyImageEdit

Bu düğüm, JoyImage modelleriyle kullanılmak üzere bir metin istemini ve isteğe bağlı görüntüleri koşullandırma verilerine kodlar. Görüntü oluşturma veya düzenleme görevlerine yön verebilecek zengin koşullandırma oluşturmak için bir CLIP metin kodlayıcısını isteğe bağlı görüntü girdileriyle birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Metin istemini kodlamak için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | Kodlanacak metin istemi; çok satırlı girdi ve dinamik istemleri destekler | STRING | Evet | - |
| `vae` | Görüntüleri potansiyel uzaya kodlamak için bir VAE modeli (isteğe bağlı) | VAE | Hayır | - |
| `images` | Koşullandırmaya dahil edilecek bir veya daha fazla görüntü; en fazla 6 görüntü | IMAGE | Hayır | 0 ila 6 görüntü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Metin istemi ve sağlanan tüm görüntüleri birleştiren kodlanmış koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`
