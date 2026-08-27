# Flux Görsel Silme

Maskelenmiş nesneyi görüntüden kaldırır ve arka planı yeniden oluşturur. Silmek istediğiniz şeyin üzerine maskeyi boyayın; düğüm, alanı makul bir arka plan içeriğiyle doldurur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görsel` | İşlenecek giriş görüntüsü | IMAGE | Evet | - |
| `mask` | Beyaz alanlar kaldırılır; siyah alanlar korunur | MASK | Evet | - |
| `piksel_genişlet` | Nesnenin kenarlarının temiz bir şekilde kaplanmasını sağlamak için maske sınırlarını genişletir (varsayılan: 10) | INT | Evet | 0 ile 25 |
| `seed` | Gürültüyü oluşturmak için kullanılan rastgele tohum (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |

**Not:** Giriş görüntüsü her iki boyutta da en az 256x256 piksel olmalıdır. Maske, görüntü boyutlarıyla eşleşecek şekilde otomatik olarak yeniden boyutlandırılır ve işleme başlamadan önce görüntünün alfa kanalı kaldırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Maskelenmiş nesnenin kaldırıldığı ve arka planın yeniden oluşturulduğu sonuç görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/tr.md)

---
**Source fingerprint (SHA-256):** `124be59b9829aa9f865d7ec76cd68f7978e2010cd3a84f25742a1c17f2d70b76`
