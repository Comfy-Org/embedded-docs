# Kanca LoRA Oluştur (Sadece Model)

Bu düğüm, yalnızca model bileşenine uygulanan bir LoRA (Düşük Dereceli Uyarlama) kancası oluşturur ve CLIP bileşenini tamamen değiştirmez. Belirtilen güçte bir LoRA dosyası yükler ve model üzerinde uygularken CLIP gücünü sıfıra ayarlar. Bu düğüm, önceki kancalarla zincirlenerek karmaşık değişiklik hatları oluşturulmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `lora_adı` | loras klasöründen yüklenecek LoRA dosyasının adı | STRING | Evet | Birden çok seçenek mevcut |
| `model_gücü` | LoRA'nın model bileşenine uygulanması için güç çarpanı (varsayılan: 1.0) | FLOAT | Evet | -20.0 ila 20.0 |
| `önceki_kancalar` | Bu kanca ile zincirlenecek isteğe bağlı önceki kancalar | HOOKS | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `hooks` | Model işlemeye uygulanabilen oluşturulan LoRA kancası | HOOKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/tr.md)

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`
