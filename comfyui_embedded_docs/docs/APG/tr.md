> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/tr.md)

APG (Uyarlanabilir Yansıtılmış Kılavuzluk) düğümü, yayılım sürecinde kılavuzluğun nasıl uygulandığını ayarlayarak örnekleme işlemini değiştirir. Kılavuzluk vektörünü, koşullu çıktıya göre paralel ve dik bileşenler olarak ayırarak daha kontrollü görüntü oluşturmayı sağlar. Düğüm, kılavuzluğun ölçeğini ayarlamak, büyüklüğünü normalize etmek ve yayılım adımları arasında daha pürüzsüz geçişler için momentum uygulamak üzere parametreler sağlar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Gerekli | - | - | Uyarlanabilir yansıtılmış kılavuzluğun uygulanacağı yayılım modeli |
| `eta` | FLOAT | Gerekli | 1.0 | -10.0 - 10.0 | Paralel kılavuzluk vektörünün ölçeğini kontrol eder. 1 değerinde varsayılan CFG davranışı sağlanır. |
| `norm_threshold` | FLOAT | Gerekli | 5.0 | 0.0 - 50.0 | Kılavuzluk vektörünü bu değere normalize eder. 0 değerinde normalizasyon devre dışı bırakılır. |
| `momentum` | FLOAT | Gerekli | 0.0 | -5.0 - 1.0 | Yayılım sırasında kılavuzluğun kayan ortalamasını kontrol eder. 0 değerinde devre dışı bırakılır. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Örnekleme işlemine uyarlanabilir yansıtılmış kılavuzluk uygulanmış olarak değiştirilmiş modeli döndürür |