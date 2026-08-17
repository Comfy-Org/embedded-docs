# Lumina2 için CLIP Metin Kodlama

Lumina2 için CLIP Text Encode düğümü, bir sistem istemini ve bir kullanıcı istemini, difüzyon modelinin belirli görüntüler üretmesini yönlendirebilecek bir katıştırmaya kodlamak için bir CLIP modeli kullanır. Önceden tanımlanmış bir sistem istemini özel metin isteminizle birleştirir ve görüntü üretimi için koşullandırma verileri oluşturmak üzere bunları CLIP modelinden geçirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2 iki tür sistem istemi sağlar: "superior", üstün görüntü-metin uyumuna sahip görüntüler üretir; "alignment", en yüksek derecede görüntü-metin uyumuna sahip yüksek kaliteli görüntüler üretir. | COMBO | Evet | `"superior"`<br>`"alignment"` |
| `user_prompt` | Kodlanacak metin. Çok satırlı girdiyi ve dinamik istemleri destekler. | STRING | Evet | N/A |
| `clip` | Metni kodlamak için kullanılan CLIP modeli. | CLIP | Evet | N/A |

**Not:** `clip` girdisi zorunludur ve None olamaz. clip girdisi geçersizse, düğüm, kontrol noktasının geçerli bir CLIP veya metin kodlayıcı modeli içermeyebileceğini belirten bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Difüzyon modelini yönlendirmek için kullanılan, katıştırılmış metni içeren bir koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/tr.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
