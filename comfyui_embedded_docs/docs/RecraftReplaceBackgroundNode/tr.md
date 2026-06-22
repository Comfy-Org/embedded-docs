# Recraft Arka Planı Değiştir

Verilen bilgiye göre, bir önceki mesajda belirtilen çeviri kurallarına uygun olarak belgeyi Türkçeye çeviriyorum.

Görüntünün arka planını, sağlanan isteme göre değiştirin. Bu düğüm, görüntüleriniz için metin açıklamanıza uygun yeni arka planlar oluşturmak üzere Recraft API'sini kullanarak ana konuyu korurken arka planı tamamen dönüştürmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | İşlenecek giriş görüntüsü | IMAGE | Evet | - |
| `istem` | Görüntü oluşturma için istem (varsayılan: boş) | STRING | Evet | - |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1) | INT | Evet | 1-6 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Oluşturulan arka plan için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak "realistic_image" stili kullanılır | STYLEV3 | Hayır | - |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş) | STRING | Hayır | - |

**Not:** `seed` parametresi düğümün ne zaman yeniden yürütüleceğini kontrol eder ancak harici API'nin doğası gereği deterministik sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Arka planı değiştirilmiş oluşturulan görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `305cb8c542159a089b1fa03971205b23d50c8a328af006e284fb27011070f6bd`
