# Optik Akış Modelini Yükle

`models/optical_flow/` klasöründen bir optik akış modeli yükler. Şu anda yalnızca torchvision'ın RAFT-large formatı desteklenmektedir; bu, VOIDWarpedNoise düğümü tarafından kullanılan modeldir. ComfyUI optik akış ağırlıklarını otomatik olarak indirmez; checkpoint dosyasını manuel olarak `models/optical_flow/` dizinine yerleştirmelisiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek optik akış modeli. Dosyalar `optical_flow` klasörüne yerleştirilmelidir. Şu anda yalnızca torchvision'ın `raft_large.pth` dosyası desteklenmektedir. | COMBO | Evet | `models/optical_flow/` klasöründeki dosyaların listesi |

Not: Seçilen checkpoint, önekleri `feature_encoder.`, `context_encoder.` ve `update_block.` olan anahtarlar içeren bir torchvision RAFT-large state dict olmalıdır. Dosya bu formata uymuyorsa, düğüm bir ValueError hatası verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `OPTICAL_FLOW` | Yüklenen optik akış modeli; değerlendirme moduna ayarlanmış, fp16 destekleyen cihazlarda fp16 hassasiyetinde (aksi halde float32) yüklenmiş, diğer düğümlerle kullanım için bir ModelPatcher ile sarılmıştır. | OPTICAL_FLOW |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/tr.md)

---
**Source fingerprint (SHA-256):** `82e5d747679ede113ec4d72fd6eda4b8f20d098832612bebf26ef65de8b4b3dc`
