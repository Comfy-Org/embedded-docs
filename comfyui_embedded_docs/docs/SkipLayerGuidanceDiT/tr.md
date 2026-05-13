> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/tr.md)

İşte SkipLayerGuidanceDiT düğümü için Türkçe teknik belge çevirisi:

## Genel Bakış

Atlanmış katmanlara sahip başka bir CFG negatif seti kullanarak ayrıntılı yapıya yönelik yönlendirmeyi geliştirir. SkipLayerGuidance'ın bu genel sürümü, her DiT modelinde kullanılabilir ve Perturbed Attention Guidance'dan ilham alınmıştır. Orijinal deneysel uygulama SD3 için oluşturulmuştur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Katman atlama yönlendirmesinin uygulanacağı model |
| `double_layers` | STRING | Evet | - | Atlanacak çift bloklar için virgülle ayrılmış katman numaraları (varsayılan: "7, 8, 9") |
| `single_layers` | STRING | Evet | - | Atlanacak tek bloklar için virgülle ayrılmış katman numaraları (varsayılan: "7, 8, 9") |
| `scale` | FLOAT | Evet | 0,0 - 10,0 | Yönlendirme ölçek faktörü (varsayılan: 3,0) |
| `start_percent` | FLOAT | Evet | 0,0 - 1,0 | Yönlendirme uygulaması için başlangıç yüzdesi (varsayılan: 0,01) |
| `end_percent` | FLOAT | Evet | 0,0 - 1,0 | Yönlendirme uygulaması için bitiş yüzdesi (varsayılan: 0,15) |
| `rescaling_scale` | FLOAT | Evet | 0,0 - 10,0 | Çıktı büyüklüğünü ayarlamak için yeniden ölçeklendirme faktörü (varsayılan: 0,0, yeniden ölçeklendirme yapılmaz) |

**Not:** Hem `double_layers` hem de `single_layers` boşsa (hiçbir katman numarası içermiyorsa), düğüm herhangi bir yönlendirme uygulamadan orijinal modeli döndürür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Katman atlama yönlendirmesi uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `cf494fbeb33e7bc3b3f798e9e9b025623afad4ea6340ef628caa776c7d42ba12`
