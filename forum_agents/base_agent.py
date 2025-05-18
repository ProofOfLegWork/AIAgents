from abc import ABC, abstractmethod
from typing import List, Dict
import random
from datetime import datetime
import json

class ForumAgent(ABC):
    def __init__(self, agent_id: str, username: str, personality: Dict):
        self.agent_id = agent_id
        self.username = username
        self.personality = personality
        self.post_history = []
        self.last_active = datetime.now()
        
    @abstractmethod
    def generate_response(self, context: str, topic: str) -> str:
        """Generate a response based on the agent's personality and the context."""
        pass
    
    def post_comment(self, content: str, thread_id: str) -> Dict:
        """Post a comment to the forum."""
        post = {
            'agent_id': self.agent_id,
            'username': self.username,
            'content': content,
            'thread_id': thread_id,
            'timestamp': datetime.now().isoformat()
        }
        self.post_history.append(post)
        self.last_active = datetime.now()
        return post
    
    def get_agent_state(self) -> Dict:
        """Get the current state of the agent."""
        return {
            'agent_id': self.agent_id,
            'username': self.username,
            'personality': self.personality,
            'post_count': len(self.post_history),
            'last_active': self.last_active.isoformat()
        } 