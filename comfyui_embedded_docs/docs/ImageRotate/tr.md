# Görüntü Döndürme

ImageRotate düğümü, giriş görüntüsünü belirtilen açılarla döndürür. Dört döndürme seçeneğini destekler: döndürme yok, saat yönünde 90 derece, 180 derece ve saat yönünde 270 derece. Döndürme işlemi, görüntü veri bütünlüğünü koruyan verimli tensör işlemleri kullanılarak gerçekleştirilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Döndürülecek giriş görüntüsü | IMAGE | Evet | - |
| `döndürme` | Görüntüye uygulanacak döndürme açısı (varsayılan: "none") | STRING | Evet | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Döndürülmüş çıktı görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/tr.md)

---
**Source fingerprint (SHA-256):** `068946b31ebe87b2524a1e628b5bc0a3da7367d7252fa7afafe96bcbb174747d`
