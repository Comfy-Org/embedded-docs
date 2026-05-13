> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/fr.md)

Le nœud `CLIPSave` enregistre un modèle d'encodeur de texte CLIP sur le disque au format SafeTensors. Il est conçu pour les workflows avancés de fusion de modèles et sépare automatiquement le modèle CLIP en ses composants (tels que CLIP-L, CLIP-G ou T5XXL) en fonction de la structure interne du modèle, enregistrant chaque composant dans un fichier séparé.

## Entrées

| Paramètre | Type de données | Type d'entrée | Valeur par défaut | Plage | Description |
|-----------|-----------------|---------------|-------------------|-------|-------------|
| `clip` | CLIP | Requis | - | - | Le modèle CLIP à enregistrer. |
| `filename_prefix` | STRING | Requis | `clip/ComfyUI` | - | Le chemin de préfixe et le nom de fichier pour le(s) fichier(s) enregistré(s). Le nœud ajoutera un suffixe de composant (par exemple `_clip_l`, `_clip_g`) et un compteur pour créer des noms de fichiers uniques. |
| `prompt` | PROMPT | Caché | - | - | Les informations du prompt du workflow, enregistrées comme métadonnées dans le fichier de sortie. |
| `extra_pnginfo` | EXTRA_PNGINFO | Caché | - | - | Métadonnées supplémentaires, enregistrées sous forme de paires clé-valeur dans le fichier de sortie. |

## Sorties

Ce nœud n'a pas de connexions de sortie. Il enregistre les fichiers traités directement dans le répertoire `ComfyUI/output/`.

### Détails des fichiers enregistrés

Le nœud analyse le dictionnaire d'état du modèle CLIP et enregistre des fichiers SafeTensors séparés pour chaque composant détecté. Le composant est identifié par le préfixe de ses clés de paramètres. Les préfixes suivants sont vérifiés :

- `clip_l.` (encodeur de texte CLIP-L)
- `clip_g.` (encodeur de texte CLIP-G)
- `clip_h.` (encodeur de texte CLIP-H)
- `t5xxl.` (encodeur de texte T5-XXL)
- `pile_t5xl.` (encodeur de texte Pile-T5-XL)
- `mt5xl.` (encodeur de texte mT5-XL)
- `umt5xxl.` (encodeur de texte UMT5-XXL)
- `t5base.` (encodeur de texte T5-Base)
- `gemma2_2b.` (encodeur de texte Gemma 2 2B)
- `llama.` (encodeur de texte LLaMA)
- `hydit_clip.` (encodeur de texte Hydit CLIP)
- Préfixe vide (autres composants CLIP)

Pour chaque composant détecté, le nœud crée un fichier avec le nom `{filename_prefix}_{counter:05}_.safetensors`, où le préfixe du composant est ajouté au préfixe du nom de fichier (par exemple `clip/ComfyUI_clip_l_00001_.safetensors`). Le préfixe `transformer.` est supprimé des clés de paramètres lors de l'enregistrement.

---
**Source fingerprint (SHA-256):** `039b39cbfb9b04ccebc5fc885ebe75dfde14838530d38133d0a3a6311e392059`
