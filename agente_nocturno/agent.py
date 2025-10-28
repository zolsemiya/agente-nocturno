from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='crear texto para que se interprete musicalmente a partir de textos',
    instruction='Este agente te pedira responder 3 preguntas diferentes sobre una caminata en un humedal y a apartir de esto creara un texto erriquecido en terminos descriptivos para alimentar esta IA musical https://www.media.io/, las musicas generadas deben ser basadas en los generos musicales del altiplano de cundinamarca y boyaca entre los años 1920 y 1970',
)
