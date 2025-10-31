> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/tr.md)

LoraSave düğümü, model farklılıklarından LoRA (Low-Rank Adaptation) dosyalarını çıkarır ve kaydeder. Difüzyon modeli farklılıklarını, metin kodlayıcı farklılıklarını veya her ikisini birden işleyebilir ve bunları belirtilen rank ve türde LoRA formatına dönüştürür. Ortaya çıkan LoRA dosyası, daha sonra kullanılmak üzere çıktı dizinine kaydedilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `dosyaadı_öneki` | STRING | Evet | - | Çıktı dosya adı için önek (varsayılan: "loras/ComfyUI_extracted_lora") |
| `rütbe` | INT | Evet | 1-4096 | LoRA için rank değeri, boyutu ve karmaşıklığı kontrol eder (varsayılan: 8) |
| `lora_türü` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulacak LoRA'nın türü, çeşitli mevcut seçeneklerle |
| `yanlılık_farkı` | BOOLEAN | Evet | - | LoRA hesaplamasında bias farklılıklarının dahil edilip edilmeyeceği (varsayılan: True) |
| `model_farkı` | MODEL | Hayır | - | Bir loraya dönüştürülecek ModelSubtract çıktısı |
| `metin_kodlayıcı_farkı` | CLIP | Hayır | - | Bir loraya dönüştürülecek CLIPSubtract çıktısı |

**Not:** Düğümün çalışması için `model_diff` veya `text_encoder_diff` parametrelerinden en az birinin sağlanması gerekir. Eğer her ikisi de atlanırsa, düğüm herhangi bir çıktı üretmeyecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| - | - | Bu düğüm, bir LoRA dosyasını çıktı dizinine kaydeder ancak iş akışı üzerinden herhangi bir veri döndürmez |