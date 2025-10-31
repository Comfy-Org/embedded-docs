> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/tr.md)

Kling Dual Character Video Effect Node, seçilen sahneye dayalı özel efektler içeren videolar oluşturur. İki görüntü alır ve ilk görüntüyü kompozit videonun sol tarafına, ikinci görüntüyü ise sağ tarafına konumlandırır. Seçilen efekt sahnesine bağlı olarak farklı görsel efektler uygulanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image_left` | IMAGE | Evet | - | Sol taraf görüntüsü |
| `image_right` | IMAGE | Evet | - | Sağ taraf görüntüsü |
| `effect_scene` | COMBO | Evet | Birden fazla seçenek mevcut | Video oluşturmaya uygulanacak özel efekt sahnesi türü |
| `model_name` | COMBO | Hayır | Birden fazla seçenek mevcut | Karakter efektleri için kullanılacak model (varsayılan: "kling-v1") |
| `mode` | COMBO | Hayır | Birden fazla seçenek mevcut | Video oluşturma modu (varsayılan: "std") |
| `duration` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan videonun süresi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Çift karakter efektli oluşturulan video |
| `duration` | STRING | Oluşturulan videonun süre bilgisi |