Runway Metinden Görsele düğümü, Runway'in Gen 4 modelini kullanarak metin istemlerinden görseller oluşturur. Bir metin açıklaması ve isteğe bağlı olarak görsel oluşturma sürecini yönlendirmek için bir referans görseli sağlayabilirsiniz. Düğüm, API iletişimini yönetir ve oluşturulan görseli döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Oluşturma için metin istemi (varsayılan: "") | STRING | Evet | - |
| `oran` | Oluşturulan görsel için en-boy oranı | COMBO | Evet | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" |
| `referans_görsel` | Oluşturmayı yönlendirmek için isteğe bağlı referans görseli | IMAGE | Hayır | - |

**Not:** Referans görselinin boyutları 7999x7999 pikseli geçmemeli ve en-boy oranı 0,5 ile 2,0 arasında olmalıdır. Bir referans görseli sağlandığında, görsel oluşturma sürecini yönlendirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Metin istemine ve isteğe bağlı referans görseline dayalı olarak oluşturulan görsel | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `140f8e6b07216892d84f2d7fbc3afaf1c390e98ddedf27d4926032066a783f67`
