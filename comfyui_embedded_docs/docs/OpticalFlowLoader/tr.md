# Optik Akış Modelini Yükle

## Genel Bakış

`models/optical_flow/` klasöründen bir optik akış modeli yükler. Şu anda yalnızca VOIDWarpedNoise düğümü tarafından kullanılan torchvision'ın RAFT-large formatı desteklenmektedir. ComfyUI, optik akış ağırlıklarını otomatik olarak indirmez; kontrol noktası dosyasını manuel olarak `models/optical_flow/` dizinine yerleştirmeniz gerekir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek optik akış modeli. Dosyalar `optical_flow` klasörüne yerleştirilmelidir. Bugün itibarıyla yalnızca torchvision'ın `raft_large.pth` dosyası desteklenmektedir. | STRING | Evet | `models/optical_flow/` klasöründeki dosyaların listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `OPTICAL_FLOW` | Yüklenen optik akış modeli, diğer düğümlerle kullanılmak üzere bir ModelPatcher ile sarılmıştır. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/tr.md)

---
**Source fingerprint (SHA-256):** `94bab0bb7e2b9d9b3f343337799eccc744f79275b72a6fad9681b408b4a0820b`
