> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/tr.md)

Bu düğüm, kontrol noktası ağırlıklarını yükleyerek ve hem model hem de CLIP bileşenlerine güç ayarlamaları uygulayarak bir kanca modelini LoRA (Düşük Dereceli Uyarlama) olarak oluşturur. Mevcut modellere kanca tabanlı bir yaklaşımla LoRA tarzı değişiklikler uygulamanıza olanak tanıyarak, kalıcı model değişiklikleri olmadan ince ayar ve uyarlama yapılmasını sağlar. Düğüm, önceki kancalarla birleşebilir ve verimlilik için yüklenen ağırlıkları önbelleğe alır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `ckpt_name` | STRING | Evet | Birden çok seçenek mevcut | Ağırlıkların yükleneceği kontrol noktası dosyası (mevcut kontrol noktalarından seçim yapın) |
| `strength_model` | FLOAT | Evet | -20,0 ile 20,0 | Model ağırlıklarına uygulanan güç çarpanı (varsayılan: 1,0) |
| `strength_clip` | FLOAT | Evet | -20,0 ile 20,0 | CLIP ağırlıklarına uygulanan güç çarpanı (varsayılan: 1,0) |
| `prev_hooks` | HOOKS | Hayır | - | Yeni oluşturulan LoRA kancalarıyla birleştirilecek isteğe bağlı önceki kancalar |

**Parametre Kısıtlamaları:**

- `ckpt_name` parametresi, mevcut kontrol noktaları klasöründen kontrol noktalarını yükler
- Her iki güç parametresi de 0,01 adım artışlarıyla -20,0 ile 20,0 arasında değerler kabul eder
- `prev_hooks` sağlanmadığında, düğüm yeni bir kanca grubu oluşturur
- Düğüm, aynı kontrol noktasının birden çok kez yeniden yüklenmesini önlemek için yüklenen ağırlıkları önbelleğe alır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `HOOKS` | HOOKS | Sağlanmışsa önceki kancalarla birleştirilmiş, oluşturulan LoRA kancaları |

---
**Source fingerprint (SHA-256):** `8c0dd6b2e8e99e1d7dbc864aa802c0713842fb0d4ee018ea5cbedfb7896a770d`
