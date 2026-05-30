> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/tr.md)

## Genel Bakış

Bu düğüm, farklı hızlara sahip birden çok grafik kartı kullanırken her bir GPU'nun göreceli performansını belirlemenizi sağlar. Cihazlar arasında iş dağıtımı için kullanılabilecek bir GPU seçenekleri grubu oluşturur, ancak hız tabanlı iş yükü dağıtımı henüz mevcut sürümde uygulanmamıştır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `device_index` | INT | Evet | 0 ila 64 | Yapılandırılacak GPU cihazının indeks numarası (varsayılan: 0) |
| `relative_speed` | FLOAT | Evet | 0.0 ila sınırsız | Bu GPU'nun diğerlerine göre göreceli hızı, iş yükü dağıtımı için kullanılır (varsayılan: 1.0, adım: 0.01) |
| `gpu_options` | GPU_OPTIONS | Hayır | - | Bu cihazın seçeneklerini eklemek için mevcut bir GPU seçenekleri grubu. Sağlanmazsa yeni bir grup oluşturulur |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `GPU_OPTIONS` | GPU_OPTIONS | Yapılandırılmış cihaz ayarlarını içeren bir GPU seçenekleri grubu. Çoklu GPU işlemleri için diğer düğümlere aktarılabilir |

**Not:** `relative_speed` parametresi tanımlanmış olsa da, dahili zamanlayıcı tarafından iş yükünü GPU'lar arasında dağıtmak için henüz kullanılmamaktadır. Mevcut uygulamada, iş yükü göreceli hızlardan bağımsız olarak tüm cihazlara eşit şekilde dağıtılır.

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
