## Genel Bakış

Hem pozitif hem de negatif koşullandırmaya referans görseller ekleyin. Bu düğüm, görüntü oluşturma sürecini yönlendirmek için kullanılacak bir veya daha fazla referans görsel sağlamanıza olanak tanır; bu, bir talimata dayalı düzenleme veya konu odaklı kişiselleştirme için yapılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Referans görsellerin ekleneceği pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negatif` | Referans görsellerin ekleneceği negatif koşullandırma. | CONDITIONING | Evet | - |
| `görseller` | Referans görseller. 1 görsel, talimata dayalı düzenlemeyi etkinleştirir; 2-10 görsel, çoklu referans konu odaklı kişiselleştirmeyi etkinleştirir. | IMAGE | Evet | 1 ila 10 görsel |

**`images` parametresi hakkında not:** Bu, 1 ila 10 görsel arasında kabul eden otomatik büyüyen bir girdidir. Görseller `image_1` ile `image_10` arasında etiketlenir. En az 1 görsel sağlamanız gerekir. Görsel sayısı çalışma modunu belirler: tek bir görsel düzenleme talimatları için kullanılırken, birden fazla görsel (2-10) konu odaklı kişiselleştirme için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Referans görsellerin eklendiği pozitif koşullandırma. | CONDITIONING |
| `negatif` | Referans görsellerin eklendiği negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/tr.md)

---
**Source fingerprint (SHA-256):** `b14a8fc2acd44618370bd7e94758d469ff37530f2e19498a6c72ee3748559303`
