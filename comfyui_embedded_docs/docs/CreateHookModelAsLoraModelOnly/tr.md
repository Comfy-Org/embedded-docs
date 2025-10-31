> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/tr.md)

Bu düğüm, bir sinir ağının yalnızca model bileşenini değiştirmek için bir LoRA (Düşük Dereceli Uyarlama) modeli uygulayan bir kanca oluşturur. Bir kontrol noktası dosyası yükler ve onu model bileşenine belirtilen bir güçle uygularken, CLIP bileşenini değiştirmeden bırakır. Bu, temel CreateHookModelAsLora sınıfının işlevselliğini genişleten deneysel bir düğümdür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Evet | Birden fazla seçenek mevcut | LoRA modeli olarak yüklenecek kontrol noktası dosyası. Mevcut seçenekler kontrol noktaları klasörünün içeriğine bağlıdır. |
| `strength_model` | FLOAT | Evet | -20.0 - 20.0 | LoRA'nın model bileşenine uygulanması için güç çarpanı (varsayılan: 1.0) |
| `prev_hooks` | HOOKS | Hayır | - | Bu kanca ile zincirlenecek isteğe bağlı önceki kancalar |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `hooks` | HOOKS | LoRA model değişikliğini içeren oluşturulan kanca grubu |