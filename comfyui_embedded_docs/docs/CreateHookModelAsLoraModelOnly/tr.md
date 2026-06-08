Bu düğüm, bir sinir ağının yalnızca model bileşenini değiştirmek için bir LoRA (Düşük Dereceli Uyarlama) modeli uygulayan bir kanca oluşturur. CLIP bileşenini değiştirmeden, belirtilen güçte bir kontrol noktası dosyasını yükler ve modele uygular. Bu düğüm, temel CreateHookModelAsLora sınıfının işlevselliğini genişleten deneysel bir düğümdür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ckpt_adı` | LoRA modeli olarak yüklenecek kontrol noktası dosyası. Mevcut seçenekler, kontrol noktaları klasörünün içeriğine bağlıdır. | STRING | Evet | Birden çok seçenek mevcut |
| `model_gücü` | LoRA'nın model bileşenine uygulanması için güç çarpanı (varsayılan: 1,0) | FLOAT | Evet | -20,0 ila 20,0 |
| `önceki_kancalar` | Bu kanca ile zincirlenecek isteğe bağlı önceki kancalar | HOOKS | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `hooks` | LoRA model değişikliğini içeren oluşturulan kanca grubu | HOOKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/tr.md)

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
