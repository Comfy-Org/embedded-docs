> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/tr.md)

Bu düğüm, kontrol noktası ağırlıklarını yükleyerek ve hem model hem de CLIP bileşenlerine güç ayarlamaları uygulayarak bir kanca modelini LoRA (Düşük Dereceli Uyarlama) olarak oluşturur. Mevcut modellere, kalıcı model değişiklikleri yapmadan ince ayar ve uyarlama sağlayan, kanca tabanlı bir yaklaşım aracılığıyla LoRA tarzı değişiklikler uygulamanıza olanak tanır. Düğüm, önceki kancalarla birleşebilir ve verimlilik için yüklenen ağırlıkları önbelleğe alır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | COMBO | Evet | Birden fazla seçenek mevcut | Ağırlıkların yükleneceği kontrol noktası dosyası (mevcut kontrol noktalarından seçin) |
| `strength_model` | FLOAT | Evet | -20.0 - 20.0 | Model ağırlıklarına uygulanan güç çarpanı (varsayılan: 1.0) |
| `strength_clip` | FLOAT | Evet | -20.0 - 20.0 | CLIP ağırlıklarına uygulanan güç çarpanı (varsayılan: 1.0) |
| `prev_hooks` | HOOKS | Hayır | - | Yeni oluşturulan LoRA kancalarıyla birleştirmek için isteğe bağlı önceki kancalar |

**Parametre Kısıtlamaları:**

- `ckpt_name` parametresi, mevcut kontrol noktaları klasöründen kontrol noktalarını yükler
- Her iki güç parametresi de -20.0 ile 20.0 arasında, 0.01 adım artışlarıyla değerler kabul eder
- `prev_hooks` sağlanmadığında, düğüm yeni bir kanca grubu oluşturur
- Düğüm, aynı kontrol noktasını birden fazla kez yeniden yüklemekten kaçınmak için yüklenen ağırlıkları önbelleğe alır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Oluşturulan LoRA kancaları, sağlandıysa önceki kancalarla birleştirilmiş |