> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/tr.md)

NAGuidance düğümü, bir modele Normalize Edilmiş Dikkat Yönlendirmesi uygular. Bu teknik, örnekleme sürecinde modelin dikkat mekanizmasını değiştirerek istenmeyen kavramlardan uzaklaşmayı sağlar ve böylece damıtılmış veya schnell modellerle negatif prompt'ların kullanılmasına olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Normalize Edilmiş Dikkat Yönlendirmesi uygulanacak model. |
| `nag_scale` | FLOAT | Evet | 0.0 - 50.0 | Yönlendirme ölçek faktörü. Daha yüksek değerler, üretimi negatif prompt'tan daha fazla uzaklaştırır. (varsayılan: 5.0) |
| `nag_alpha` | FLOAT | Evet | 0.0 - 1.0 | Normalize edilmiş dikkat için karıştırma faktörü. 1.0 değeri orijinal dikkati tamamen değiştirirken, 0.0 değerinin hiçbir etkisi yoktur. (varsayılan: 0.5) |
| `nag_tau` | FLOAT | Evet | 1.0 - 10.0 | Normalleştirme oranını sınırlamak için kullanılan bir ölçeklendirme faktörü. (varsayılan: 1.5) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Normalize Edilmiş Dikkat Yönlendirmesi etkinleştirilmiş, yamalanmış model. |