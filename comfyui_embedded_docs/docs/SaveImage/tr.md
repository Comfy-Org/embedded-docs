# Görüntüyü Kaydet

SaveImage düğümü, giriş görüntülerini ComfyUI çıktı dizininize PNG dosyaları olarak kaydeder. Her kaydedilen dosyaya istem gibi iş akışı meta verilerini gömebilir ve görüntüleri değiştirmeden döndürür; böylece diğer düğümler tarafından hâlâ kullanılabilirler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `dosyaadı_öneki` | Kaydedilecek dosyanın ön eki. Düğümlerden değerleri dahil etmek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: "ComfyUI"). | STRING | Evet | - |

Düğüm ayrıca, ComfyUI tarafından iş akışı istemi ve ek PNG bilgileriyle otomatik olarak doldurulan `prompt` ve `extra_pnginfo` adlı iki gizli giriş alır. Meta veriler etkinleştirildiğinde, bu bilgiler kaydedilen her PNG dosyasına metin meta verisi olarak gömülür.

Kaydedilen her görüntünün dosya adı, `filename_prefix`, görüntünün toplu iş içindeki konumuyla değiştirilen isteğe bağlı bir `%batch_num%` yer tutucusu ve beş basamaklı bir sayaçtan oluşturulur; örneğin `ComfyUI_00001_.png`. Görüntüler PNG sıkıştırma düzeyi 4 ile yazılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Orijinal giriş görüntüleri; diske kaydedildikten sonra değiştirilmeden döndürülür. | IMAGE |
| `ui` | Ön uçta görüntülenmek üzere kaydedilen görüntü dosyalarının listesini (dosya adı, alt klasör ve tür) içeren yalnızca UI'ye özel bir sonuç. | UI_RESULT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/tr.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
