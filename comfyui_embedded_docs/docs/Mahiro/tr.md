> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/tr.md)

Mahiro düğümü, kılavuzlama işlevini, pozitif ve negatif prompt'lar arasındaki farktan ziyade pozitif prompt'un yönüne daha fazla odaklanacak şekilde değiştirir. Normalleştirilmiş koşullu ve koşulsuz gürültüsüz çıktılar arasındaki kosinüs benzerliğini kullanarak özel bir kılavuzlama ölçeklendirme yaklaşımı uygulayan yamalı bir model oluşturur. Bu deneysel düğüm, üretimi pozitif prompt'un amaçlanan yönüne daha güçlü bir şekilde yönlendirmeye yardımcı olur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | | Değiştirilmiş kılavuzlama işlevi ile yamalanacak model |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Mahiro kılavuzlama işlevi uygulanmış değiştirilmiş model |