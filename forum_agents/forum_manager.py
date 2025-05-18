from typing import List, Dict
from datetime import datetime, timedelta
import random
from .mining_agent import MiningAgent
from faker import Faker

class ForumManager:
    def __init__(self):
        self.agents: List[MiningAgent] = []
        self.threads: Dict[str, List[Dict]] = {}
        self.fake = Faker()
        self.topics = [
            'proof_of_work',
            'mining_app',
            'future_direction'
        ]
        
    def create_agent(self, expertise_level: str, mining_experience: int) -> MiningAgent:
        """Create a new mining agent with random username."""
        username = self.fake.user_name()
        agent_id = f"agent_{len(self.agents) + 1}"
        agent = MiningAgent(agent_id, username, expertise_level, mining_experience)
        self.agents.append(agent)
        return agent
    
    def create_thread(self, topic: str, initial_post: str) -> str:
        """Create a new discussion thread."""
        thread_id = f"thread_{len(self.threads) + 1}"
        self.threads[thread_id] = [{
            'content': initial_post,
            'timestamp': datetime.now().isoformat(),
            'topic': topic
        }]
        return thread_id
    
    def simulate_discussion(self, thread_id: str, duration_minutes: int = 30):
        """Simulate a discussion in a thread for a specified duration."""
        if thread_id not in self.threads:
            return
        
        end_time = datetime.now() + timedelta(minutes=duration_minutes)
        topic = self.threads[thread_id][0]['topic']
        
        while datetime.now() < end_time:
            # Select random agent to respond
            agent = random.choice(self.agents)
            
            # Get context from last few posts
            context = "\n".join([post['content'] for post in self.threads[thread_id][-3:]])
            
            # Generate and post response
            response = agent.generate_response(context, topic)
            post = agent.post_comment(response, thread_id)
            self.threads[thread_id].append(post)
            
            # Random delay between posts
            delay = random.randint(1, 5)
            datetime.now() + timedelta(minutes=delay)
    
    def get_thread_summary(self, thread_id: str) -> Dict:
        """Get a summary of a thread's discussion."""
        if thread_id not in self.threads:
            return {}
        
        return {
            'thread_id': thread_id,
            'topic': self.threads[thread_id][0]['topic'],
            'post_count': len(self.threads[thread_id]),
            'participants': len(set(post['agent_id'] for post in self.threads[thread_id])),
            'duration': (datetime.fromisoformat(self.threads[thread_id][-1]['timestamp']) - 
                        datetime.fromisoformat(self.threads[thread_id][0]['timestamp'])).total_seconds() / 60
        } 