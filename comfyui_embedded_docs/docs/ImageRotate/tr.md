> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/tr.md)

ImageRotate düğümü, giriş görüntüsünü belirtilen açılarla döndürür. Dört döndürme seçeneğini destekler: döndürme yok, saat yönünde 90 derece, 180 derece ve saat yönünde 270 derece. Döndürme işlemi, görüntü veri bütünlüğünü koruyan verimli tensör işlemleri kullanılarak gerçekleştirilir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `görüntü` | IMAGE | Evet | - | Döndürülecek giriş görüntüsü |
| `döndürme` | STRING | Evet | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" | Görüntüye uygulanacak döndürme açısı (varsayılan: "none") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `görüntü` | IMAGE | Döndürülmüş çıktı görüntüsü |

---
**Source fingerprint (SHA-256):** `068946b31ebe87b2524a1e628b5bc0a3da7367d7252fa7afafe96bcbb174747d`
