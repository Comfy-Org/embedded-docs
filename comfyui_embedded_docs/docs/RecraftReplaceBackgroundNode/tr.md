> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/tr.md)

Verilen bilgiye göre, bir önceki mesajda belirtilen çeviri kurallarına uygun olarak belgeyi Türkçeye çeviriyorum.

Görüntünün arka planını, sağlanan isteme göre değiştirin. Bu düğüm, görüntüleriniz için metin açıklamanıza uygun yeni arka planlar oluşturmak üzere Recraft API'sini kullanarak ana konuyu korurken arka planı tamamen dönüştürmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | İşlenecek giriş görüntüsü |
| `prompt` | STRING | Evet | - | Görüntü oluşturma için istem (varsayılan: boş) |
| `n` | INT | Evet | 1-6 | Oluşturulacak görüntü sayısı (varsayılan: 1) |
| `seed` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0) |
| `recraft_style` | STYLEV3 | Hayır | - | Oluşturulan arka plan için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak "realistic_image" stili kullanılır |
| `negative_prompt` | STRING | Hayır | - | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş) |

**Not:** `seed` parametresi düğümün ne zaman yeniden yürütüleceğini kontrol eder ancak harici API'nin doğası gereği deterministik sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Arka planı değiştirilmiş oluşturulan görüntü(ler) |

---
**Source fingerprint (SHA-256):** `305cb8c542159a089b1fa03971205b23d50c8a328af006e284fb27011070f6bd`
