> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/tr.md)

SaveLoRA düğümü, LoRA (Düşük Dereceli Uyarlama) modellerini çıktı dizininize kaydeder. Bir LoRA modelini girdi olarak alır ve otomatik olarak oluşturulmuş bir dosya adıyla bir safetensors dosyası oluşturur. Dosya adı önekini özelleştirebilir ve daha iyi organizasyon için isteğe bağlı olarak dosya adına eğitim adım sayısını dahil edebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `lora` | LORA_MODEL | Evet | - | Kaydedilecek LoRA modeli. LoRA katmanları içeren modeli kullanmayın. |
| `prefix` | STRING | Evet | - | Kaydedilen LoRA dosyası için kullanılacak önek (varsayılan: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | Hayır | - | İsteğe bağlı: LoRA'nın eğitildiği adım sayısı, kaydedilen dosyanın adlandırılmasında kullanılır. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Yok* | - | Bu düğüm herhangi bir çıktı döndürmez, ancak LoRA modelini çıktı dizinine kaydeder. |