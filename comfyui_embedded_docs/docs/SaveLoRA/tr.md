SaveLoRA düğümü, bir LoRA (Düşük Dereceli Uyarlama) modelini bir dosyaya kaydeder. Bir LoRA modelini girdi olarak alır ve çıktı dizinine bir `.safetensors` dosyası olarak yazar. Nihai dosya adına dahil edilmek üzere bir dosya adı öneki ve isteğe bağlı bir adım sayısı belirtebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `lora` | Kaydedilecek LoRA modeli. LoRA katmanlarına sahip modeli kullanmayın. | LORA_MODEL | Evet | Yok |
| `prefix` | Kaydedilen LoRA dosyası için kullanılacak önek (varsayılan: "loras/ComfyUI_trained_lora"). | STRING | Evet | Yok |
| `steps` | İsteğe bağlı: LoRA'nın eğitildiği adım sayısı, kaydedilen dosyayı adlandırmak için kullanılır. | INT | Hayır | Yok |

**Not:** `lora` girdisi saf bir LoRA modeli olmalıdır. Üzerine LoRA katmanları uygulanmış bir temel model sağlamayın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *Yok* | Bu düğüm, iş akışına herhangi bir veri çıktısı vermez. Diske bir dosya kaydeden bir çıktı düğümüdür. | Yok |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/tr.md)

---
**Source fingerprint (SHA-256):** `e68a449d741c908f23fc1585d848254d78c310ad19efbd139c33c9ddef3145c7`
