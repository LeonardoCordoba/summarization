## Resumen de texto en español con Transformers // Abstractive summarization in Spanish with Transformers
Este trabajo es parte de la tesis de Maestría en Data Mining titulada "Generación de resúmenes de texto en español", por Leonardo Ignacio Córdoba. La defensa puede ser vista [aquí](https://www.youtube.com/watch?v=6TZbdWj3MxE&t=4s). 


En este repositorio se guardan ejemplos de uso de 5 modelos: dos modelos mt5 especializados en las tareas de MLSUM y de CC-NEWS-es-titles, ambas tareas de resumen, dos modelos Beto2Beto especializados en las mismas tareas y de Beto2Beto.

- En la carpeta ejemplos encontrarán 3 notebooks con ejemplos de uso.
- En la carpeta CC-NEWS-es-titles hay notebooks empleadas para generar el dataset.
- En anotaciones.csv se encuentran las anotaciones manuales con las cuales se compararon los resultados de mt5 y beto2beto, junto a Pegasus y el ground truth. 

### Recursos disponibilizados

Como parte de este trabajo se disponibilizan los siguientes recursos:

Conjuntos de datos son:
- CC-NEWS-ES: https://huggingface.co/datasets/LeoCordoba/CC-NEWS-ES
- CC-NEWS-ES-titles: https://huggingface.co/datasets/LeoCordoba/CC-NEWS-ES-titles


Los modelos entrenados son:
- MT5-small-mlsum: https://huggingface.co/LeoCordoba/mt5-small-mlsum
- MT5-small-cc-news-es-titles: https://huggingface.co/LeoCordoba/mt5-small-cc-news-es-titles
- Beto2Beto: https://huggingface.co/LeoCordoba/beto2beto
- Beto2Beto-cc-news-es-titles: https://huggingface.co/LeoCordoba/beto2beto-cc-news-es-titles
- Beto2Beto-mlsum: https://huggingface.co/LeoCordoba/beto2beto-mlsum