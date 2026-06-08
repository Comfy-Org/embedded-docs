SaveLoRA düğümü, LoRA (Düşük Dereceli Uyarlama) modellerini çıktı dizininize kaydeder. Giriş olarak bir LoRA modeli alır ve otomatik olarak oluşturulan bir dosya adıyla bir safetensors dosyası oluşturur. Dosya adı önekini özelleştirebilir ve isteğe bağlı olarak daha iyi organizasyon için dosya adına eğitim adım sayısını dahil edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `lora` | Kaydedilecek LoRA modeli. LoRA katmanlarına sahip modeli kullanmayın. | LORA_MODEL | Evet | - |
| `prefix` | Kaydedilen LoRA dosyası için kullanılacak önek (varsayılan: "loras/ComfyUI_trained_lora"). | STRING | Evet | - |
| `steps` | İsteğe bağlı: LoRA'nın eğitildiği adım sayısı, kaydedilen dosyayı adlandırmak için kullanılır. | INT | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *Yok* | Bu düğüm herhangi bir çıktı döndürmez ancak LoRA modelini çıktı dizinine kaydeder. | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/tr.md)

---
**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`
