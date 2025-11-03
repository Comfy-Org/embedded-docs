> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/tr.md)

SVG dosyalarını diskte kaydeder. Bu düğüm, SVG verilerini girdi olarak alır ve isteğe bağlı meta veri gömme özelliği ile çıktı dizininize kaydeder. Düğüm, sayaç sonekleriyle dosya adlandırmayı otomatik olarak halleder ve iş akışı prompt bilgilerini doğrudan SVG dosyasına gömebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `svg` | SVG | Evet | - | Diske kaydedilecek SVG verisi |
| `filename_prefix` | STRING | Evet | - | Kaydedilecek dosya için ön ek. Bu, düğümlerden gelen değerleri dahil etmek için %date:yyyy-MM-dd% veya %Empty Latent Image.width% gibi biçimlendirme bilgileri içerebilir. (varsayılan: "svg/ComfyUI") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui` | DICT | ComfyUI arayüzünde görüntülenmek üzere dosya adı, alt klasör ve tür dahil olmak üzere dosya bilgilerini döndürür |

**Not:** Bu düğüm, mevcut olduğunda iş akışı meta verilerini (prompt ve ek PNG bilgileri) otomatik olarak SVG dosyasına gömer. Meta veriler, SVG'nin meta veri öğesi içinde bir CDATA bölümü olarak eklenir.