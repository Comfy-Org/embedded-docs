> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/tr.md)

AlignYourStepsScheduler düğümü, farklı model türlerine göre gürültü giderme işlemi için sigma değerleri üretir. Örnekleme sürecinin her adımı için uygun gürültü seviyelerini hesaplar ve toplam adım sayısını gürültü giderme parametresine göre ayarlar. Bu, örnekleme adımlarının farklı difüzyon modellerinin özel gereksinimleriyle uyumlu hale getirilmesine yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_type` | STRING | Evet | `"SD1"`<br>`"SDXL"`<br>`"SVD"` | Sigma hesaplaması için kullanılacak model türünü belirtir (varsayılan: "SD1") |
| `steps` | INT | Evet | 1 ila 10000 | Oluşturulacak toplam örnekleme adımı sayısı (varsayılan: 10) |
| `denoise` | FLOAT | Evet | 0,0 ila 1,0 | Görüntünün ne kadar gürültüden arındırılacağını kontrol eder; 1,0 tüm adımları kullanırken, daha düşük değerler daha az adım kullanır (varsayılan: 1,0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Gürültü giderme işlemi için hesaplanan sigma değerlerini döndürür |

---
**Source fingerprint (SHA-256):** `112535f9c100ca4e13dcd733e7a371c00c203b38d77bd10beb4355ba3512ec66`
