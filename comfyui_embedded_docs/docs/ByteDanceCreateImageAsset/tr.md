> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/tr.md)

Bu düğüm, ByteDance'in Seedance 2.0 hizmeti için kişisel bir görsel varlığı oluşturur. Bir girdi görselini yükler ve belirtilen bir varlık grubuna kaydeder. Herhangi bir grup kimliği sağlanmazsa, varlığı eklemeden önce tarayıcınızda yeni bir grup oluşturmak için bir gerçek kişi doğrulama süreci başlatır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | | Kişisel varlık olarak kaydedilecek görsel. |
| `group_id` | STRING | Hayır | | Aynı kişi için tekrarlanan insan doğrulamasını atlamak için mevcut bir Seedance varlık grubu kimliğini yeniden kullanın. Tarayıcıda gerçek kişi doğrulaması çalıştırmak ve yeni bir grup oluşturmak için boş bırakın (varsayılan: boş). |

**Görsel Kısıtlamaları:**
*   Görsel genişliği 300 ile 6000 piksel arasında olmalıdır.
*   Görsel yüksekliği 300 ile 6000 piksel arasında olmalıdır.
*   Görsel en-boy oranı 0,4:1 ile 2,5:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `asset_id` | STRING | Yeni oluşturulan görsel varlığı için benzersiz tanımlayıcı. |
| `group_id` | STRING | Varlık grubu için tanımlayıcı. Bu, sağlanan `group_id` veya yeni oluşturulan bir kimlik olacaktır. |

---
**Source fingerprint (SHA-256):** `b8b7b4cbbc16a8bb0102982757496ad4e8140bd87155902668c0be0d8b4d3d98`
