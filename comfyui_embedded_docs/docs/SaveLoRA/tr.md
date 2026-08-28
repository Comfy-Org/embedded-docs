# LoRA Ağırlıklarını Kaydet

SaveLoRA düğümü, bir LoRA (Düşük Dereceli Uyarlama) modelini bir dosyaya kaydeder. Girdi olarak bir LoRA modeli alır ve bunu çıktı dizinindeki bir `.safetensors` dosyasına yazar. Son dosya adına dahil edilmek üzere bir dosya adı öneki ve isteğe bağlı bir adım sayısı belirtebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `lora` | Kaydedilecek LoRA modeli. LoRA katmanları içeren modeli kullanmayın. | LORA_MODEL | Evet | N/A |
| `prefix` | Kaydedilen LoRA dosyası için kullanılacak önek (varsayılan: "loras/ComfyUI_trained_lora"). | STRING | Evet | N/A |
| `steps` | İsteğe bağlı: LoRA'nın eğitildiği adım sayısı; kaydedilen dosyayı adlandırmak için kullanılır. | INT | Hayır | N/A |

**Not:** `lora` girdisi saf bir LoRA modeli olmalıdır. Üzerine LoRA katmanları uygulanmış bir temel model sağlamayın.

**Not:** Dosya, ComfyUI çıktı dizinine `.safetensors` uzantısıyla kaydedilir. Dosya adı, mevcut dosyaların üzerine yazılmasını önlemek için `prefix` ve sıfırla doldurulmuş bir sayaçtan (5 basamak) oluşturulur. `steps` sağlandığında, adım sayısı da dosya adına dahil edilir (örneğin, 1000 adım için `1000_steps`).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *None* | Bu düğüm, iş akışına herhangi bir veri çıktısı vermez. Dosyayı diske kaydeden bir çıktı düğümüdür. | N/A |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/tr.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
