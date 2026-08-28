# ModelNoiseScale

## Genel Bakış

Bu düğüm, model örnekleme sırasında kullanılan gürültü ölçeğini ayarlar. Modelin örnekleme sürecine uygulanan gürültü miktarını kontrol eden belirli bir gürültü ölçeği değeri belirlemenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Gürültü ölçeği ayarının uygulanacağı model. | MODEL | Evet | - |
| `gürültü_ölçeği` | Mutlak eğitim gürültü ölçeği. Örneğin HiDream-O1 base: 8.0, dev: 7.5. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 64.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Yeni gürültü ölçeği uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/tr.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
