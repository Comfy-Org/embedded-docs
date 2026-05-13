> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/tr.md)

Runway Metinden Görsele düğümü, Runway'in Gen 4 modelini kullanarak metin istemlerinden görseller oluşturur. Bir metin açıklaması ve isteğe bağlı olarak görsel oluşturma sürecini yönlendirmek için bir referans görseli sağlayabilirsiniz. Düğüm, API iletişimini yönetir ve oluşturulan görseli döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `prompt` | STRING | Evet | - | Oluşturma için metin istemi (varsayılan: "") |
| `ratio` | COMBO | Evet | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" | Oluşturulan görsel için en-boy oranı |
| `reference_image` | IMAGE | Hayır | - | Oluşturmayı yönlendirmek için isteğe bağlı referans görseli |

**Not:** Referans görselinin boyutları 7999x7999 pikseli geçmemeli ve en-boy oranı 0,5 ile 2,0 arasında olmalıdır. Bir referans görseli sağlandığında, görsel oluşturma sürecini yönlendirir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | IMAGE | Metin istemine ve isteğe bağlı referans görseline dayalı olarak oluşturulan görsel |

---
**Source fingerprint (SHA-256):** `140f8e6b07216892d84f2d7fbc3afaf1c390e98ddedf27d4926032066a783f67`
