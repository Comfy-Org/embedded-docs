> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/tr.md)

SkipLayerGuidanceSD3 düğümü, atlanan katmanlarla ek bir sınıflandırıcısız yönlendirme seti uygulayarak ayrıntılı yapıya doğru yönlendirmeyi geliştirir. Bu deneysel uygulama, Perturbed Attention Guidance'dan ilham alır ve oluşturulan çıktıdaki yapısal ayrıntıları iyileştirmek için negatif koşullandırma işlemi sırasında belirli katmanları seçici bir şekilde atlayarak çalışır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Atlama katmanı yönlendirmesi uygulanacak model |
| `layers` | STRING | Evet | - | Atlanacak katman indekslerinin virgülle ayrılmış listesi (varsayılan: "7, 8, 9") |
| `scale` | FLOAT | Evet | 0.0 - 10.0 | Atlama katmanı yönlendirme etkisinin gücü (varsayılan: 3.0) |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | Yönlendirme uygulamasının başlangıç noktası, toplam adımların yüzdesi olarak (varsayılan: 0.01) |
| `end_percent` | FLOAT | Evet | 0.0 - 1.0 | Yönlendirme uygulamasının bitiş noktası, toplam adımların yüzdesi olarak (varsayılan: 0.15) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Atlama katmanı yönlendirmesi uygulanmış modifiye edilmiş model |