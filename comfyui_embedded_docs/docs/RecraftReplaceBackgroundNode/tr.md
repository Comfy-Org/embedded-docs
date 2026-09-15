# Recraft Arka Planı Değiştir

Bir görselin arka planını, sağlanan istem temelinde değiştirir. Bu düğüm, metin açıklamanıza göre görselleriniz için yeni arka planlar oluşturmak üzere Recraft API'sini kullanır; ana konuyu bozmadan arka planı tamamen dönüştürmenizi sağlar. Girdi grubundaki her görsel ayrı ayrı işlenir ve sonuçlar tek bir çıktı grubunda birleştirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | İşlenecek girdi görseli | IMAGE | Evet | - |
| `istem` | Görsel oluşturma için istem (varsayılan: boş) | STRING | Evet | - |
| `n` | Oluşturulacak görsel sayısı (varsayılan: 1) | INT | Evet | 1-6 |
| `tohum` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Oluşturulan arka plan için isteğe bağlı stil seçimi. Sağlanmazsa varsayılan olarak "realistic_image" stiline geçer | STYLEV3 | Hayır | - |
| `negatif_istem` | Bir görselde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş) | STRING | Hayır | - |

**Notlar:**
- `seed` parametresi düğümün ne zaman yeniden yürütüleceğini kontrol eder ancak harici API'nin doğası gereği deterministik sonuçları garanti etmez.
- `recraft_style` bağlı olmadığında veya boş bırakıldığında, düğüm `realistic_image` stiline geri döner.
- `negative_prompt` boş bırakıldığında, istekle birlikte gönderilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Arka planı değiştirilmiş oluşturulan görsel(ler). Her girdi görseli için oluşturulan sonuç sayısı `n` tarafından belirlenir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
