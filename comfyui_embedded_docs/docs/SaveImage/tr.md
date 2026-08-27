# Görüntüyü Kaydet

SaveImage düğümü, girdi görüntülerini PNG dosyaları olarak ComfyUI çıktı dizininize kaydeder. İş akışı meta verileri (prompt gibi) kaydedilen her dosyaya gömülebilir ve görüntüler, diğer düğümler tarafından kullanılmaya devam edilebilmesi için değiştirilmeden döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `dosyaadı_öneki` | Kaydedilecek dosyanın öneki. Bu, düğümlerden değerler eklemek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: "ComfyUI"). | STRING | Evet | - |

Düğüm ayrıca, ComfyUI tarafından iş akışı promptu ve ek PNG bilgileriyle otomatik olarak doldurulan `prompt` ve `extra_pnginfo` adlı iki gizli girdi alır. Meta veri etkinleştirildiğinde, bu bilgiler kaydedilen her PNG dosyasına metin meta verisi olarak gömülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Orijinal girdi görüntüleri, diske kaydedildikten sonra değiştirilmeden döndürülür. | IMAGE |
| `ui` | Yalnızca arayüz için kullanılan; ön uçta görüntülenmek üzere kaydedilmiş görüntü dosyalarının (dosya adı, alt klasör ve tür) listesini içeren sonuç. | UI_RESULT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/tr.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
