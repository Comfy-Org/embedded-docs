Bu düğüm, LoRA klasöründe (alt klasörler dahil) bulunan modelleri, ilgili model yolu `ComfyUI\models\loras` olacak şekilde otomatik olarak algılar. Daha fazla bilgi için lütfen LoRA Modellerini Yükleme bölümüne bakın.

LoRA Yükleyici düğümü, öncelikle LoRA modellerini yüklemek için kullanılır. LoRA modellerini, görsellerinize belirli stiller, içerikler ve detaylar kazandırabilen filtreler olarak düşünebilirsiniz:

- Belirli sanatsal stiller uygulayın (mürekkep boyama gibi)
- Belirli karakterlerin özelliklerini ekleyin (oyun karakterleri gibi)
- Görsele belirli detaylar ekleyin
Tüm bunlar LoRA aracılığıyla elde edilebilir.

Birden fazla LoRA modeli yüklemeniz gerekiyorsa, aşağıda gösterildiği gibi birden fazla düğümü doğrudan birbirine bağlayabilirsiniz:

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Genellikle temel modele bağlanmak için kullanılır | MODEL |
| `clip` | Genellikle CLIP modeline bağlanmak için kullanılır | CLIP |
| `lora_adı` | Kullanılacak LoRA modelinin adını seçin | COMBO[STRING] |
| `model_gücü` | Değer aralığı -100,0 ile 100,0 arasındadır, günlük görsel üretiminde genellikle 0~1 arasında kullanılır. Daha yüksek değerler, model ayarlama efektlerinin daha belirgin olmasını sağlar | FLOAT |
| `clip_gücü` | Değer aralığı -100,0 ile 100,0 arasındadır, günlük görsel üretiminde genellikle 0~1 arasında kullanılır. Daha yüksek değerler, model ayarlama efektlerinin daha belirgin olmasını sağlar | FLOAT |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | LoRA ayarlamaları uygulanmış model | MODEL |
| `clip` | LoRA ayarlamaları uygulanmış CLIP örneği | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/tr.md)
