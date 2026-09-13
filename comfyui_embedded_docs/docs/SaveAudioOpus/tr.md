# Sesi Kaydet (Opus)

SaveAudioOpus düğümü, ses verilerini Opus biçiminde bir dosyaya kaydeder; dışa aktarılan dosya için kodlama kalitesini (bit hızı) ve dosya adı önekini seçmenize olanak tanır. Bu düğüm kullanımdan kaldırılmıştır ve gelecek sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Opus dosyası olarak kaydedilecek ses verisi. Bunun None olması durumunda (örneğin, kaynak videoda ses parçası olmadığında) bir ValueError yükseltilir. | AUDIO | Evet | - |
| `dosya_adı_ön_eki` | Çıktı dosya adı için kullanılan önek (varsayılan: "audio/ComfyUI"). | STRING | Hayır | - |
| `kalite` | Opus dosyasını kodlamak için kullanılan bit hızı; daha yüksek değerler daha iyi kalite ancak daha büyük dosyalar üretir (varsayılan: "128k"). | COMBO | Hayır | `"64k"`<br>`"96k"`<br>`"128k"`<br>`"192k"`<br>`"320k"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Opus dosyasına kaydedilen ses verisi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/tr.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
