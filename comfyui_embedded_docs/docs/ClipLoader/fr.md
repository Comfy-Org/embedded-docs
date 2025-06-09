Ce nœud est principalement utilisé pour charger indépendamment les modèles d'encodeur de texte CLIP.
Les fichiers de modèle peuvent être détectés dans les chemins suivants :

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> Si vous sauvegardez un modèle après le démarrage de ComfyUI, vous devrez actualiser l'interface frontend de ComfyUI pour obtenir la liste la plus récente des chemins de fichiers de modèle

Formats de modèle pris en charge :

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

Pour plus de détails sur le chargement des fichiers de modèle les plus récents, consultez [folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)

## Entrées

| Paramètre     | Type de Donnée | Description |
|---------------|----------------|-------------|
| `nom_clip`    | COMBO[STRING]  | Spécifie le nom du modèle CLIP à charger. Ce nom est utilisé pour localiser le fichier du modèle dans une structure de répertoire prédéfinie. |
| `type`        | COMBO[STRING]  | Détermine le type de modèle CLIP à charger. À mesure que ComfyUI prend en charge plus de modèles, de nouveaux types seront ajoutés ici. Consultez la définition de la classe `CLIPLoader` dans [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) pour plus de détails. |
| `appareil`    | COMBO[STRING]  | Choisit l'appareil pour charger le modèle CLIP. `default` exécutera le modèle sur GPU, tandis que la sélection de `CPU` forcera le chargement sur CPU. |

### Options d'Appareil Expliquées

**Quand choisir "default" :**

- Vous avez suffisamment de mémoire GPU
- Vous voulez les meilleures performances
- Vous laissez le système optimiser automatiquement l'utilisation de la mémoire

**Quand choisir "cpu" :**

- Mémoire GPU insuffisante
- Besoin de réserver de la mémoire GPU pour d'autres modèles (comme UNet)
- Exécution dans un environnement avec peu de VRAM
- Besoins de débogage ou fins spéciales

**Impact sur les Performances**

L'exécution sur CPU sera beaucoup plus lente que sur GPU, mais peut économiser de la précieuse mémoire GPU pour d'autres composants plus importants du modèle. Dans les environnements avec des contraintes de mémoire, placer le modèle CLIP sur CPU est une stratégie d'optimisation courante.

### Combinaisons Prises en Charge

| Type de Modèle | Encodeur Correspondant |
|----------------|------------------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

À mesure que ComfyUI se met à jour, ces combinaisons peuvent s'étendre. Pour plus de détails, consultez la définition de la classe `CLIPLoader` dans [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|---------------|-------------|
| `clip`    | CLIP         | Le modèle CLIP chargé, prêt à être utilisé dans des tâches en aval ou pour un traitement ultérieur. |

## Notes Supplémentaires

Les modèles CLIP jouent un rôle fondamental en tant qu'encodeurs de texte dans ComfyUI, responsables de la conversion des prompts textuels en représentations numériques que les modèles de diffusion peuvent comprendre. Vous pouvez les considérer comme des traducteurs, chargés de traduire votre texte dans un langage que les grands modèles peuvent comprendre. Bien sûr, différents modèles ont leurs propres "dialectes", donc différents encodeurs CLIP sont nécessaires entre différentes architectures pour compléter le processus d'encodage de texte.
