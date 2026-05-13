> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/tr.md)

Bu düğüm, bir 3B modelin dokularını düzenlemek için Tencent Hunyuan3D API'sini kullanır. Bir 3B model ve istenen değişikliklerin metin açıklamasını sağlarsınız; düğüm, isteminize göre dokuları yeniden çizilmiş modelin yeni bir sürümünü döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Evet | FBX, Herhangi | FBX formatında 3B model. Model 100.000'den az yüze sahip olmalıdır. |
| `prompt` | STRING | Evet | | Doku düzenlemeyi açıklar. En fazla 1024 UTF-8 karakterini destekler. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) |

**Not:** `model_3d` girişi FBX formatında bir dosya olmalıdır. Bu düğüm tarafından diğer 3B dosya biçimleri desteklenmez.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `GLB` | FILE3D | GLB formatında işlenmiş 3B model. |
| `OBJ` | FILE3D | OBJ formatında işlenmiş 3B model. |
| `texture_image` | IMAGE | 3B model için yeni oluşturulan doku görüntüsü. |

---
**Source fingerprint (SHA-256):** `c8e81fcfc24707746b8d1291d31aff325523cd93a627b896402ce1b5a96c7e87`
