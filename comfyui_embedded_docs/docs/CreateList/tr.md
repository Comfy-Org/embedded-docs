> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/tr.md)

Liste Oluştur düğümü, birden fazla girdiyi tek bir sıralı listede birleştirir. Aynı veri türünden herhangi bir sayıda girdi alır ve bunları bağlandıkları sırayla birleştirir. Bu düğüm, bir iş akışında diğer düğümler tarafından işlenmek üzere görüntü veya metin gibi veri grupları hazırlamak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `input_*` | Değişken | Evet | Herhangi | Değişken sayıda girdi yuvası. Artı (+) simgesine tıklayarak daha fazla girdi ekleyebilirsiniz. Tüm girdiler aynı veri türünde olmalıdır (örneğin, tümü IMAGE veya tümü STRING). |

**Not:** Düğüm, öğeleri bağladıkça otomatik olarak yeni girdi yuvaları oluşturacaktır. Düğümün doğru çalışması için bağlı tüm girdiler aynı veri türünü paylaşmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `list` | Değişken | Bağlı girdilerdeki tüm öğeleri, sağlandıkları sırayla birleştiren tek bir liste. Çıktı veri türü, girdi veri türüyle eşleşir. |

---
**Source fingerprint (SHA-256):** `d0e10c4d1186e694a72b18407c34cc1df74f77d02c989b507af75594c1a0794e`
