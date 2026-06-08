# TripoSplat Görüntü Ön İşleme

Bu düğüm, her bir giriş görüntüsünü siyah bir arka plan üzerinde ortalanmış bir kare şeklinde kırpar ve ardından belirtilen çıktı boyutuna ulaşmak için dolgu ekler. TripoSplat 3B modeli için tutarlı kare çerçeveleme ve kenar yapaylıklarını önlemek için isteğe bağlı alfa mat aşındırması sağlayarak görüntüleri hazırlamak üzere tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `görüntü` | Ön işlenecek giriş görüntüsü(ler)i | IMAGE | Evet | - |
| `mask` | Kırpma bölgesini belirlemek için kullanılan görüntü alfa maskesi | MASK | Evet | - |
| `aşındırma_yarıçapı` | Kırpmadan önce alfa matını bu piksel yarıçapında aşındırır (kenar taşmasını önler). Varsayılan: 1 | INT | Evet | 0 ile 16 |
| `boyut` | Kare görüntü boyutu. Model 1024'te eğitilmiştir; diğer boyutlar çalışır ancak dağılım dışıdır. Varsayılan: 1024 | INT | Evet | 256 ile 4096 (16'lık adımlarla) |

**Not:** `mask` girişi zorunludur ve sağlanmalıdır. Maskenin toplu iş boyutu görüntüden farklıysa, eşleşmesi için otomatik olarak tekrarlanır. Maske boyutları görüntü boyutlarından farklıysa, maske çift doğrusal enterpolasyon kullanılarak görüntüyle eşleşecek şekilde yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `görüntü` | Siyah arka plan üzerinde ortalanmış kare şeklinde kırpılmış ve dolgulu ön işlenmiş görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/tr.md)

---
**Source fingerprint (SHA-256):** `3f33dbc3a99ccb23ede767915a28fabdfa388edb8d5782edea3f8d03e5965b2a`
