> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/tr.md)

LatentCut düğümü, gizli örneklerden seçilen bir boyut boyunca belirli bir bölümü çıkarır. x, y veya t boyutunu, başlangıç konumunu ve çıkarılacak miktarı belirterek gizli temsilin bir kısmını kesmenizi sağlar. Düğüm, hem pozitif hem de negatif indekslemeyi işler ve çıkarma miktarını mevcut sınırlar içinde kalacak şekilde otomatik olarak ayarlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Evet | - | Çıkarım yapılacak giriş gizli örnekleri |
| `dim` | COMBO | Evet | "x"<br>"y"<br>"t" | Gizli örneklerin hangi boyut boyunca kesileceği |
| `index` | INT | Evet | -16384 ila 16384 | Kesme işlemi için başlangıç konumu (varsayılan: 0). Pozitif değerler baştan, negatif değerler sondan sayar. Düğüm, indeksi gizli örneklerin geçerli aralığında kalacak şekilde otomatik olarak sınırlar |
| `amount` | INT | Evet | 1 ila 16384 | Belirtilen boyut boyunca çıkarılacak öğe sayısı (varsayılan: 1). Düğüm, bu değer başlangıç indeksinin ötesindeki mevcut veriyi aşarsa otomatik olarak azaltır |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Gizli örneklerin çıkarılan bölümü |

---
**Source fingerprint (SHA-256):** `54f2b0cead9dce2c2cbd241d4e8c50ce85a67d3e1a40e7002056b83acbf0cf2d`
