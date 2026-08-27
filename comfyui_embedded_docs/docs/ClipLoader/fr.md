# ClipLoader

Le nœud CLIPLoader charge un modèle d'encodeur de texte (CLIP, T5 ou similaire) à partir d'un fichier, le rendant disponible pour d'autres nœuds qui doivent convertir des invites textuelles en représentations numériques. Il prend en charge une grande variété d'architectures de modèles, chacune nécessitant un type d'encodeur spécifique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_name` | Le nom du fichier du modèle d'encodeur de texte à charger. Ce doit être un fichier situé dans le répertoire `ComfyUI/models/text_encoders/`. | STRING | Oui | Liste des fichiers trouvés dans le dossier `text_encoders` |
| `type` | Le type d'architecture du modèle chargé. Il détermine la variante d'encodeur spécifique à utiliser (par défaut : `"stable_diffusion"`). | COMBO | Oui | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `appareil` | L'appareil sur lequel charger le modèle. `"default"` utilise le GPU s'il est disponible, tandis que `"cpu"` force le chargement sur le CPU. Il s'agit d'une option avancée (par défaut : `"default"`). | COMBO | Non | `"default"`<br>`"cpu"` |

### Correspondances type-encodeur prises en charge

Le paramètre `type` sélectionne le bon encodeur pour une architecture de modèle donnée. Voici les correspondances courantes :

| Type | Encodeur |
|------|----------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (padding de 226 jetons) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recommandé) ou t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL ou Music3 Qwen/RVQ |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `clip` | Le modèle d'encodeur de texte chargé, prêt à être connecté à d'autres nœuds pour l'encodage de texte et le conditionnement. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/fr.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
