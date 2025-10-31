> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/tr.md)

AlignYourStepsScheduler düğümü, farklı model türlerine dayalı olarak gürültü giderme işlemi için sigma değerleri üretir. Örnekleme işleminin her adımı için uygun gürültü seviyelerini hesaplar ve toplam adım sayısını gürültü giderme parametresine göre ayarlar. Bu, örnekleme adımlarının farklı yayılım modellerinin özel gereksinimleriyle uyumlu hale getirilmesine yardımcı olur.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model_type` | STRING | COMBO | - | SD1, SDXL, SVD | Sigma hesaplamasında kullanılacak model türünü belirtir |
| `steps` | INT | INT | 10 | 1-10000 | Üretilecek toplam örnekleme adımı sayısı |
| `denoise` | FLOAT | FLOAT | 1.0 | 0.0-1.0 | Görüntünün ne kadar gürültüsünün giderileceğini kontrol eder; 1.0 tüm adımları kullanır, daha düşük değerler daha az adım kullanır |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Gürültü giderme işlemi için hesaplanan sigma değerlerini döndürür |