> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/tr.md)

SkipLayerGuidanceSD3 düğümü, atlanmış katmanlarla ek bir sınıflandırıcısız yönlendirme seti uygulayarak, ayrıntılı yapıya yönelik yönlendirmeyi geliştirir. Bu deneysel uygulama, Perturbed Attention Guidance'dan ilham alınmıştır ve negatif koşullandırma sürecinde belirli katmanları seçici olarak atlayarak, oluşturulan çıktıdaki yapısal detayları iyileştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Katman atlama yönlendirmesinin uygulanacağı model |
| `layers` | STRING | Evet | - | Atlanacak katman indekslerinin virgülle ayrılmış listesi (varsayılan: "7, 8, 9") |
| `scale` | FLOAT | Evet | 0.0 - 10.0 | Katman atlama yönlendirme etkisinin gücü (varsayılan: 3.0) |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | Yönlendirme uygulamasının başlangıç noktası, toplam adımların yüzdesi olarak (varsayılan: 0.01) |
| `end_percent` | FLOAT | Evet | 0.0 - 1.0 | Yönlendirme uygulamasının bitiş noktası, toplam adımların yüzdesi olarak (varsayılan: 0.15) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Katman atlama yönlendirmesi uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `97c8220abd223bd35b4d0274c2b4536ffb6be7954ccd917943905bd22f60c1a5`
