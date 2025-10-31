> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/tr.md)

Görüntüleri eşzamanlı olarak prompt ve en-boy oranına dayalı şekilde değiştirir. Bu düğüm, bir giriş görüntüsünü alır ve orijinal görüntünün en-boy oranını koruyarak sağlanan metin prompt'una göre dönüştürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Değiştirilecek giriş görüntüsü |
| `istem` | STRING | Evet | - | Görüntü oluşturma için prompt (varsayılan: "") |
| `görüntü_ağırlığı` | FLOAT | Hayır | 0.0-0.98 | Görüntünün ağırlığı; 1.0'a ne kadar yakınsa, görüntü o kadar az değiştirilir (varsayılan: 0.1) |
| `model` | MODEL | Evet | Birden fazla seçenek mevcut | Görüntü değişikliği için kullanılacak Luma modeli |
| `tohum` | INT | Hayır | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed; gerçek sonuçlar seed'den bağımsız olarak belirsizdir (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Luma modeli tarafından oluşturulan değiştirilmiş görüntü |