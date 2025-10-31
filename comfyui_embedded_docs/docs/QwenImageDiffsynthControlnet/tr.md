> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/tr.md)

QwenImageDiffsynthControlnet düğümü, bir temel modelin davranışını değiştirmek için bir difüzyon sentez kontrol ağı yaması uygular. Görüntü girişi ve isteğe bağlı bir maske kullanarak modelin üretim sürecini ayarlanabilir güçle yönlendirir ve kontrol ağının etkisini dahil eden yamalı bir model oluşturur, böylece daha kontrollü görüntü sentezi sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Kontrol ağı ile yamalanacak temel model |
| `model_patch` | MODEL_PATCH | Evet | - | Temel modele uygulanacak kontrol ağı yama modeli |
| `vae` | VAE | Evet | - | Difüzyon sürecinde kullanılan VAE (Varyasyonel Otokodlayıcı) |
| `image` | IMAGE | Evet | - | Kontrol ağını yönlendirmek için kullanılan giriş görüntüsü (sadece RGB kanalları kullanılır) |
| `strength` | FLOAT | Evet | -10.0 - 10.0 | Kontrol ağı etkisinin gücü (varsayılan: 1.0) |
| `mask` | MASK | Hayır | - | Kontrol ağının uygulanması gereken alanları tanımlayan isteğe bağlı maske (dahili olarak ters çevrilir) |

**Not:** Bir maske sağlandığında, otomatik olarak ters çevrilir (1.0 - mask) ve kontrol ağı işlemi için beklenen boyutlara uyacak şekilde yeniden şekillendirilir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Difüzyon sentez kontrol ağı yaması uygulanmış değiştirilmiş model |