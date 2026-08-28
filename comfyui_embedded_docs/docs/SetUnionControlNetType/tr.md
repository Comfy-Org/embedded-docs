# BileşimControlNetTürüAyarla

SetUnionControlNetType düğümü, bir kontrol ağının hangi kontrol türünü kullanacağını seçmenizi sağlar. Mevcut bir kontrol ağını alır ve seçilen kontrol türüyle değiştirilmiş bir kopya oluşturur; orijinal kontrol ağı değişmeden kalır. "auto" seçildiğinde, depolanan kontrol türü temizlenir ve tür otomatik olarak algılanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `kontrol_ağı` | Yeni bir tür ayarıyla değiştirilecek kontrol ağı | CONTROL_NET | Evet | - |
| `tür` | Uygulanacak kontrol ağı türü. Otomatik tür algılama için "auto" kullanın veya mevcut seçeneklerden belirli bir kontrol ağı türü seçin (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/softedge"`<br>`"canny"`<br>`"scribble"`<br>`"seg"`<br>`"tile"`<br>`"inpaint"`<br>`"lineart"`<br>`"blur"`<br>`"mlsd"`<br>`"normalbae"`<br>`"mask"` |

`type` `"auto"` olarak ayarlandığında, düğüm depolanan kontrol türünü temizler ve tür otomatik olarak algılanabilir. Belirli bir tür seçildiğinde, düğüm eşleşen kontrol türünü kopyalanan kontrol ağında saklar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `control_net` | Belirtilen tür ayarı uygulanmış değiştirilmiş kontrol ağı | CONTROL_NET |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/tr.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
