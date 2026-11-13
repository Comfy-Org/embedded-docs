# Krea 2 Stil Referansı

## Genel Bakış

Krea 2 Stil Referansı düğümü, Krea 2 görüntü oluşturma işleminin stilini etkilemek için bir referans görüntü eklemenizi sağlar. Birden fazla stil referansını birbirine zincirleyebilir (toplam 10'a kadar) ve birleştirilmiş sonucu bir Krea 2 Görüntü düğümüne besleyebilirsiniz. Sağladığınız her görüntü ComfyAPI deposuna yüklenir ve URL olarak iletilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görsel` | Stili oluşturmayı etkileyen referans görüntü. | IMAGE | Evet | - |
| `güç` | Referans gücü (varsayılan: 1,0). | FLOAT | Evet | 0,0 ila 1,0 (adım: 0,05) |
| `stil_referansı` | İsteğe bağlı gelen stil referansları zinciri; bu düğüm bir tane daha ekler. | STYLE_REF | Hayır | - |

**Kısıtlamalar hakkında not:** Toplamda en fazla 10 stil referansını zincirleyebilirsiniz. 11. referansı eklemeye çalışırsanız, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `stil_referansı` | Her biri bir URL ve güç değeri içeren stil referans girişlerinin listesi. Bu çıktıyı bir Krea 2 Görüntü düğümüne besleyin. | STYLE_REF |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `6f68e5eea264e77beed4f9c5f4c8830fce7c25dfac813ffbf1951eafbb7edf72`
