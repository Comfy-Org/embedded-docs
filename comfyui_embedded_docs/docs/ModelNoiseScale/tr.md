> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/tr.md)

# Genel Bakış

Bu düğüm, model örneklemesi sırasında kullanılan gürültü ölçeğini ayarlar. Modelin örnekleme sürecine uygulanan gürültü miktarını kontrol eden belirli bir gürültü ölçeği değeri belirlemenizi sağlar.

# Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Gürültü ölçeği ayarının uygulanacağı model. |
| `gürültü_ölçeği` | FLOAT | Evet | 0.0 ile 64.0 arası (adım: 0.01) | Mutlak eğitim gürültü ölçeği. Örneğin HiDream-O1 taban: 8.0, geliştirici: 7.5. (varsayılan: 1.0) |

# Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `MODEL` | MODEL | Yeni gürültü ölçeği uygulanmış değiştirilmiş model. |

---
**Source fingerprint (SHA-256):** `37b77a5d65fb872f45be8ffa4efb65037bc7459bb001babaaf6b526a9a735190`
