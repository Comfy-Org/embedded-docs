Bu düğüm, birden fazla metin listesini tek bir birleşik listede birleştirir. Giriş olarak listeler halinde metin almak ve bunları birbirine eklemek üzere tasarlanmıştır. Düğüm, birleştirilmiş listedeki toplam metin sayısını kaydeder.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `metinler` | Birleştirilecek metin listeleri. Girişe birden fazla liste bağlanabilir ve bunlar tek bir listede birleştirilir. | STRING | Evet | N/A |

**Not:** Bu düğüm bir grup işlemi olarak yapılandırılmıştır (`is_group_process = True`), yani ana işleme işlevi çalışmadan önce birden fazla liste girişini birleştirerek otomatik olarak işler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `metinler` | Tüm giriş metinlerini içeren tek bir birleştirilmiş liste. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/tr.md)

---
**Source fingerprint (SHA-256):** `043a39a373d03f1ff79dd0746070171bab4d5d915c985e4e64fd35f802b09f69`
