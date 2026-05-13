> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/tr.md)

LatentBlend düğümü, iki gizli (latent) örneği belirtilen bir karışım faktörü kullanarak birleştirir. İki gizli girdi alır ve ilk örneğin karışım faktörüyle, ikinci örneğin ise tersiyle ağırlıklandırıldığı yeni bir çıktı oluşturur. Girdi örnekleri farklı boyutlara sahipse, ikinci örnek otomatik olarak ilk örneğin boyutlarına yeniden boyutlandırılır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples1` | LATENT | Evet | - | Karıştırılacak ilk gizli örnek |
| `samples2` | LATENT | Evet | - | Karıştırılacak ikinci gizli örnek |
| `blend_factor` | FLOAT | Evet | 0 ile 1 | İki örnek arasındaki karışım oranını kontrol eder (varsayılan: 0.5) |

**Not:** `samples1` ve `samples2` farklı boyutlara sahipse, `samples2`, merkez kırpma ile bikübik enterpolasyon kullanılarak `samples1`'in boyutlarına otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `latent` | LATENT | Her iki girdi örneğini birleştiren karıştırılmış gizli örnek |

---
**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`
