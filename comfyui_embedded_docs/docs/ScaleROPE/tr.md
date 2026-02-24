> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/tr.md)

ScaleROPE düğümü, bir modelin Döner Konum Yerleştirmesinin (ROPE) X, Y ve T (zaman) bileşenlerine ayrı ölçeklendirme ve kaydırma faktörleri uygulayarak değiştirmenize olanak tanır. Bu, modelin konumsal kodlama davranışını ayarlamak için kullanılan gelişmiş, deneysel bir düğümdür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | ROPE parametreleri değiştirilecek model. |
| `scale_x` | FLOAT | Hayır | 0.0 - 100.0 | ROPE'nin X bileşenine uygulanacak ölçeklendirme faktörü (varsayılan: 1.0). |
| `shift_x` | FLOAT | Hayır | -256.0 - 256.0 | ROPE'nin X bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). |
| `scale_y` | FLOAT | Hayır | 0.0 - 100.0 | ROPE'nin Y bileşenine uygulanacak ölçeklendirme faktörü (varsayılan: 1.0). |
| `shift_y` | FLOAT | Hayır | -256.0 - 256.0 | ROPE'nin Y bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). |
| `scale_t` | FLOAT | Hayır | 0.0 - 100.0 | ROPE'nin T (zaman) bileşenine uygulanacak ölçeklendirme faktörü (varsayılan: 1.0). |
| `shift_t` | FLOAT | Hayır | -256.0 - 256.0 | ROPE'nin T (zaman) bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Yeni ROPE ölçeklendirme ve kaydırma parametreleri uygulanmış model. |
