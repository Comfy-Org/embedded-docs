# Optik Akış Modelini Yükle

## Genel Bakış

`models/optical_flow/` klasöründen bir optik akış modeli yükler. Şu anda yalnızca torchvision'ın RAFT-large formatı desteklenmektedir; bu format, VOIDWarpedNoise düğümü tarafından kullanılan modeldir. ComfyUI optik akış ağırlıklarını otomatik olarak indirmez; kontrol noktası dosyasını manuel olarak `models/optical_flow/` dizinine yerleştirmeniz gerekir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek optik akış modeli. Dosyalar `optical_flow` klasörüne yerleştirilmelidir. Şu anda yalnızca torchvision'ın `raft_large.pth` dosyası desteklenmektedir. | COMBO | Evet | `models/optical_flow/` klasöründeki dosyaların listesi |

Seçilen dosya, torchvision RAFT-large kontrol noktası olmalıdır. Düğüm, dosyanın beklenen RAFT anahtarlarını (`feature_encoder.*`, `context_encoder.*` ve `update_block.*`) içerip içermediğini kontrol eder ve biçim tanınmazsa bir ValueError hatası verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `OPTICAL_FLOW` | Diğer düğümlerle kullanılmak üzere bir ModelPatcher içine sarılmış, yüklenen optik akış modeli. | OPTICAL_FLOW |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/tr.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
