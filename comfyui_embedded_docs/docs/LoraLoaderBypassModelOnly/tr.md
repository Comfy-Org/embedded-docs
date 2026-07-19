# LoRA Yükle (Bypass, Sadece Model) (Hata Ayıklama İçin)

Bu düğüm, bir modelin davranışını değiştirmek için bir LoRA (Düşük Dereceli Uyarlama) uygular, ancak yalnızca model bileşeninin kendisini etkiler. Belirtilen bir LoRA dosyasını yükler ve modelin ağırlıklarını belirli bir güçle ayarlar; CLIP metin kodlayıcı gibi diğer bileşenleri değiştirmez.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA ayarlamalarının uygulanacağı temel model. | MODEL | Evet | - |
| `lora_name` | Yüklenecek ve uygulanacak LoRA dosyasının adı. Seçenekler, `loras` dizinindeki dosyalardan doldurulur. | STRING | Evet | (Mevcut LoRA dosyalarının listesi) |
| `strength_model` | LoRA'nın model ağırlıkları üzerindeki etkisinin gücü. Pozitif bir değer LoRA'yı uygular, negatif bir değer tersini uygular ve 0 değerinin hiçbir etkisi yoktur (varsayılan: 1,0). | FLOAT | Evet | -100,0 ila 100,0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Ağırlıklarına LoRA ayarlamaları uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/tr.md)

---
**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`
