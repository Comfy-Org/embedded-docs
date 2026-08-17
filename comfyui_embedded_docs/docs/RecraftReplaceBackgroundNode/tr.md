# Recraft Arka Planı Değiştir

Görüntüdeki arka planı, sağlanan isteme göre değiştirin. Bu düğüm, görüntüleriniz için metin açıklamanıza göre yeni arka planlar oluşturmak üzere Recraft API'sini kullanır; ana öğeyi bozulmadan koruyarak arka planı tamamen dönüştürmenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | İşlenecek giriş görüntüsü | IMAGE | Evet | - |
| `prompt` | Görüntü üretimi için istem (varsayılan: boş) | STRING | Evet | - |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1) | INT | Evet | 1-6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_style` | Üretilen arka plan için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak "realistic_image" stilini kullanır | STYLEV3 | Hayır | - |
| `negative_prompt` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş) | STRING | Hayır | - |

**Not:** `seed` parametresi, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; ancak harici API'nin doğası gereği deterministik sonuçları garanti etmez.

**Not:** Giriş kümesindeki her görüntü ayrı ayrı işlenir; düğüm, her giriş görüntüsü için arka planı değiştirilmiş `n` adet görüntü döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Arka planı değiştirilmiş üretilen görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
