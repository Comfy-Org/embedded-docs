# Koşullandırmayı Kaydet

Bu düğüm, tek bir conditioning'i çıktı klasörüne safetensors dosyası olarak kaydeder. Kaydedilen dosya models/embeddings klasörüne taşınabilir ve daha sonra Load Conditioning ile yüklenebilir; örneğin metin kodlayıcıyı atlamak için. Düğüm, conditioning'i değiştirmeden geçirir; böylece iş akışında daha sonra hâlâ kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Kaydedilecek conditioning. Yalnızca tek bir conditioning kaydı desteklenir. | CONDITIONING | Evet | - |
| `filename_prefix` | Çıktı dosya adını oluşturmak için kullanılan önek. Dosya, sonuna sayısal bir sayaç eklenerek çıktı klasörüne yazılır. Varsayılan: `conditioning/ComfyUI` | STRING | Evet | - |

**Notlar:**

- `conditioning` girdisi birden fazla kayıt içeriyorsa (örneğin conditioning'ler birleştirildikten sonra), düğüm şu hatayı verir: "Save Conditioning supports a single conditioning entry, save it before combining."
- Tensor, tensor listesi/demeti, boolean, tamsayı, ondalık sayı veya dize olan conditioning seçenekleri conditioning ile birlikte kaydedilir. `None` olan seçenekler atlanır. Bunların dışındaki herhangi bir seçenek türü, seçeneğin kaydedilemeyeceğini belirten bir hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `conditioning` | İçeri verilen conditioning'in aynısı, değiştirilmeden. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`
