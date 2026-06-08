# Flux Silme Düğümü

Maskelenen nesneyi görüntüden kaldırır ve arka planı yeniden oluşturur. Silinecek alanın üzerine maske çizin; düğüm, bu alanı olası arka plan içeriğiyle doldurur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `görsel` | İşlenecek giriş görüntüsü | IMAGE | Evet | - |
| `mask` | Beyaz alanlar kaldırılır; siyah alanlar korunur | MASK | Evet | - |
| `piksel_genişlet` | Nesne kenarlarının temiz bir şekilde kaplanmasını sağlamak için maske sınırlarını genişletir (varsayılan: 10) | INT | Evet | 0 ile 25 |
| `seed` | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |

**Not:** Giriş görüntüsü her iki boyutta da en az 256x256 piksel olmalıdır. Maske, görüntü boyutlarına uyacak şekilde otomatik olarak yeniden boyutlandırılır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `IMAGE` | Maskelenen nesnenin kaldırıldığı ve arka planın yeniden oluşturulduğu sonuç görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/tr.md)

---
**Source fingerprint (SHA-256):** `70cf3223bc1ba0528cf99e84f073bd7a1bbcc26164cef99f4deb1645038fbf11`
