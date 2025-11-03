> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/tr.md)

TrainLoraNode, sağlanan latents ve conditioning verilerini kullanarak bir diffusion model üzerinde LoRA (Low-Rank Adaptation) modeli oluşturur ve eğitir. Özel eğitim parametreleri, optimizerlar ve kayıp fonksiyonları ile bir modeli ince ayar yapmanıza olanak tanır. Düğüm, LoRA uygulanmış eğitilmiş modeli, LoRA ağırlıklarını, eğitim kaybı metriklerini ve tamamlanan toplam eğitim adımlarını çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | LoRA eğitimi yapılacak model. |
| `latents` | LATENT | Evet | - | Eğitim için kullanılacak latents, modelin veri kümesi/girişi olarak hizmet eder. |
| `positive` | CONDITIONING | Evet | - | Eğitim için kullanılacak pozitif conditioning. |
| `batch_size` | INT | Evet | 1-10000 | Eğitim için kullanılacak batch boyutu (varsayılan: 1). |
| `grad_accumulation_steps` | INT | Evet | 1-1024 | Eğitim için kullanılacak gradyan biriktirme adım sayısı (varsayılan: 1). |
| `steps` | INT | Evet | 1-100000 | LoRA için eğitilecek adım sayısı (varsayılan: 16). |
| `learning_rate` | FLOAT | Evet | 0.0000001-1.0 | Eğitim için kullanılacak öğrenme oranı (varsayılan: 0.0005). |
| `rank` | INT | Evet | 1-128 | LoRA katmanlarının rank değeri (varsayılan: 8). |
| `optimizer` | COMBO | Evet | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | Eğitim için kullanılacak optimizer (varsayılan: "AdamW"). |
| `loss_function` | COMBO | Evet | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | Eğitim için kullanılacak kayıp fonksiyonu (varsayılan: "MSE"). |
| `seed` | INT | Evet | 0-18446744073709551615 | Eğitim için kullanılacak seed (LoRA ağırlık başlatma ve gürültü örnekleme için generator'da kullanılır) (varsayılan: 0). |
| `training_dtype` | COMBO | Evet | "bf16"<br>"fp32" | Eğitim için kullanılacak veri türü (varsayılan: "bf16"). |
| `lora_dtype` | COMBO | Evet | "bf16"<br>"fp32" | LoRA için kullanılacak veri türü (varsayılan: "bf16"). |
| `algorithm` | COMBO | Evet | Birden fazla seçenek mevcut | Eğitim için kullanılacak algoritma. |
| `gradient_checkpointing` | BOOLEAN | Evet | - | Eğitim için gradyan kontrol noktası kullanımı (varsayılan: True). |
| `existing_lora` | COMBO | Evet | Birden fazla seçenek mevcut | Eklenecek mevcut LoRA. Yeni LoRA için None olarak ayarlayın (varsayılan: "[None]"). |

**Not:** Pozitif conditioning girişlerinin sayısı, latent görüntülerin sayısıyla eşleşmelidir. Birden fazla görüntü ile yalnızca bir pozitif conditioning sağlanırsa, tüm görüntüler için otomatik olarak tekrarlanacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_with_lora` | MODEL | Eğitilmiş LoRA'nın uygulandığı orijinal model. |
| `lora` | LORA_MODEL | Kaydedilebilen veya diğer modellere uygulanabilen eğitilmiş LoRA ağırlıkları. |
| `loss` | LOSS_MAP | Zaman içindeki eğitim kaybı değerlerini içeren bir sözlük. |
| `steps` | INT | Tamamlanan toplam eğitim adım sayısı (mevcut LoRA'dan önceki adımlar dahil). |