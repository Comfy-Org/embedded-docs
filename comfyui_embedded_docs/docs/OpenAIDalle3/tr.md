> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/tr.md)

OpenAI'nin DALL·E 3 uç noktası aracılığıyla görüntüleri eşzamanlı olarak oluşturur. Bu düğüm, bir metin istemi alır ve OpenAI'nin DALL·E 3 modelini kullanarak karşılık gelen görüntüleri oluşturur; görüntü kalitesi, stili ve boyutlarını belirtmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | DALL·E için metin istemi (varsayılan: "") |
| `tohum` | INT | Hayır | 0 ile 2147483647 arası | arka uçta henüz uygulanmadı (varsayılan: 0) |
| `kalite` | COMBO | Hayır | "standard"<br>"hd" | Görüntü kalitesi (varsayılan: "standard") |
| `stil` | COMBO | Hayır | "natural"<br>"vivid" | Canlı (Vivid) stil, modelin hiper gerçekçi ve dramatik görüntüler oluşturmaya yönelmesine neden olur. Doğal (Natural) stil ise modelin daha doğal, daha az hiper gerçekçi görünen görüntüler üretmesine neden olur. (varsayılan: "natural") |
| `boyut` | COMBO | Hayır | "1024x1024"<br>"1024x1792"<br>"1792x1024" | Görüntü boyutu (varsayılan: "1024x1024") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | DALL·E 3 tarafından oluşturulan görüntü |