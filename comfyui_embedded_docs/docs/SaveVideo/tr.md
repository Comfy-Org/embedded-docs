SaveVideo düğümü, giriş video içeriğini ComfyUI çıktı dizininize kaydeder. Kaydedilen dosya için dosya adı ön eki, video formatı ve codec bileşenini belirlemenize olanak tanır. Düğüm, sayaç artışlarıyla dosya adlandırmayı otomatik olarak yönetir ve kaydedilen videoya iş akışı meta verilerini dahil edebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kaydedilecek video. | VIDEO | Evet | - |
| `dosyaadı_öneki` | Kaydedilecek dosyanın ön eki. Bu, düğümlerden değerler eklemek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: "video/ComfyUI"). | STRING | Hayır | - |
| `format` | Videonun kaydedileceği format (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"mp4"`<br>`"webm"`<br>`"mkv"`<br>`"gif"` |
| `codec` | Video için kullanılacak codec bileşeni (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"h264"`<br>`"h265"`<br>`"vp9"`<br>`"av1"`<br>`"prores"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *Çıktı yok* | Bu düğüm herhangi bir çıktı verisi döndürmez. | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/tr.md)

---
**Source fingerprint (SHA-256):** `506ddc8820924688cccb9fd838ff9c0f5217a38f708f28f15a060be9325cea61`
