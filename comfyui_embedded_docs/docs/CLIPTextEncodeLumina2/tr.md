CLIP Metin Kodlama (Lumina2) düğümü, bir sistem yönergesini ve bir kullanıcı yönergesini CLIP modeli kullanarak, difüzyon modelini belirli görüntüler üretmeye yönlendirebilecek bir gömülü vektöre (embedding) kodlar. Önceden tanımlanmış bir sistem yönergesini, özel metin yönergenizle birleştirir ve bunları CLIP modeli aracılığıyla işleyerek görüntü oluşturma için koşullama verisi (conditioning data) oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sistem_istemi` | Lumina2 iki tür sistem yönergesi sağlar: "superior" üstün görüntü-metin uyumuna sahip görüntüler üretir; "alignment" ise en yüksek derecede görüntü-metin uyumuna sahip yüksek kaliteli görüntüler üretir. | STRING | Evet | `"superior"`<br>`"alignment"` |
| `kullanıcı_istemi` | Kodlanacak metin. Çok satırlı girişi ve dinamik yönergeleri destekler. | STRING | Evet | Yok |
| `clip` | Metni kodlamak için kullanılan CLIP modeli. | CLIP | Evet | Yok |

**Not:** `clip` girişi zorunludur ve boş (None) olamaz. clip girişi geçersizse, düğüm kontrol noktasının (checkpoint) geçerli bir CLIP veya metin kodlayıcı modeli içermeyebileceğini belirten bir hata verecektir.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Difüzyon modelini yönlendirmek için kullanılan, kodlanmış metni içeren bir koşullama (conditioning). | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/tr.md)

---
**Source fingerprint (SHA-256):** `fcc0802180ffc2c0757b395850d54632da011473da0c6b1c5268b42da3747024`
