> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/tr.md)

Self-Attention Guidance düğümü, örnekleme süreci boyunca dikkat mekanizmasını değiştirerek yayılım modellerine kılavuzluk uygular. Koşulsuz gürültü giderme adımlarından dikkat skorlarını yakalar ve bunları nihai çıktıyı etkileyen bulanık kılavuzluk haritaları oluşturmak için kullanır. Bu teknik, modelin kendi dikkat kalıplarından yararlanarak oluşturma sürecine rehberlik etmeye yardımcı olur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Self-attention guidance uygulanacak yayılım modeli |
| `scale` | FLOAT | Hayır | -2.0 - 5.0 | Self-attention guidance etkisinin gücü (varsayılan: 0.5) |
| `blur_sigma` | FLOAT | Hayır | 0.0 - 10.0 | Kılavuzluk haritasını oluşturmak için uygulanan bulanıklık miktarı (varsayılan: 2.0) |

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Self-attention guidance uygulanmış modifiye edilmiş model |

**Not:** Bu düğüm şu anda deneysel aşamadadır ve parçalı gruplar (chunked batches) ile sınırlamalara sahiptir. Yalnızca bir UNet çağrısından dikkat skorlarını kaydedebilir ve daha büyük grup boyutlarıyla (batch sizes) düzgün çalışmayabilir.