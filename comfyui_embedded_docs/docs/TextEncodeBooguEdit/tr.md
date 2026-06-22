# TextEncodeBooguEdit

Bu düğüm, Boogu ile görüntü düzenleme için koşullandırmayı (conditioning) hazırlar. Düzenleme talimatını güçlendirmek için referans görüntüden alınan görsel belirteçler (vision tokens) yalnızca pozitif koşullandırmaya eklenirken; CFG altında birbirini gidermesi ve orijinal görüntü kimliğini koruması amacıyla bir VAE referans gizli değişkeni (latent) hem pozitif hem de negatif koşullandırmaya eklenir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Metin kodlama için kullanılan CLIP modeli | CLIP | Evet | |
| `prompt` | İstenen düzenlemeyi tanımlayan metin istemi | STRING | Evet | |
| `negative_prompt` | Düzenlemede kaçınılması gerekenleri tanımlayan metin istemi | STRING | Hayır | |
| `vae` | Referans görüntüleri gizli uzaya (latent space) kodlamak için kullanılan VAE modeli | VAE | Hayır | |
| `images` | Düzenlenecek referans görüntü(ler). Boogu, örnek başına bir referansa odaklanır; daha fazlasına izin verilir. | IMAGE | Hayır | En fazla 16 görüntü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `negative` | Görsel belirteçlerle birlikte metin istemini ve referans gizli değişkenlerini içeren koşullandırma | CONDITIONING |
| `negative` | Negatif metin istemini ve referans gizli değişkenlerini içeren koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/tr.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
