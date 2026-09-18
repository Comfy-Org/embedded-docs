# YuE2 Générer de la musique

Génère des tokens musicaux et un conditionnement acoustique à partir d'un style, de paroles et d'une notation ABC. Il renvoie le conditionnement et la durée générée en secondes, qui doivent être fournis au nœud Empty YuE2 Latent Audio. Si l'entrée ABC est laissée vide, le mode sélectionné est ignoré et le mode off est utilisé automatiquement.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `clip` | Le modèle CLIP utilisé pour tokeniser et encoder les entrées musicales. | CLIP | Oui | - |
| `style` | Texte décrivant le style musical. Prend en charge les entrées multilignes et les prompts dynamiques. | STRING | Oui | Texte multiligne |
| `paroles` | Paroles pour la musique générée. Prend en charge les entrées multilignes et les prompts dynamiques. | STRING | Oui | Texte multiligne |
| `abc` | Connectez le générateur ABC ou fournissez une partition modifiée. Laissez vide pour utiliser automatiquement le mode off. défaut : "" | STRING | Oui | Texte multiligne |
| `graine` | Graine aléatoire pour la génération. défaut : 0 | INT | Oui | 0 à 18446744073709551615 |
| `mode` | full : génère la mélodie et les accords ; melody : génère uniquement la mélodie, recommandé pour les reprises. défaut : "full" | COMBO | Oui | "full"<br>"melody" |
| `max_duration` | Durée maximale en secondes. Automatiquement réduite pour les prompts longs ; la génération peut s'arrêter plus tôt. défaut : 360.0 | FLOAT | Oui | 0.04 à 900.0 |
| `temperature` | Température d'échantillonnage pour la génération. défaut : 1.0 (avancé) | FLOAT | Oui | 0.0 à 5.0 |
| `top_p` | Seuil de probabilité pour l'échantillonnage par noyau. défaut : 0.95 (avancé) | FLOAT | Oui | 0.01 à 1.0 |
| `top_k` | Limite de l'échantillonnage top-k. défaut : 100 (avancé) | INT | Oui | 1 à 32768 |
| `repetition_penalty` | Pénalité appliquée aux tokens répétés. défaut : 1.2 (avancé) | FLOAT | Oui | 0.01 à 10.0 |
| `cfg_scale` | Guidage autorégressif pour le style et les paroles. 1.0 désactive CFG, ce qui correspond au flux de travail ABC. Utilisez 1.01 pour correspondre au guidage d'origine en mode off. défaut : 1.0 (avancé, facultatif) | FLOAT | Non | 0.0 à 100.0 |

Remarque : si `abc` est vide ou ne contient que des espaces, la sélection de `mode` est ignorée et le mode off est utilisé automatiquement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Conditionnement acoustique généré à partir des tokens musicaux. | CONDITIONING |
| `seconds` | Durée audio générée en secondes. Fournissez cette valeur au nœud Empty YuE2 Latent Audio. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/fr.md)

---
**Source fingerprint (SHA-256):** `5a88e185d2998c51acff7f0c76c8c35ca30b80b88cb541d97f9ab91566b5a3ed`
