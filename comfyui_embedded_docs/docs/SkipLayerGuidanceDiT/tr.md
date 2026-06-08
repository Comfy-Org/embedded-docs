İşte SkipLayerGuidanceDiT düğümü için Türkçe teknik belge çevirisi:

## Genel Bakış

Atlanmış katmanlara sahip başka bir CFG negatif seti kullanarak ayrıntılı yapıya yönelik yönlendirmeyi geliştirir. SkipLayerGuidance'ın bu genel sürümü, her DiT modelinde kullanılabilir ve Perturbed Attention Guidance'dan ilham alınmıştır. Orijinal deneysel uygulama SD3 için oluşturulmuştur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Katman atlama yönlendirmesinin uygulanacağı model | MODEL | Evet | - |
| `çift_katmanlar` | Atlanacak çift bloklar için virgülle ayrılmış katman numaraları (varsayılan: "7, 8, 9") | STRING | Evet | - |
| `tek_katmanlar` | Atlanacak tek bloklar için virgülle ayrılmış katman numaraları (varsayılan: "7, 8, 9") | STRING | Evet | - |
| `ölçek` | Yönlendirme ölçek faktörü (varsayılan: 3,0) | FLOAT | Evet | 0,0 - 10,0 |
| `başlangıç_yüzdesi` | Yönlendirme uygulaması için başlangıç yüzdesi (varsayılan: 0,01) | FLOAT | Evet | 0,0 - 1,0 |
| `bitiş_yüzdesi` | Yönlendirme uygulaması için bitiş yüzdesi (varsayılan: 0,15) | FLOAT | Evet | 0,0 - 1,0 |
| `yeniden_ölçeklendirme_ölçeği` | Çıktı büyüklüğünü ayarlamak için yeniden ölçeklendirme faktörü (varsayılan: 0,0, yeniden ölçeklendirme yapılmaz) | FLOAT | Evet | 0,0 - 10,0 |

**Not:** Hem `double_layers` hem de `single_layers` boşsa (hiçbir katman numarası içermiyorsa), düğüm herhangi bir yönlendirme uygulamadan orijinal modeli döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Katman atlama yönlendirmesi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/tr.md)

---
**Source fingerprint (SHA-256):** `cf494fbeb33e7bc3b3f798e9e9b025623afad4ea6340ef628caa776c7d42ba12`
