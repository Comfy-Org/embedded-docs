> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/tr.md)

Bu düğüm, bir sinir ağının yalnızca model bileşenini değiştirmek için bir LoRA (Düşük Dereceli Uyarlama) modeli uygulayan bir kanca oluşturur. CLIP bileşenini değiştirmeden, belirtilen güçte bir kontrol noktası dosyasını yükler ve modele uygular. Bu düğüm, temel CreateHookModelAsLora sınıfının işlevselliğini genişleten deneysel bir düğümdür.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `ckpt_name` | STRING | Evet | Birden çok seçenek mevcut | LoRA modeli olarak yüklenecek kontrol noktası dosyası. Mevcut seçenekler, kontrol noktaları klasörünün içeriğine bağlıdır. |
| `strength_model` | FLOAT | Evet | -20,0 ila 20,0 | LoRA'nın model bileşenine uygulanması için güç çarpanı (varsayılan: 1,0) |
| `prev_hooks` | HOOKS | Hayır | - | Bu kanca ile zincirlenecek isteğe bağlı önceki kancalar |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `hooks` | HOOKS | LoRA model değişikliğini içeren oluşturulan kanca grubu |

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
