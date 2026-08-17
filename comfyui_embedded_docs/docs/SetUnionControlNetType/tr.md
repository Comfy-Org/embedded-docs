# BileşimControlNetTürüAyarla

SetUnionControlTypeNode, koşullandırma için kullanılan bir kontrol ağının kontrol türünü ayarlamanızı sağlar. Mevcut bir kontrol ağını alır, bunun değiştirilmiş bir kopyasını oluşturur ve seçilen kontrol türünü bu kopyada saklar; böylece orijinal değişmeden kalır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `control_net` | Seçilen kontrol türüyle kopyalanacak ve değiştirilecek kontrol ağı | CONTROL_NET | Evet | - |
| `type` | Kopyalanan kontrol ağına uygulanacak kontrol türü. Kontrol türünü ayarlanmamış bırakmak için "auto" seçin veya mevcut birleşik kontrol ağı türlerinden belirli bir tür seçin (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

Not: `type` "auto" olduğunda, kopyalanan kontrol ağındaki kontrol türü listesi temizlenir. Belirli bir tür seçildiğinde, kopyalanan kontrol ağı ilgili tür numarasını saklar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `control_net` | Seçilen kontrol türü uygulanmış kontrol ağının değiştirilmiş kopyası | CONTROL_NET |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/tr.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
