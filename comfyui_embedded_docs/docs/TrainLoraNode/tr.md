# LoRA Eğit

TrainLoraNode, sağlanan latentler ve koşullandırma verilerini kullanarak bir difüzyon modeli üzerinde LoRA (Düşük Dereceli Uyarlama) modeli oluşturur ve eğitir. Özel eğitim parametreleri, optimize ediciler ve kayıp fonksiyonları ile bir modeli ince ayar yapmanızı sağlar. Düğüm, eğitilmiş LoRA ağırlıklarını, bir kayıp geçmişi haritasını ve tamamlanan toplam eğitim adım sayısını çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'nın eğitileceği model. | MODEL | Evet | - |
| `latents` | Eğitim için kullanılacak latentler, modelin veri kümesi/girdisi olarak işlev görür. | LATENT | Evet | - |
| `pozitif` | Eğitim için kullanılacak pozitif koşullandırma. | CONDITIONING | Evet | - |
| `toplu_iş_boyutu` | Eğitim için kullanılacak parti boyutu (varsayılan: 1). | INT | Evet | 1-10000 |
| `gradyan_birikim_adımları` | Eğitim için kullanılacak gradyan birikim adım sayısı (varsayılan: 1). | INT | Evet | 1-1024 |
| `adımlar` | LoRA'nın eğitileceği adım sayısı (varsayılan: 16). | INT | Evet | 1-100000 |
| `öğrenme_oranı` | Eğitim için kullanılacak öğrenme oranı (varsayılan: 0.0005). | FLOAT | Evet | 0.0000001-1.0 |
| `rütbe` | LoRA katmanlarının derecesi (varsayılan: 8). | INT | Evet | 1-128 |
| `optimize_edici` | Eğitim için kullanılacak optimize edici (varsayılan: "AdamW"). | COMBO | Evet | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" |
| `kayıp_işlevi` | Eğitim için kullanılacak kayıp fonksiyonu (varsayılan: "MSE"). | COMBO | Evet | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" |
| `tohum` | Eğitim için kullanılacak tohum değeri (LoRA ağırlık başlatma ve gürültü örneklemesi için üreteçte kullanılır) (varsayılan: 0). | INT | Evet | 0-18446744073709551615 |
| `eğitim_veri_tipi` | Eğitim için kullanılacak veri türü. 'none' değeri, modelin yerel hesaplama veri türünü geçersiz kılmak yerine korur. fp16 modelleri için GradScaler otomatik olarak etkinleştirilir (varsayılan: "bf16"). | COMBO | Evet | "bf16"<br>"fp32"<br>"none" |
| `lora_veri_tipi` | LoRA için kullanılacak veri türü (varsayılan: "bf16"). | COMBO | Evet | "bf16"<br>"fp32" |
| `quantized_backward` | 'none' eğitim veri türü kullanılırken ve nicelenmiş bir model üzerinde eğitim yapılırken, etkinleştirildiğinde geri yayılımın nicelenmiş matmul ile yapılmasını sağlar (varsayılan: False). | BOOLEAN | Evet | - |
| `algoritma` | Eğitim için kullanılacak algoritma. | COMBO | Evet | Birden çok seçenek mevcut |
| `gradyan_kontrol_noktası` | Eğitim için gradyan denetim noktası kullan (varsayılan: True). | BOOLEAN | Evet | - |
| `checkpoint_depth` | Gradyan denetim noktası için derinlik seviyesi (varsayılan: 1). | INT | Evet | 1-5 |
| `offloading` | GPU belleğinden tasarruf etmek için eğitim sırasında model ağırlıklarını CPU'ya boşalt (varsayılan: False). | BOOLEAN | Evet | - |
| `mevcut_lora` | Eklenmek üzere mevcut LoRA. Yeni LoRA için Yok olarak ayarlayın (varsayılan: "[None]"). | COMBO | Evet | Birden çok seçenek mevcut |
| `bucket_mode` | Çözünürlük kovası modunu etkinleştir. Etkinleştirildiğinde, ResolutionBucket düğümünden önceden kovalanmış latentler bekler (varsayılan: False). | BOOLEAN | Evet | - |
| `bypass_mode` | Eğitim için baypas modunu etkinleştir. Etkinleştirildiğinde, bağdaştırıcılar ağırlık değişikliği yerine ileri kancalar aracılığıyla uygulanır. Ağırlıkların doğrudan değiştirilemediği nicelenmiş modeller için kullanışlıdır (varsayılan: False). | BOOLEAN | Evet | - |

**Not:** Pozitif koşullandırma girdilerinin sayısı, latent görüntü sayısıyla eşleşmelidir. Birden çok görüntü ile yalnızca bir pozitif koşullandırma sağlanırsa, tüm görüntüler için otomatik olarak tekrarlanacaktır.

**`training_dtype` hakkında not:** "none" olarak ayarlandığında, modelin yerel hesaplama veri türü korunur. fp16 modelleri için GradScaler, gradyan hesaplaması sırasında taşmayı önlemek için otomatik olarak etkinleştirilir. `fp16_accumulation` da etkinleştirilmişse (`--fast` bayrakları aracılığıyla), bu kombinasyon sayısal olarak kararsız olabilir ve NaN değerlerine neden olabilir.

**`quantized_backward` hakkında not:** Bu parametre yalnızca `training_dtype` "none" olarak ayarlandığında ve model nicelenmiş bir model olduğunda geçerlidir. Geri yayılım geçişi sırasında nicelenmiş matris çarpımını etkinleştirir.

**`bypass_mode` hakkında not:** Etkinleştirildiğinde, bağdaştırıcılar model ağırlıklarını doğrudan değiştirmek yerine ileri kancalar aracılığıyla uygulanır. Bu, özellikle ağırlıkların doğrudan değiştirilemediği nicelenmiş modeller için kullanışlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `kayıp_haritası` | Kaydedilebilen veya diğer modellere uygulanabilen eğitilmiş LoRA ağırlıkları. | LORA_MODEL |
| `adımlar` | Zaman içindeki eğitim kaybı değerlerini içeren bir sözlük. | LOSS_MAP |
| `adımlar` | Tamamlanan toplam eğitim adım sayısı (mevcut LoRA'dan gelen önceki adımlar dahil). | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/tr.md)

---
**Source fingerprint (SHA-256):** `df315ef416ff3ce81e6a526af2c4e5115980e6c35830825967e7189d4f8541d8`
