# Lumina2 için CLIP Metin Kodlama

Bu düğüm, bir CLIP modeli kullanarak bir sistem istemini ve bir kullanıcı istemini, difüzyon modelini belirli görüntüler üretmeye yönlendirmek için kullanılabilecek bir gömme (embedding) olarak kodlar. Önceden tanımlanmış bir Lumina 2 sistem istemini özel metin isteminizle birleştirir ve görüntü üretimi için koşullandırma verisi oluşturmak üzere bunları CLIP modelinden geçirir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sistem_istemi` | Lumina2 iki tür sistem istemi sunar: Superior: Metin istemlerine veya kullanıcı istemlerine dayalı olarak üstün düzeyde metin-görüntü hizalaması ile üstün görüntüler üretmek üzere tasarlanmış bir asistansınız. Alignment: Metin istemlerine dayalı olarak en yüksek düzeyde metin-görüntü hizalaması ile yüksek kaliteli görüntüler üretmek üzere tasarlanmış bir asistansınız. | COMBO | Evet | `"superior"`<br>`"alignment"` |
| `kullanıcı_istemi` | Kodlanacak metin. Çok satırlı girdi ve dinamik istemleri destekler. | STRING | Evet | N/A |
| `clip` | Metni kodlamak için kullanılan CLIP modeli. | CLIP | Evet | N/A |

**Not:** `clip` girdisi zorunludur ve None olamaz. clip girdisi geçersizse, düğüm, kontrol noktasının geçerli bir CLIP veya metin kodlayıcı modeli içermeyebileceğini belirten bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `CONDITIONING` | Difüzyon modelini yönlendirmek için kullanılan, gömülü metni içeren bir koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/tr.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
