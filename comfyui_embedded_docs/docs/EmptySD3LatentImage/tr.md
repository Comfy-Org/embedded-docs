> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/tr.md)

EmptySD3LatentImage düğümü, Stable Diffusion 3 modelleri için özel olarak biçimlendirilmiş boş bir gizli görüntü tensörü oluşturur. SD3 işlem hatlarının beklediği doğru boyut ve yapıya sahip, sıfırlarla dolu bir tensör üretir. Bu, genellikle görüntü oluşturma iş akışları için bir başlangıç noktası olarak kullanılır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `genişlik` | INT | Evet | 16 ile MAKSİMUM ÇÖZÜNÜRLÜK (adım: 16) | Çıktı gizli görüntüsünün piksel cinsinden genişliği (varsayılan: 1024) |
| `yükseklik` | INT | Evet | 16 ile MAKSİMUM ÇÖZÜNÜRLÜK (adım: 16) | Çıktı gizli görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024) |
| `toplu_boyut` | INT | Evet | 1 ile 4096 | Bir grupta oluşturulacak gizli görüntü sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `LATENT` | LATENT | SD3 uyumlu boyutlara sahip boş örnekler içeren bir gizli tensör. Tensör 16 kanala sahiptir ve giriş genişlik ve yüksekliğine kıyasla 8 kat uzamsal olarak alt örneklenmiştir. |

---
**Source fingerprint (SHA-256):** `21eb5b6385b9b0db95d48fa2f4b85eafe44f865af11ee194945ab7ffe54b6acc`
