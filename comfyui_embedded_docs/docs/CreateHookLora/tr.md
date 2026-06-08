ComfyUI Düğüm Belgeleri - Create Hook LoRA

Create Hook LoRA düğümü, modellere LoRA (Düşük Dereceli Uyarlama) değişiklikleri uygulamak için kanca nesneleri oluşturur. Belirtilen bir LoRA dosyasını yükler ve model ile CLIP güçlerini ayarlayabilen kancalar oluşturur, ardından bu kancaları kendisine iletilen mevcut kancalarla birleştirir. Düğüm, daha önce yüklenen LoRA dosyalarını önbelleğe alarak gereksiz işlemleri önler ve LoRA yüklemeyi verimli bir şekilde yönetir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `lora_adı` | loras dizininden yüklenecek LoRA dosyasının adı | STRING | Evet | Birden çok seçenek mevcut |
| `model_gücü` | Model ayarlamaları için güç çarpanı (varsayılan: 1,0) | FLOAT | Evet | -20,0 ile 20,0 arası |
| `clip_gücü` | CLIP ayarlamaları için güç çarpanı (varsayılan: 1,0) | FLOAT | Evet | -20,0 ile 20,0 arası |
| `önceki_kancalar` | Yeni LoRA kancalarıyla birleştirilecek isteğe bağlı mevcut kanca grubu | HOOKS | Hayır | Yok |

**Parametre Kısıtlamaları:**

- Hem `strength_model` hem de `strength_clip` 0 olarak ayarlanırsa, düğüm yeni LoRA kancaları oluşturmayı atlar ve mevcut kancaları değiştirmeden döndürür
- Düğüm, aynı LoRA tekrar tekrar kullanıldığında performansı optimize etmek için en son yüklenen LoRA dosyasını önbelleğe alır

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `HOOKS` | Birleştirilmiş LoRA kancalarını ve önceki kancaları içeren bir kanca grubu | HOOKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/tr.md)

---
**Source fingerprint (SHA-256):** `42d5d776bfc9b239191952e2bce23513d183f904fc3c15039469381a547486f8`
