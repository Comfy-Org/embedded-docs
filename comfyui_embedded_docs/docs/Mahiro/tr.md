> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/tr.md)

Mahiro düğümü, pozitif ve negatif yönlendirmeler arasındaki farktan ziyade pozitif yönlendirmenin yönüne daha fazla odaklanmak için yönlendirme işlevini değiştirir. Normalize edilmiş koşullu ve koşulsuz gürültü giderme çıktıları arasındaki kosinüs benzerliğini kullanarak özel bir yönlendirme ölçekleme yaklaşımı uygulayan yamalı bir model oluşturur. Bu deneysel düğüm, üretimi pozitif yönlendirmenin amaçlanan yönüne daha güçlü bir şekilde yönlendirmeye yardımcı olur.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | | Değiştirilmiş yönlendirme işleviyle yamalanacak model |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Mahiro yönlendirme işlevi uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `8b4a73cfa488f97d87e5a18d5ab30765055b5d5a66c6c2f1a5f016eed2af0300`
