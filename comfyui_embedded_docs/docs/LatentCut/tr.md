> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/tr.md)

LatentCut düğümü, gizli örneklerden belirli bir boyut boyunca bir bölüm çıkarır. Boyut (x, y veya t), başlangıç pozisyonu ve çıkarılacak miktarı belirterek gizli temsilden bir parça kesip almanıza olanak tanır. Düğüm hem pozitif hem de negatif indekslemeyi işler ve çıkarım miktarını mevcut sınırlar içinde kalacak şekilde otomatik olarak ayarlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Evet | - | Çıkarım yapılacak giriş gizli örnekleri |
| `dim` | COMBO | Evet | "x"<br>"y"<br>"t" | Gizli örneklerin kesileceği boyut |
| `index` | INT | Hayır | -16384 - 16384 | Kesimin başlayacağı pozisyon (varsayılan: 0). Pozitif değerler baştan, negatif değerler sondan sayar |
| `amount` | INT | Hayır | 1 - 16384 | Belirtilen boyut boyunca çıkarılacak eleman sayısı (varsayılan: 1) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Gizli örneklerden çıkarılan bölüm |