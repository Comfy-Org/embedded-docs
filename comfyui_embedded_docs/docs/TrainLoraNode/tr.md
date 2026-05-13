> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/tr.md)

TrainLoraNode, sağlanan latentler ve koşullandırma verilerini kullanarak bir difüzyon modeli üzerinde LoRA (Düşük Dereceli Uyarlama) modeli oluşturur ve eğitir. Özel eğitim parametreleri, optimize ediciler ve kayıp fonksiyonları ile bir modeli ince ayar yapmanızı sağlar. Düğüm, eğitilmiş LoRA ağırlıklarını, bir kayıp geçmişi haritasını ve tamamlanan toplam eğitim adım sayısını çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | LoRA'nın eğitileceği model. |
| `latents` | LATENT | Evet | - | Eğitim için kullanılacak latentler, modelin veri kümesi/girdisi olarak işlev görür. |
| `pozitif` | CONDITIONING | Evet | - | Eğitim için kullanılacak pozitif koşullandırma. |
| `toplu_iş_boyutu` | INT | Evet | 1-10000 | Eğitim için kullanılacak parti boyutu (varsayılan: 1). |
| `gradyan_birikim_adımları` | INT | Evet | 1-1024 | Eğitim için kullanılacak gradyan birikim adım sayısı (varsayılan: 1). |
| `adımlar` | INT | Evet | 1-100000 | LoRA'nın eğitileceği adım sayısı (varsayılan: 16). |
| `öğrenme_oranı` | FLOAT | Evet | 0.0000001-1.0 | Eğitim için kullanılacak öğrenme oranı (varsayılan: 0.0005). |
| `rütbe` | INT | Evet | 1-128 | LoRA katmanlarının derecesi (varsayılan: 8). |
| `optimize_edici` | COMBO | Evet | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | Eğitim için kullanılacak optimize edici (varsayılan: "AdamW"). |
| `kayıp_işlevi` | COMBO | Evet | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | Eğitim için kullanılacak kayıp fonksiyonu (varsayılan: "MSE"). |
| `tohum` | INT | Evet | 0-18446744073709551615 | Eğitim için kullanılacak tohum değeri (LoRA ağırlık başlatma ve gürültü örneklemesi için üreteçte kullanılır) (varsayılan: 0). |
| `eğitim_veri_tipi` | COMBO | Evet | "bf16"<br>"fp32"<br>"none" | Eğitim için kullanılacak veri türü. 'none' değeri, modelin yerel hesaplama veri türünü geçersiz kılmak yerine korur. fp16 modelleri için GradScaler otomatik olarak etkinleştirilir (varsayılan: "bf16"). |
| `lora_veri_tipi` | COMBO | Evet | "bf16"<br>"fp32" | LoRA için kullanılacak veri türü (varsayılan: "bf16"). |
| `quantized_backward` | BOOLEAN | Evet | - | 'none' eğitim veri türü kullanılırken ve nicelenmiş bir model üzerinde eğitim yapılırken, etkinleştirildiğinde geri yayılımın nicelenmiş matmul ile yapılmasını sağlar (varsayılan: False). |
| `algoritma` | COMBO | Evet | Birden çok seçenek mevcut | Eğitim için kullanılacak algoritma. |
| `gradyan_kontrol_noktası` | BOOLEAN | Evet | - | Eğitim için gradyan denetim noktası kullan (varsayılan: True). |
| `checkpoint_depth` | INT | Evet | 1-5 | Gradyan denetim noktası için derinlik seviyesi (varsayılan: 1). |
| `offloading` | BOOLEAN | Evet | - | GPU belleğinden tasarruf etmek için eğitim sırasında model ağırlıklarını CPU'ya boşalt (varsayılan: False). |
| `mevcut_lora` | COMBO | Evet | Birden çok seçenek mevcut | Eklenmek üzere mevcut LoRA. Yeni LoRA için Yok olarak ayarlayın (varsayılan: "[None]"). |
| `bucket_mode` | BOOLEAN | Evet | - | Çözünürlük kovası modunu etkinleştir. Etkinleştirildiğinde, ResolutionBucket düğümünden önceden kovalanmış latentler bekler (varsayılan: False). |
| `bypass_mode` | BOOLEAN | Evet | - | Eğitim için baypas modunu etkinleştir. Etkinleştirildiğinde, bağdaştırıcılar ağırlık değişikliği yerine ileri kancalar aracılığıyla uygulanır. Ağırlıkların doğrudan değiştirilemediği nicelenmiş modeller için kullanışlıdır (varsayılan: False). |

**Not:** Pozitif koşullandırma girdilerinin sayısı, latent görüntü sayısıyla eşleşmelidir. Birden çok görüntü ile yalnızca bir pozitif koşullandırma sağlanırsa, tüm görüntüler için otomatik olarak tekrarlanacaktır.

**`training_dtype` hakkında not:** "none" olarak ayarlandığında, modelin yerel hesaplama veri türü korunur. fp16 modelleri için GradScaler, gradyan hesaplaması sırasında taşmayı önlemek için otomatik olarak etkinleştirilir. `fp16_accumulation` da etkinleştirilmişse (`--fast` bayrakları aracılığıyla), bu kombinasyon sayısal olarak kararsız olabilir ve NaN değerlerine neden olabilir.

**`quantized_backward` hakkında not:** Bu parametre yalnızca `training_dtype` "none" olarak ayarlandığında ve model nicelenmiş bir model olduğunda geçerlidir. Geri yayılım geçişi sırasında nicelenmiş matris çarpımını etkinleştirir.

**`bypass_mode` hakkında not:** Etkinleştirildiğinde, bağdaştırıcılar model ağırlıklarını doğrudan değiştirmek yerine ileri kancalar aracılığıyla uygulanır. Bu, özellikle ağırlıkların doğrudan değiştirilemediği nicelenmiş modeller için kullanışlıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `kayıp_haritası` | LORA_MODEL | Kaydedilebilen veya diğer modellere uygulanabilen eğitilmiş LoRA ağırlıkları. |
| `adımlar` | LOSS_MAP | Zaman içindeki eğitim kaybı değerlerini içeren bir sözlük. |
| `adımlar` | INT | Tamamlanan toplam eğitim adım sayısı (mevcut LoRA'dan gelen önceki adımlar dahil). |

---
**Source fingerprint (SHA-256):** `df315ef416ff3ce81e6a526af2c4e5115980e6c35830825967e7189d4f8541d8`
