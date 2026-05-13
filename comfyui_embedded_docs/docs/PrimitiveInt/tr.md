> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/tr.md)

PrimitiveInt düğümü, iş akışınızda tam sayı değerleriyle çalışmak için basit bir yol sağlar. Bir tam sayı girişi alır ve aynı değeri çıktı olarak verir; bu sayede düğümler arasında tam sayı parametreleri iletmek veya diğer işlemler için belirli sayısal değerler ayarlamak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `değer` | INT | Evet | -9223372036854775807 ile 9223372036854775807 arası | Çıktı olarak verilecek tam sayı değeri (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | INT | Giriş tam sayı değeri, değiştirilmeden iletilir |

---
**Source fingerprint (SHA-256):** `13b5ff6703498fd37ae48d574e010cf78aa2bfc514b68c34b2cf6740ed75c834`
