> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/tr.md)

Bu düğüm, yalnızca model bileşenine uygulanan bir LoRA (Düşük Dereceli Uyarlama) kancası oluşturur ve CLIP bileşenini etkilemeden model davranışını değiştirmenize olanak tanır. Bir LoRA dosyası yükler ve CLIP bileşenini değiştirmeden bırakarak, belirtilen bir güçle modele uygular. Düğüm, karmaşık değişiklik işlem hatları oluşturmak için önceki kancalarla zincirlenebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `lora_adı` | STRING | Evet | Birden fazla seçenek mevcut | loras klasöründen yüklenecek LoRA dosyasının adı |
| `model_gücü` | FLOAT | Evet | -20.0 ile 20.0 arası | Model bileşenine LoRA uygulama güç çarpanı (varsayılan: 1.0) |
| `önceki_kancalar` | HOOKS | Hayır | - | Bu kanca ile zincirlenecek isteğe bağlı önceki kancalar |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Model işlemeye uygulanabilen oluşturulmuş LoRA kancası |