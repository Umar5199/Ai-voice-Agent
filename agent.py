import os
from dotenv import load_dotenv
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import gladia, google, deepgram, silero

load_dotenv()

async def entrypoint(ctx: JobContext):
    # Connect to LiveKit room
    await ctx.connect()
    
    # Define your agent
    agent = Agent(
        instructions="""You are a helpful voice assistant. 
        Keep responses brief and conversational since this is a voice conversation."""
    )
    
    # Create session with all your working APIs
    session = AgentSession(
        vad=silero.VAD.load(),
        stt=gladia.STT(
            languages=["en"],  # English only for better accuracy
        ),
        llm=google.LLM(
            model="gemini-2.5-flash",  # Your working Gemini model
        ),
        tts=deepgram.TTS(
            model="aura-asteria-en",  # Clear, pleasant voice
        ),
    )
    
    # Start the agent
    await session.start(agent=agent, room=ctx.room)
    await session.generate_reply(
        instructions="Greet the user warmly. Say: 'Hello! I'm your voice assistant powered by Gemini. How can I help you today?'"
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))