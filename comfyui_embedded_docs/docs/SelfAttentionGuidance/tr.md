Self-Attention Guidance düğümü, örnekleme işlemi sırasında dikkat mekanizmasını değiştirerek difüzyon modellerine yönlendirme uygular. Koşulsuz gürültü giderme adımlarından dikkat puanlarını yakalar ve bunları, nihai çıktıyı etkileyen bulanık yönlendirme haritaları oluşturmak için kullanır. Bu teknik, modelin kendi dikkat kalıplarından yararlanarak üretim sürecini yönlendirmeye yardımcı olur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kendi kendine dikkat yönlendirmesinin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `ölçek` | Kendi kendine dikkat yönlendirme etkisinin gücü (varsayılan: 0,5) | FLOAT | Hayır | -2,0 ila 5,0 |
| `bulanıklık_sigma` | Yönlendirme haritasını oluşturmak için uygulanan bulanıklık miktarı (varsayılan: 2,0) | FLOAT | Hayır | 0,0 ila 10,0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kendi kendine dikkat yönlendirmesi uygulanmış değiştirilmiş model | MODEL |

**Not:** Bu düğüm şu anda deneyseldir ve parçalı gruplarla sınırlamaları vardır. Yalnızca bir UNet çağrısından dikkat puanlarını kaydedebilir ve daha büyük grup boyutlarıyla düzgün çalışmayabilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `5f16ecd8f74bfd71073c6e3a65be08e54e4f5b9c56fe08deb48f35df381e82fa`
