> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/tr.md)

Bu düğüm, yalnızca model bileşenine uygulanan bir LoRA (Düşük Dereceli Uyarlama) kancası oluşturur ve CLIP bileşenini tamamen değiştirmez. Belirtilen güçte bir LoRA dosyası yükler ve model üzerinde uygularken CLIP gücünü sıfıra ayarlar. Bu düğüm, önceki kancalarla zincirlenerek karmaşık değişiklik hatları oluşturulmasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | Evet | Birden çok seçenek mevcut | loras klasöründen yüklenecek LoRA dosyasının adı |
| `strength_model` | FLOAT | Evet | -20.0 ila 20.0 | LoRA'nın model bileşenine uygulanması için güç çarpanı (varsayılan: 1.0) |
| `prev_hooks` | HOOKS | Hayır | - | Bu kanca ile zincirlenecek isteğe bağlı önceki kancalar |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `hooks` | HOOKS | Model işlemeye uygulanabilen oluşturulan LoRA kancası |

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`
