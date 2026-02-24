> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/tr.md)

SaveLoRA düğümü, bir LoRA (Düşük Dereceli Uyarlama) modelini bir dosyaya kaydeder. Bir LoRA modelini girdi olarak alır ve çıktı dizininde bir `.safetensors` dosyasına yazar. Dosya adı öneki ve isteğe bağlı olarak son dosya adına dahil edilecek bir adım sayısı belirleyebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `lora` | MODEL | Evet | Yok | Kaydedilecek LoRA modeli. LoRA katmanları içeren modeli kullanmayın. |
| `prefix` | STRING | Evet | Yok | Kaydedilen LoRA dosyası için kullanılacak önek (varsayılan: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | Hayır | Yok | İsteğe bağlı: LoRA'nın eğitildiği adım sayısı, kaydedilen dosyanın adlandırılmasında kullanılır. |

**Not:** `lora` girdisi saf bir LoRA modeli olmalıdır. Üzerine LoRA katmanları uygulanmış bir temel model sağlamayın.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Yok* | Yok | Bu düğüm, iş akışına herhangi bir veri çıktısı sağlamaz. Diske bir dosya kaydeden bir çıktı düğümüdür. |
