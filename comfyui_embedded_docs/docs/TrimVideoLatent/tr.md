> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/tr.md)

TrimVideoLatent düğümü, bir video gizli temsilinin başındaki kareleri kaldırır. Bir gizli video örneği alır ve başlangıçtan itibaren belirtilen sayıda kareyi keserek videonun kalan kısmını döndürür. Bu, ilk kareleri kaldırarak video dizilerini kısaltmanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `örnekler` | LATENT | Evet | - | Kırpılacak video karelerini içeren giriş gizli video temsili |
| `kırpma_miktarı` | INT | Evet | 0 ila 99999 | Videonun başından kaldırılacak kare sayısı (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | LATENT | Başlangıçtan itibaren belirtilen sayıda karenin kaldırıldığı kırpılmış gizli video temsili |

---
**Source fingerprint (SHA-256):** `7fd482533d1f63219565a3a25776173c77c419fbf5086015d42136f5bfdfbed2`
