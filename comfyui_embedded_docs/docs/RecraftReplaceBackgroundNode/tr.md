# Recraft Arka Planı Değiştir

Sağlanan isteme dayalı olarak görüntüdeki arka planı değiştirir. Bu düğüm, Recraft API'sini kullanarak metin açıklamanıza göre görüntüleriniz için yeni arka planlar üretir; ana nesneyi korurken arka planı tamamen dönüştürmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | İşlenecek girdi görüntüsü | IMAGE | Evet | - |
| `istem` | Görüntü üretimi için istem (varsayılan: boş) | STRING | Evet | - |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1) | INT | Evet | 1-6 |
| `tohum` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Üretilen arka plan için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak "realistic_image" stilini kullanır | STYLEV3 | Hayır | - |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş) | STRING | Hayır | - |

**Not:** `seed` parametresi düğümün ne zaman yeniden çalışacağını kontrol eder ancak harici API'nin doğası gereği deterministik sonuçlar garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `IMAGE` | Değiştirilmiş arka plana sahip üretilen görüntü(ler). Her girdi görüntüsü için üretilen sonuç sayısı `n` tarafından belirlenir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
