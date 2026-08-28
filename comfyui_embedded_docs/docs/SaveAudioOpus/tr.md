# Sesi Kaydet (Opus)

SaveAudioOpus düğümü, ses verilerini Opus formatında bir dosyaya kaydeder. Bir ses girdisi alır ve yapılandırılabilir kalite ayarlarıyla sıkıştırılmış bir Opus dosyası olarak dışa aktarır. Bu düğüm kullanımdan kaldırılmıştır ve gelecekteki sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Opus dosyası olarak kaydedilecek ses verisi. Bu değer None ise (örneğin, kaynak videoda ses parçası olmadığında) bir ValueError yükseltilir. | AUDIO | Evet | - |
| `dosya_adı_ön_eki` | Çıktı dosya adı için ön ek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |
| `kalite` | Opus dosyasını kodlamak için kullanılan bit hızı; daha yüksek değerler daha iyi kalite ancak daha büyük dosyalar üretir (varsayılan: "128k") | COMBO | Hayır | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Opus dosyasına kaydedilen ses verisi | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/tr.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
