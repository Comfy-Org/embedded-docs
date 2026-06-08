OpenAI'nin DALL·E 3 uç noktası üzerinden eşzamanlı olarak görseller oluşturur. Bu düğüm, bir metin istemi alır ve OpenAI'nin DALL·E 3 modelini kullanarak karşılık gelen görselleri oluşturur; görsel kalitesini, stilini ve boyutlarını belirlemenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | DALL·E için metin istemi (varsayılan: "") | STRING | Evet | - |
| `tohum` | Henüz arka uçta uygulanmadı (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |
| `kalite` | Görsel kalitesi (varsayılan: "standard") | COMBO | Hayır | "standard"<br>"hd" |
| `stil` | Canlı (vivid), modelin hiper-gerçekçi ve dramatik görsellere yönelmesine neden olur. Doğal (natural), modelin daha doğal, daha az hiper-gerçekçi görünümlü görseller üretmesini sağlar. (varsayılan: "natural") | COMBO | Hayır | "natural"<br>"vivid" |
| `boyut` | Görsel boyutu (varsayılan: "1024x1024") | COMBO | Hayır | "1024x1024"<br>"1024x1792"<br>"1792x1024" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | DALL·E 3'ten oluşturulan görsel | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/tr.md)

---
**Source fingerprint (SHA-256):** `e36bfe2a6ecec050906f220de3a3edf06eff0bfd6e21f08ce90579172a07d7eb`
