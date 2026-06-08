SkipLayerGuidanceSD3 düğümü, atlanmış katmanlarla ek bir sınıflandırıcısız yönlendirme seti uygulayarak, ayrıntılı yapıya yönelik yönlendirmeyi geliştirir. Bu deneysel uygulama, Perturbed Attention Guidance'dan ilham alınmıştır ve negatif koşullandırma sürecinde belirli katmanları seçici olarak atlayarak, oluşturulan çıktıdaki yapısal detayları iyileştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Katman atlama yönlendirmesinin uygulanacağı model | MODEL | Evet | - |
| `katmanlar` | Atlanacak katman indekslerinin virgülle ayrılmış listesi (varsayılan: "7, 8, 9") | STRING | Evet | - |
| `ölçek` | Katman atlama yönlendirme etkisinin gücü (varsayılan: 3.0) | FLOAT | Evet | 0.0 - 10.0 |
| `başlangıç_yüzdesi` | Yönlendirme uygulamasının başlangıç noktası, toplam adımların yüzdesi olarak (varsayılan: 0.01) | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_yüzdesi` | Yönlendirme uygulamasının bitiş noktası, toplam adımların yüzdesi olarak (varsayılan: 0.15) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Katman atlama yönlendirmesi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/tr.md)

---
**Source fingerprint (SHA-256):** `97c8220abd223bd35b4d0274c2b4536ffb6be7954ccd917943905bd22f60c1a5`
