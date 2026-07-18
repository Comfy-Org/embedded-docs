Bu düğüm, Seedance 2.0 için kişisel bir video varlığı oluşturur. Giriş videonuzu yükler ve belirtilen bir varlık grubuna kaydeder. Bir grup kimliği sağlamazsanız, önce yeni bir grup oluşturmak için tarayıcınızda bir gerçek kişi doğrulama sürecinden geçmenizi sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kişisel varlık olarak kaydedilecek video. | VIDEO | Evet | - |
| `group_id` | Aynı kişi için tekrarlanan insan doğrulamasını atlamak amacıyla mevcut bir Seedance varlık grubu kimliğini yeniden kullanın. Tarayıcıda gerçek kişi kimlik doğrulaması yapmak ve yeni bir grup oluşturmak için boş bırakın. (varsayılan: boş dize) | STRING | Hayır | - |

**Video Kısıtlamaları:**
*   **Süre:** 2 ile 15 saniye arasında olmalıdır.
*   **Boyutlar:** Genişlik ve yükseklik 300 ile 6000 piksel arasında olmalıdır.
*   **En Boy Oranı:** Genişlik-yükseklik oranı 0,4 ile 2,5 arasında olmalıdır.
*   **Toplam Piksel:** Toplam piksel sayısı (genişlik × yükseklik) 409.600 ile 927.408 arasında olmalıdır.
*   **Kare Hızı:** Saniyede 24 ile 60 kare (FPS) arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `asset_id` | Yeni oluşturulan video varlığı için benzersiz tanımlayıcı. | STRING |
| `group_id` | Yeni videoyu içeren varlık grubunun tanımlayıcısı. Bu, sağlanan `group_id` veya yeni oluşturulan bir kimlik olacaktır. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/tr.md)

---
**Source fingerprint (SHA-256):** `9da0872cf8df32765e3fb1eef50bc24f53b65e069d8ef2609de1075d89edd605`
