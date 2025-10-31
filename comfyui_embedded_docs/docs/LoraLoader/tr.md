> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/tr.md)

Bu düğüm, LoRA klasöründeki (alt klasörler dahil) modelleri otomatik olarak algılar. İlgili model yolu `ComfyUI\models\loras` şeklindedir. Daha fazla bilgi için LoRA Modellerini Yükleme bölümüne bakınız.

LoRA Yükleyici düğümü, temel olarak LoRA modellerini yüklemek için kullanılır. LoRA modellerini, görüntülerinize belirli stiller, içerikler ve detaylar katabilen filtreler olarak düşünebilirsiniz:

- Belirli sanatsal stiller uygulama (mürekkep boyama gibi)
- Belirli karakterlerin özelliklerini ekleme (oyun karakterleri gibi)
- Görüntüye spesifik detaylar ekleme
Bunların tümü LoRA aracılığıyla gerçekleştirilebilir.

Birden fazla LoRA modeli yüklemeniz gerekiyorsa, aşağıda gösterildiği gibi doğrudan birden fazla düğümü birbirine zincirleyebilirsiniz:

## Girdiler

| Parametre | Veri Türü | Açıklama |
| --- | --- | --- |
| `model` | MODEL | Genellikle temel modeli bağlamak için kullanılır |
| `clip` | CLIP | Genellikle CLIP modelini bağlamak için kullanılır |
| `lora_name` | COMBO[STRING] | Kullanılacak LoRA modelinin adını seçin |
| `strength_model` | FLOAT | -100.0 ile 100.0 arasında değer aralığı, günlük görüntü oluşturma için genellikle 0~1 arasında kullanılır. Daha yüksek değerler, model ayarlama etkilerini daha belirgin hale getirir |
| `strength_clip` | FLOAT | -100.0 ile 100.0 arasında değer aralığı, günlük görüntü oluşturma için genellikle 0~1 arasında kullanılır. Daha yüksek değerler, model ayarlama etkilerini daha belirgin hale getirir |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
| --- | --- | --- |
| `model` | MODEL | LoRA ayarlamaları uygulanmış model |
| `clip` | CLIP | LoRA ayarlamaları uygulanmış CLIP örneği |